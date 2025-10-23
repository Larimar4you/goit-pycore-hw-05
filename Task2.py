import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """Аналізує текст і повертає генератор дійсних чисел.
    Дійсні числа відокремлені пробілами."""

    pattern = r"(?<!\S)-?\d+\.\d+(?!\S)"  
    for match in re.finditer(
        pattern, text
    ):  
        yield float(match.group(0))  


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """Використовує функцію-генератор для обчислення загальної суми чисел."""
    numbers = func(text)
    return sum(numbers) 


# Приклад використання:

text = (
    "The total income of the employee consists of several parts: "
    "1000.01 as the base income, supplemented by additional earnings "
    "of 27.45 and 324.00 dollars."
)

total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
