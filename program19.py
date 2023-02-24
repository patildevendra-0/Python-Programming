def Display_Digits(iNo):
    iCnt=0
    
    iRev = 0
    if(iNo<0):
        iNo = -iNo
    if(iNo==0):
        Even = Even+1  
    while (iNo!=0):
        iDigit = iNo%10
        iRev = (iRev*10)+iDigit
        iNo = iNo//10
    return iRev
   
        
def main():
    print("Enter number")
    iValue = int (input())

    Ans=Display_Digits(iValue)
    print(Ans)
if __name__=="__main__":
    main()    