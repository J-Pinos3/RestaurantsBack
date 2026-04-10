import time

def fetch_data():
    time.sleep(2)
    return {"message":"Data fetched"}   


def process_data():
    time.sleep(1)
    return {"message":"Data processed"}   


def main():
    result1 = fetch_data()
    result2 = process_data()
    print(result1)
    print(result2)

main()