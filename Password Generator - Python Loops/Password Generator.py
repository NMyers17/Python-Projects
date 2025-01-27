import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("""
 _____   _  _   ___     ___    __     __    __   _   _    __    ___   __       __   ___   __  _   ___   ___    __    _____    __    ___  
|_   _| | || | | __|   | _,\  /  \  /' _/ /' _/ | | | |  /__\  | _ \ | _\     / _] | __| |  \| | | __| | _ \  /  \  |_   _|  /__\  | _ \ 
  | |   | >< | | _|    | v_/ | /\ | `._`. `._`. | 'V' | | \/ | | v / | v |   | [/\ | _|  | | ' | | _|  | v / | /\ |   | |   | \/ | | v / 
  |_|   |_||_| |___|   |_|   |_||_| |___/ |___/ !_/ \_!  \__/  |_|_\ |__/     \__/ |___| |_|\__| |___| |_|_\ |_||_|   |_|    \__/  |_|_\ 

 """)

# Gather user inputs
input_characters = int(input("How many characters would you like your password to be?\n"))
input_numbers = input("Do you want to include numbers? (Y/N)\n")
input_symbols = input("Do you want to include symbols? (Y/N)\n")

# Determine the number of each character type
num_letters = random.randint(input_characters // 3, input_characters)
num_numbers = random.randint(1, input_characters - num_letters - 1) if input_numbers.lower() == 'y' or 'Y' else 0
num_symbols = input_characters - num_letters - num_numbers if input_symbols.lower() == 'y' or 'Y' else 0

password_list = []

# Add letters
for _ in range(num_letters):
    password_list.append(random.choice(letters))
# Add numbers
for _ in range(num_numbers):
    password_list.append(random.choice(numbers))
# Add symbols
for _ in range(num_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
password = ''.join(password_list)

print(f"Your newly generated password is: {password}")