def Display(No):
    iCnt = No
    while(iCnt>=1):
        print(iCnt)
        iCnt = iCnt-1

            

def main():
    print("Enter number")
    iValue = int (input())


    Display(iValue)

if __name__=="__main__":
    main()    