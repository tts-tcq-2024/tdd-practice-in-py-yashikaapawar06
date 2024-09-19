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

