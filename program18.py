def Display_Digits(iNo):
    iCnt=0
    Even = 0
    odd= 0
    if(iNo<0):
        iNo = -iNo
    if(iNo==0):
        Even = Even+1  
    while (iNo!=0):
        iDigit = iNo%10
        if(iNo%2==0):
             Even = Even+1
        else:
            odd = odd+1     
        iNo = iNo//10
    
    print("even:",Even) 
    print("odd:",odd) 
        
def main():
    print("Enter number")
    iValue = int (input())

    Ans=Display_Digits(iValue)
    print(Ans)
if __name__=="__main__":
    main()    