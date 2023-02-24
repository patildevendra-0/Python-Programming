def Display(No):
    iSum = 0
    for i in range(1,No,1):
        if(No%i==0):
            iSum = iSum+i
    return iSum        

def main():
    print("Enter number")
    iValue = int (input())


    Ans = Display(iValue)
    print(Ans)

if __name__=="__main__":
    main()    