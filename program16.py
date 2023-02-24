def Display_Digits(iNo):
    iCnt=0
    iSum = 0
    while (iNo>0):
        iDigit = iNo%10
        iSum = iSum+iDigit
        iNo = iNo//10
        
    return  iSum
        
def main():
    print("Enter number")
    iValue = int (input())

    Ans=Display_Digits(iValue)
    print(Ans)
if __name__=="__main__":
    main()    