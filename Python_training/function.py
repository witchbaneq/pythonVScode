def get_user_numbers():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    return {
        "first_number": first_number,
        "second_number": second_number
    }



def sum_of_numbers(numbers, additional_number, minus_number=False):
    result = numbers.get("first_number") + numbers.get("second_number") + additional_number
    if minus_number:
        result -= 2
    return result



user_one_numbers = get_user_numbers()
user_two_numbers = get_user_numbers()

first_sum = sum_of_numbers(user_one_numbers, 0, minus_number=True)
second_sum = sum_of_numbers(user_two_numbers, 1)

print(f"User One's numbers: {user_one_numbers['first_number']}, {user_one_numbers['second_number']}")

print("Now, let's get numbers for User Two.")

print(f"User Two's numbers: {user_two_numbers['first_number']}, {user_two_numbers['second_number']}")

print("Calculating sums...")

print(f"User One's sum: {first_sum}")

print("Now, let's calculate User Two's sum.")

print(f"User Two's sum: {second_sum}")