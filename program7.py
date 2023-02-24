def Display(No):
    Fact = 1
    for i in range(1,No,1):
        Fact  = Fact*i
    return Fact

def main():
    print("Enter number")
    iValue = int (input())


    Ans = Display(iValue)
    print(Ans)

if __name__=="__main__":
    main()    