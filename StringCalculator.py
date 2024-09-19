import re

def add(numbers: str) -> int:
    if numbers == "":
        return 0
    
    if numbers.startswith("//"):
        delimiter, numbers = re.split(r"\n", numbers[2:], maxsplit=1)
        numbers = numbers.replace(delimiter, ",")
        
    numbers = numbers.replace("\n", ",")
    
    num_list = list(map(int, numbers.split(",")))
    
  
    negatives = [num for num in num_list if num < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {', '.join(map(str, negatives))}")
    
   
    num_list = [num for num in num_list if num <= 1000]
    
    return sum(num_list)

