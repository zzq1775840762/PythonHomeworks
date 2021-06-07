def recall(days , num):
    while(days > 1):
        num = (num + 1) * 2
        days -= 1
    return num

if __name__ == "__main__":
    print("sum of peach: {0}".format(recall(2 , 1)));