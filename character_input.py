def main():
    name = input("Please enter you name: ").strip().capitalize()
    age = get_age()
    
    future_year = year_calculator(age)
    print(f"Hello {name},\nyou will be 100 years old in {future_year}.")

def get_age():
    while True:
        try:
            age = int(input("Please enter you age: "))
            if 0<= age <= 100:
                return age
            else:
                print("Invalid Age!")
        except ValueError:
            print("Invalid input!")
            
def year_calculator(age):
    future_year = 100-age+2023
    return future_year

if __name__ == "__main__":
    main()