from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError, OperationalError
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends, HTTPException
from user import Base, User

SQLALCHEMY_DB_URL = "sqlite:///./tets.db"

engine = create_engine(
    SQLALCHEMY_DB_URL,
    connect_args={"check_same_thread": False}
)

Base.metadata.create_all(bind=engine) #create tables
SessionLocal = sessionmaker(autocommit =False, autoflush=False, bind=engine) #create session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def create_user(db:Session, usernam:str, email:str):
    try:
        db_user = User(username=usernam, email=email)
        db.add(db_user)
        db.commit()

        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        return  HTTPException(status_code=400, detail="User with this username or email already exists")


def get_user_by_id(db: Session, user_id: int):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return user
    except OperationalError:
        return HTTPException(status_code=500, detail="Database connection error")


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter( User.username == username ).first()


def update_user_email(db:Session, user_id: int, new_email: str):

    if not new_email:
        raise ValueError("Email is required")
    
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.email = new_email
        db.commit()
        db.refresh(db_user)

    return db_user


def delete_user(db:Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    
    return db_user
