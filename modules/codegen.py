from string import ascii_lowercase, digits
from random import choice

def generate_2fa_code():
 
    numbers = "0123456789"

    code = ""
    for _ in range(6):
        code += choice(numbers)
    
    return code

def generate_backup_code():
 
    characters = ascii_lowercase + digits

    code_1 = ""
    for _ in range(4):
        code_1 += choice(characters)
    
    code_2 = ""
    for _ in range(4):
        code_2 += choice(characters)
    
    return f"{code_1}-{code_2}"

# print(f"Backup Code: {generate_backup_code()}")
# print(f"2FA Code: {generate_2fa_code()}")

# https://github.com/belux17