
def Check_Pallindrome(iNo):
    iTemp = iNo
    iRev=0
    iCnt = 0
    while(iNo!=0):
        iDigit = iNo%10
        iRev = (iRev*10)+iDigit
        iNo = iNo//10  
        iCnt+=iCnt      
    if(iTemp==iRev):
        return True
    else:
        return False    
       

            

def main():
    print("Enter the value:")
    iValue = int(input())

    iRet = Check_Pallindrome(iValue)
    if(iRet == True):
        print("{}number is pallindrome")
    else:
        print("{}number is not pallindrome") 
    


if __name__=="__main__":
    main()