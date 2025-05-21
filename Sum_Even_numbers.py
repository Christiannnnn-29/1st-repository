def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

my_list = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
result = sum_even_numbers(my_list)
print("Sum of even numbers:", result)
