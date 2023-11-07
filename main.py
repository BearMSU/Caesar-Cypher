alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # if non-letters will not be shifted, otherwise letters will.
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#While loop to start the re-use program loop
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  # If user shifts a high number too far out of range, this will acount for that.
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  # Allows for reuse
  result = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
  if result == "no":
    print("Thank you for using the Caesar Cipher. Goodbye.")
    should_continue = False
