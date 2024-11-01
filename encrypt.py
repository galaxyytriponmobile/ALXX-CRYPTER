import os
import hashlib
import time
import platform
import random
import string
from pathlib import Path

def generate_encryption_key():
    key = input("Enter the encryption key you want to use: ")
    hashed_key = hashlib.sha512(key.encode()).hexdigest()
    print("Your hashed key is:", hashed_key)
    print("You have 10 seconds to copy your key...")
    
    for i in range(10, 0, -1):
        print(i, end='\r', flush=True)
        time.sleep(1)
    
    return hashed_key

def xor_encrypt(data, key):
    key_bytes = key.encode()
    return bytearray((data[i] ^ key_bytes[i % len(key_bytes)]) for i in range(len(data)))

def encrypt_file(file_path, encryption_key, map_file):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        encrypted_data = xor_encrypt(data, encryption_key)
        
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        
        encrypted_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + '.encrypted'
        encrypted_path = file_path.with_name(encrypted_name)
        map_file.write(f"{file_path} -> {encrypted_path}\n")
        file_path.rename(encrypted_path)
        print(f"Encrypted {file_path} to {encrypted_path}")

    except Exception as e:
        print(f"Failed to encrypt {file_path}: {e}")

def encrypt_folder(folder_path, map_file):
    new_folder_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    new_folder_path = folder_path.parent / new_folder_name
    map_file.write(f"{folder_path} -> {new_folder_path}\n")
    folder_path.rename(new_folder_path)
    return new_folder_path

def encrypt_files_and_folders(target_folder, encryption_key, map_file_path):
    with open(map_file_path, 'w') as map_file:
        for root, dirs, files in os.walk(target_folder, topdown=False):
            # Encrypt files
            for file in files:
                file_path = Path(root) / file
                if file_path.name in ["loveletter.py", "file_map.txt"]:
                    continue
                encrypt_file(file_path, encryption_key, map_file)
            
            # Encrypt folder names
            for dir in dirs:
                dir_path = Path(root) / dir
                encrypted_path = encrypt_folder(dir_path, map_file)

def main():
    encryption_key = generate_encryption_key()
    
    target_folder = input("Enter the path of the folder you want to encrypt: ")
    target_folder = Path(target_folder)
    
    map_file_path = target_folder / "file_map.txt"
    
    if target_folder.exists():
        print(f"Encrypting files and folders in {target_folder}...")
        encrypt_files_and_folders(target_folder, encryption_key, map_file_path)
    else:
        print(f"Target folder {target_folder} does not exist.")

if __name__ == "__main__":
    main()
