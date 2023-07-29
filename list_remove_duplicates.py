import random

def main():
    random_list = generate_list()
    filtered_list = filter_list((random_list))
    print(f"Random list: {random_list}\nFiltered List without duplicates: {filtered_list}")

def generate_list():
    a = random.sample(range(30),10)
    return random.choices(a,k=10)

def filter_list(my_list):
    return list(set(my_list))

# Solution with loops
# def filter_list(my_list):
#     filtered_list = []
#     for element in my_list:
#         if element not in filtered_list:
#             filtered_list.append(element)
#     return filtered_list

if __name__ == "__main__":
    main()