def Display(No):
    for i in range(1,No,1):
       if(No%i==0):
        print(i)

def main():
    print("Enter number")
    iValue = int (input())


    Display(iValue)

if __name__=="__main__":
    main()    