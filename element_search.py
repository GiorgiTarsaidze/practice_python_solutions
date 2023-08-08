def main():
    print(determine([-3,-2,0,1,2,9,11,12,16],12))

def determine(my_list,number):
    start_index = 0
    last_index = len(my_list)-1

    while start_index <= last_index:
        middle_index = (last_index + start_index)//2

        middle_number = my_list[middle_index]
        #print(middle_number)       
        if number == middle_number:
            return True
        if number < middle_number:
            last_index = middle_index - 1
        else:
            start_index = middle_index + 1 
    return False

if __name__ == "__main__":
    main()