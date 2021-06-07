if __name__ == "__main__":
    num = (int)(input())

    coins = [25,10,5,1]
    nums = [i - i for i in range(0,4)]

    total = 0
    for i in range(len(coins)):
        while(num >= coins[i]):
            num -= coins[i];
            nums[i] += 1
            total += 1

    print("total:{0}".format(total))
    for i in range(0 , len(nums)):
        print("fen{0}: {1}".format(coins[i] , nums[i]) , end=" ")