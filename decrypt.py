import os
import hashlib
import platform
from pathlib import Path

def generate_encryption_key():
    key = input("Enter the decryption key you used: ")
    hashed_key = hashlib.sha512(key.encode()).hexdigest()
    return hashed_key

def xor_encrypt(data, key):
    key_bytes = key.encode()
    return bytearray((data[i] ^ key_bytes[i % len(key_bytes)]) for i in range(len(data)))

def decrypt_file(file_path, decryption_key):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_data = xor_encrypt(encrypted_data, decryption_key)
        
        with open(file_path, 'wb') as f:
            f.write(decrypted_data)
        
        decrypted_name = file_path.stem  # Remove the ".encrypted" extension
        decrypted_path = file_path.with_name(decrypted_name)
        file_path.rename(decrypted_path)
        print(f"Decrypted {file_path} to {decrypted_path}")

    except Exception as e:
        print(f"Failed to decrypt {file_path}: {e}")

def revert_names(map_file_path):
    # Read and reverse paths from map file
    with open(map_file_path, 'r') as map_file:
        for line in reversed(list(map_file)):
            original_path, encrypted_path = line.strip().split(" -> ")
            original_path, encrypted_path = Path(original_path), Path(encrypted_path)
            
            if encrypted_path.is_dir():
                encrypted_path.rename(original_path)
                print(f"Reverted folder {encrypted_path} to {original_path}")
            elif encrypted_path.is_file() and encrypted_path.suffix == ".encrypted":
                encrypted_path.rename(original_path)
                print(f"Reverted file {encrypted_path} to {original_path}")

def decrypt_files_and_folders(target_folder, decryption_key, map_file_path):
    # Revert folder and file names based on map
    revert_names(map_file_path)

    # Traverse and decrypt files
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            file_path = Path(root) / file
            if file_path.name == "file_map.txt":
                continue
            if file_path.suffix == ".encrypted":
                decrypt_file(file_path, decryption_key)

def main():
    decryption_key = generate_encryption_key()
    os_type = platform.system()
    print(f"Detected OS: {os_type}")
    
    if os_type == "Windows":
        target_folder = Path("C:/Users", "D:/Users", "A:/Users", "F:/Users")
    elif os_type in ["Linux", "Darwin"]:
        target_folder = Path("/etc", "/root")
    else:
        print("Unsupported OS.")
        return

    map_file_path = target_folder / "file_map.txt"
    if target_folder.exists() and map_file_path.exists():
        print(f"Decrypting files and folders in {target_folder}...")
        decrypt_files_and_folders(target_folder, decryption_key, map_file_path)
    else:
        print(f"Target folder {target_folder} or map file {map_file_path} does not exist.")

if __name__ == "__main__":
    main()
