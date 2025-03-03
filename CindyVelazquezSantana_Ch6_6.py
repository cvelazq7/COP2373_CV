import re


# Function to validate phone number (Format: (XXX) XXX-XXXX or XXX-XXX-XXXX)
def validate_phone_number(phone_number):
    pattern = r'^(?:\(\d{3}\)\s?|\d{3}-)\d{3}-\d{4}$'
    return bool(re.match(pattern, phone_number))


# Function to validate Social Security Number (SSN) (Format: XXX-XX-XXXX)
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))


# Function to validate zip code (Format: XXXXX or XXXXX-XXXX)
def validate_zip_code(zip_code):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))


# Main function to get input from user and check validity
def main():
    phone_number = input("Enter your phone number (XXX-XXX-XXXX or (XXX) XXX-XXXX): ")
    ssn = input("Enter your Social Security Number (XXX-XX-XXXX): ")
    zip_code = input("Enter your ZIP code (XXXXX or XXXXX-XXXX): ")

    # Check and display results for phone number
    if validate_phone_number(phone_number):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    # Check and display results for SSN
    if validate_ssn(ssn):
        print("Social Security Number is valid.")
    else:
        print("Social Security Number is invalid.")

    # Check and display results for ZIP code
    if validate_zip_code(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")


# Test the functions
if __name__ == "__main__":
    main()