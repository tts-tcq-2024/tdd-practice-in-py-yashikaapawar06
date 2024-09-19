import re

def add(numbers: str) -> int:
    if not numbers:
        return 0
    numbers = handle_custom_delimiter(numbers)
    num_list = convert_to_numbers(numbers)
    check_for_negatives(num_list)
    return calculate_sum(num_list)

def handle_custom_delimiter(numbers: str) -> str:
    if numbers.startswith("//"):
        delimiter, numbers = re.split(r"\n", numbers[2:], maxsplit=1)
        return numbers.replace(delimiter, ",")
    return numbers

def convert_to_numbers(numbers: str) -> list:
    numbers = numbers.replace("\n", ",")
    return list(map(int, numbers.split(",")))

def check_for_negatives(num_list: list) -> None:
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

def calculate_sum(num_list: list) -> int:
    return sum(filter_numbers(num_list))

def filter_numbers(num_list: list) -> list:
    return [num for num in num_list if num <= 1000]
