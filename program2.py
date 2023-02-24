def Check_Divisible(No):
    if(No%5==0):
        if(No%3==0):
            return True
        else:
            False
    else:
        False            

def main():
    print("enter number:")
    iValue  = int(input())

    Ans = Check_Divisible(iValue)
    if (Ans==True):
        print("Number is Divisible by 3 And 5")
    else:
        print("Number is not Divisible by 3 And 5")
if __name__=="__main__":
    main()    