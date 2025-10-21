"""Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.



Вимоги до завдання:

Функція generator_numbers(text: str) повинна приймати рядок як аргумент і повертати генератор, що ітерує по всіх дійсних числах у тексті. Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
Функція sum_profit(text: str, func: Callable) має використовувати генератор generator_numbers для обчислення загальної суми чисел у вхідному рядку та приймати його як аргумент при виклику.
"""

import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """Аналізує текст і повертає генератор дійсних чисел.
    Дійсні числа відокремлені пробілами."""

    pattern = r"(?<!\S)-?\d+\.\d+(?!\S)"  # Регулярний вираз для пошуку дійсних чисел, відокремлених пробілами
    for match in re.finditer(
        pattern, text
    ):  # Ітеруємося по всіх знайдених співпадіннях
        yield float(match.group(0))  # Повертаємо знайдене число як float


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """Використовує функцію-генератор для обчислення загальної суми чисел."""
    numbers = func(text)
    return sum(numbers)  # Використовуємо генератор для обчислення суми чисел у тексті


# Приклад використання:

text = (
    "The total income of the employee consists of several parts: "
    "1000.01 as the base income, supplemented by additional earnings "
    "of 27.45 and 324.00 dollars."
)

total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
