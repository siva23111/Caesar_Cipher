from PIL import Image

def encrypt(image_path, output_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()

    # Encrypt the image by applying a simple XOR operation with the key
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ key, g ^ key, b ^ key)
    
    # Save the encrypted image
    img.save(output_path)

def decrypt(image_path, output_path, key):
    # Decrypting is just applying the XOR operation again with the same key
    encrypt(image_path, output_path, key)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image?: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice! Please choose 'e' for encryption or 'd' for decryption.")
        return

    image_path = input("Enter the path to the image: ")
    output_path = input("Enter the output path for the image: ")
    key = int(input("Enter the encryption key (an integer): "))

    if choice == 'e':
        encrypt(image_path, output_path, key)
        print(f"Encrypted image saved as {output_path}")
    elif choice == 'd':
        decrypt(image_path, output_path, key)
        print(f"Decrypted image saved as {output_path}")

if __name__ == "__main__":
    main()