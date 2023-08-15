def main():
    file_name = 'text_files/nameslist.txt'
    listed_elements = file_to_list(file_name)
    print(dict_counter(listed_elements))

def file_to_list(filename):
    with open(filename, 'r') as file:
        unpacked_list = file.read().split()
    return unpacked_list

def dict_counter(listed_elements):
    mydict = {}
    for i in listed_elements:
        if i in mydict.keys():
            mydict[i] += 1
        else:
            mydict[i] = 1
    return mydict

if __name__ == "__main__":
    main()