from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

def age_group(age):
    if age < 18:
        return "Minor"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

try:
    year = int(input("Enter your birth year: "))
    age = calculate_age(year)
    group = age_group(age)

    print(f"You are {age} years old.")
    print(f"You are classified as: {group}")
except ValueError:
    print("Please enter a valid year.")
