def Display_Digits(iNo):
    iCnt=0
    while (iNo>0):
        iDigit = iNo%10
        iNo = iNo//10
        iCnt = iCnt+1
    return iCnt    
        
def main():
    print("Enter number")
    iValue = int (input())

    Ans=Display_Digits(iValue)
    print(Ans)
if __name__=="__main__":
    main()    