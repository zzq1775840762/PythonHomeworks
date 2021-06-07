if __name__ == '__main__':
    for i in range(1 , 10):
        for j in range(1 , 10):
            if i >= j :
                print("%d * %d = %2d"%(j , i , i * j) , end="\t")
        print()