if __name__ == "__main__":
    days = 1
    heght = 8e-5
    target = 8848.13
    while heght < target:
        days += 1
        heght *= 2
    print("days:{0}".format(days))