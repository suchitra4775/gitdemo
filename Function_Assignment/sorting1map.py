def people(item):
    return sorted
    
def main():
    name_list = [
    {'name':'shreya','surname':'kakade','age':15},
    {'name':'pratiksha','surname':'rokde','age':13},
    {'name':'prerna','surname':'munde','age':15}
    ]
    sorted_name_list = sorted(name_list, key=lambda x: x['name'])
    print(sorted_name_list)
if __name__=="__main__":
    main()

