# solutions/Yunus Evangeline/email_generator.py

import random

def generate_email(name, curp):
    birth_year = curp[4:6]  # Extract year from CURP
    username = name.lower().replace(" ", ".")
    suffix = str(random.randint(100, 999))
    email = f"{username}{birth_year}{suffix}@outlook.com"
    return email

# Example usage
if __name__ == "__main__":
    name = "Gaston Galindo"
    curp = "TOGG960224HDFRLS09"
    print(generate_email(name, curp))
