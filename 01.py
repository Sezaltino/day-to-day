def filter_pairs(numbers):
    return [value for value in numbers if value%2 == 0] #list comprehension deve ter os []

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 23, 28]
    results = filter_pairs(numbers)
    print(results)