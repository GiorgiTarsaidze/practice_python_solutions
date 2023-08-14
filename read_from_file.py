def main():
    file_name = 'namelist.txt'
    print(open_file(file_name))

def open_file(filename):
    with open(filename, 'r') as file:
        unpacked_list = file.read().split()
        
        mydict = {}
        for i in unpacked_list:
            if i in mydict.keys():
                mydict[i] += 1
            else:
                mydict[i] = 1
    return mydict

if __name__ == "__main__":
    main()