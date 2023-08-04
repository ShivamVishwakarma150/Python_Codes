# Print user input table
def print_table_of_2(limit):
    for i in range(1, limit + 1):
        result = 2 * i
        print(f"2 x {i} = {result}")


user_input = int(input("Enter the limit for the table of 2: "))
print_table_of_2(user_input)