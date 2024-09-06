def people(remove):
    return remove


def main():
    lst = ['HEM-234','HML-123','HELLO-99']
    cleaned_lst = [item.split('-')[0] for item in lst]
    print(cleaned_lst)

if __name__ == "__main__":
    main()



