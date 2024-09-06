from functools import reduce
def checkEven(number):
    if(number%2==0):
        return True
    return False
def multiplication(number1,number2):
    return number1*number2

def main():
    size = int(input('Enter the Size:'))
    lst = []
    print('enter the value:')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('User List:',lst)
    greterthen_number = tuple(filter(lambda number:number>=70,lst))
    smllerthen_number = tuple(filter(lambda number:number<=90,lst))
    filterlist = tuple(filter(checkEven,lst))
    reduce_list = reduce(multiplication,lst)
    print('greterthen number:',greterthen_number)
    print('smllerthen number:',smllerthen_number)
    print('filter List:',filterlist)  
    print('multiplication List:',reduce_list)   

if __name__=="__main__":
    main()
