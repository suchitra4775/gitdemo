def CheckNum(Number):


    if(Number%2==0):
        print("Even Number")
    else:
        print("odd Number")


def main():
    print('enter the Number:')
    Number = int(input())
    CheckNum(Number)


if __name__=="__main__":
    main() 

