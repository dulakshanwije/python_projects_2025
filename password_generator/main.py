import random
import string

def password_generator():
    while True:
        try:
            length_input = input("Enter the desired password length: ").strip()
            length = int(length_input)
            
            if length < 8:
                raise ValueError("Password length must be at least 8 characters.")
                
            valid_responses = ['yes', 'no']
            
            include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
            if include_uppercase not in valid_responses:
                raise ValueError('Please use "yes" or "no" for uppercase letters.')
                
            include_special = input("Include special characters? (yes/no): ").strip().lower()
            if include_special not in valid_responses:
                raise ValueError('Please use "yes" or "no" for special characters.')
                
            include_digits = input("Include digits? (yes/no): ").strip().lower()
            if include_digits not in valid_responses:
                raise ValueError('Please use "yes" or "no" for digits.')
            
            lower = string.ascii_lowercase
            uppercase = string.ascii_uppercase if include_uppercase == 'yes' else ''
            specials = string.punctuation if include_special == 'yes' else ''
            digits = string.punctuation if include_digits == 'yes' else ''
            all_characters = lower + uppercase + specials + digits
            
            required_characters = []
            if include_digits == 'yes':
                required_characters.append(random.choice(digits))
            if include_uppercase == 'yes':
                required_characters.append(random.choice(uppercase))
            if include_special == 'yes':
                required_characters.append(random.choice(specials))
            
            remaining_characters = length - len(required_characters)
            password = required_characters
            
            for _ in range(remaining_characters):
                character = random.choice(all_characters)
                password.append(character)
            
            random.shuffle(password)
            
            password_str = "".join(password)
            
            return password_str
            
        except ValueError as ve:
            print(f"Error: {ve}")
            print("Try again!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Try again!")
            
if __name__ == '__main__':
    password = password_generator()
    print(password)