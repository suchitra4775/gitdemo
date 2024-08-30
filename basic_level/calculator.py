import aithmaticmod
def main():
    print('Choose operation 1/2/3/4/5/6/7/')
    select = int(input('Enter 1/2/3/4/5/6/7'))
    num1=int(input('Enter first number'))
    num2=int(input('Enter second number'))
    if(select==1):

    
        output = aithmaticmod.Addition(num1,num2)
        print('Addition:',output)
    elif(select==2):
        output = aithmaticmod.Subtraction(num1,num2)
        print('Subtraction:',output)
    elif(select==3):
        output = aithmaticmod.floor(num1,num2)
        print('floor:',output)
    elif(select==4):
        output = aithmaticmod.modulus(num1,num2)
        print('modulus:',output)
    elif(select==5):
        output = aithmaticmod.Multiplication(num1,num2)
        print('multiplication:',output)
    elif(select==6):
        output = aithmaticmod.power(num1,num2)
        print('power:',output)
    elif(select==7):
        output = aithmaticmod.Division(num1,num2)
        print('division:',output)
    else:
        print('Select 1/2/3/4')

if __name__=="__main__":
    main()

