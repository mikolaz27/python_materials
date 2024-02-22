# def func_test(a: int) -> None:
#     print(a)
#
# 0 + func_test("sdas")
#
#
# def func(num: int | float) -> int | float:
#     return num + 5

def func(day):
    """
    Function: func

    Description:
    This function takes a string parameter 'day' and returns a corresponding message based on the day.

    Parameters:
    - day (str): The day of the week.

    Returns:
    - str: Message based on the day.

    Example:
    >>> func("Monday")
    'Here we go again...'

    >>> func("Friday")
    'Happy Friday!'

    >>> func("Saturday")
    'Yay, weekend!'

    >>> func("Sunday")
    'Yay, weekend!'

    >>> func("Wednesday")
    'Just another day...'
    """
    match day:
        case "Monday":
            return "Here we go again..."
        case "Friday":
            return "Happy Friday!"
        case "Saturday" | "Sunday":  # Multiple literals can be combined with `|`
            return "Yay, weekend!"
        case _:
            return "Just another day..."
#
#
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    gender: str


def func(person):  # person is instance of `Person` class
    match person:
        # This is not a constructor
        case Person(name, age,
                    gender) if age < 18:  # guard for extra filtering
            print(f"{name} is a child.")
        case Person(name=name, age=_,
                    gender="male"):  # Wildcard ("throwaway" variable) can be used
            print(f"{name} is man.")
        case Person(name=name, age=_, gender="female"):
            print(f"{name} is woman.")
        case Person(name, age, gender):  # Positional arguments work
            print(f"{name} is {age} years old.")


func(Person("Lucy", 30, "female"))
