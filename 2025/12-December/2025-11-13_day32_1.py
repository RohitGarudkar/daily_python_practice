#age_validation_with_custom_exception.py
class AgeException(Exception):
    """Custom exception for invalid age input."""
    pass


def check_age(age):
    if age < 0:
        raise AgeException("Age cannot be negative.")
    elif age < 18:
        raise AgeException("You must be at least 18 years old.")
    else: 
        print("Age is valid!")


# Example usage
try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError:
    print("Invalid input! Please enter a number.")
except AgeException as e:
    print("Age Error:", e)
