alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode to encrypt, type 'decode' to decrypt:\n").lower()
text = input("type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result:{cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount

        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the decoded result:{output_text}")

def caesar(orginal_text, shift_amount, enocde_or_deocde):
    output_text = ""

    for letter in original_text:

        if enocde_or_deocde == "decode":
            shift_amount *= -1
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the decoded result:{output_text}")

encrypt(original_text=text, shift_amount=shift)
decrypt(original_text=text, shift_amount=shift)