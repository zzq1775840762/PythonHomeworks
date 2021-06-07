if __name__ == "__main__":
    for a in range(0 , 100):
        for b in range(0 , 100):
            for c in range(0 , 100 , 3):
                #print(a , b , c)
                if a + b + c == 100 and 3 * a + 5 * b + c / 3 == 100:
                    print(a , b , c)