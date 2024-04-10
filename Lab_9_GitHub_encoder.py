# Encoder Lab 9 - Gabriel Wong

def encode(password: str) -> str:
    encoded_password = ' '
    for i in password:
        encoded = int(i) + 3
        if encoded > 9:
            encoded = str(encoded)[1:]
        encoded_password += str(encoded)
    return encoded_password
