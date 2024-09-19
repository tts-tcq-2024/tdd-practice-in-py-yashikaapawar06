import re
from typing import List

def add(numbers: str) -> int:
    """Main function to add numbers from a string."""
    if not numbers:
        return 0
    
    numbers = replace_custom_delimiter(numbers)
    num_list = convert_to_numbers(numbers)
    validate_negatives(num_list)
    num_list = filter_large_numbers(num_list)
    
    return sum(num_list)

def replace_custom_delimiter(numbers: str) -> str:
    """Replace custom delimiters in the input string."""
    if numbers.startswith("//"):
        delimiter, numbers = re.split(r"\n", numbers[2:], maxsplit=1)
        numbers = numbers.replace(delimiter, ",")
    return numbers.replace("\n", ",")

def convert_to_numbers(numbers: str) -> List[int]:
    """Convert a string of numbers into a list of integers."""
    return list(map(int, numbers.split(",")))

def validate_negatives(num_list: List[int]) -> None:
    """Check for negative numbers and raise an error if found."""
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")

def filter_large_numbers(num_list: List[int]) -> List[int]:
    """Filter out numbers greater than 1000 from the list."""
    return [num for num in num_list if num <= 1000]
