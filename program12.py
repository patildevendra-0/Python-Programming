def Display(No):
    for i in range(1,11,1):
        print(No*i)

def main():
    print("Enter number")
    iValue = int (input())


    Display(iValue)

if __name__=="__main__":
    main()    