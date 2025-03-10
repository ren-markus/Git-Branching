from get_name import *
from validate_age import *
from survey import *

print("=" * 35)
print("Welcome to voting eligibility check")
print("=" * 35)
print("\n")

user_name = get_name()
print(f"Hello {user_name}!\n")

age = int(input("Enter your age: "))
validate_age(age)

survey_flag = input("Would you like to participate in our survey? (Y/N): ")

if survey_flag == 'Y':
    survey()

print("\nThank you! Please visit again.\n\n")