
import Arithematic

def Arithematic_operations(iNo1,iNo2):
    
    iSum = Arithematic.Addition(iNo1,iNo2)
    print("ADDITION IS :  ",iSum)

    iMul = Arithematic.Multiplication(iNo1,iNo2)
    print("MULTIPLICATION IS: ",iMul)

    iDiv = Arithematic.Division(iNo1,iNo2)
    print("DIVISION IS: ",iDiv)

    iSub = Arithematic.Substraction(iNo1,iNo2)
    print("SUBSTRACTION IS : ",iSub)


def main():

    print("ENTER THE FIRST NUMBER: ")
    iValue1 = int(input())

    print("ENTER THE SECOUND NUMBER:")
    iValue2 = int(input())

    Arithematic_operations(iValue1,iValue2)
    

if __name__=="__main__":
    main()    