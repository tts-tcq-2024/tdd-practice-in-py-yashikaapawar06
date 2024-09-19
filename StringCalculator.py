def add(numbers: str) -> int:
    return 0

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    return int(numbers)

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    num_list = list(map(int, numbers.split(",")))
    return sum(num_list)
    
def convert_to_numbers(numbers: str) -> list:
    return list(map(int, numbers.split(",")))

def filter_large_numbers(num_list: list) -> list:
    return [num for num in num_list if num <= 1000]
    
def add(numbers: str) -> int:
    if not numbers:
        return 0
    num_list = convert_to_numbers(numbers)
    num_list = filter_large_numbers(num_list)
    return sum(num_list)



