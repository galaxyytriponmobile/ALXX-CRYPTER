import subprocess

def main():
    print("File and Folder Encryption Tool")
    print("1. Encrypt files and folders")
    print("2. Decrypt files and folders")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        print("Starting encryption process...")
        subprocess.run(['python', 'encrypt.py'])
    elif choice == '2':
        print("Starting decryption process...")
        subprocess.run(['python', 'decrypt.py'])
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
