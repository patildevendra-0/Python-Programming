def Display(No):
    iSum = 0
    for i in range(1,No,1):
        if(No%i==0):
            iSum = iSum+i
    return iSum        
def Check_Perfect(No):
    ans = Display(No)
    if (ans==No):
        print("perfect number")
    else:
        print("not perfect number")    

def main():
    print("Enter number")
    iValue = int (input())


    Ans = Check_Perfect(iValue)

if __name__=="__main__":
    main()    