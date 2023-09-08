from sys import *

def Addition(iValue1,iValue2):
    return iValue1+iValue2

def main():

    if(len(argv)!=3):
        print("INSUFFIECIENT ARGUMENTS..")
        exit()

    print("APPLICATION NAME : ",argv[0])

    iSum = Addition(argv[1],argv[2])

    print("ADDITION IS :",iSum)

if __name__=="__main__":
    main()
    

