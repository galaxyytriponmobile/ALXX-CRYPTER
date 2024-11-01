
# ALXX CRYPTER

ALXX CRYPTER is a simple file and folder encryption tool written in Python. It allows users to encrypt and decrypt files using a specified encryption key, ensuring that sensitive data is protected. This tool employs XOR encryption for file contents and uses SHA-512 for key hashing.

## Features

- **Encrypt Files**: Encrypt files in the specified directory with a chosen key.
- **Decrypt files**: File names will be lost, but content will be same as before.

# IMPORTANT
*IF YOU USE ENCRYPTOR, ALL FILE NAMES WILL BE LOST.*

*MAKE SURE TO COPY YOUR KEY, YOU WILL HAVE 10 SECONDS FOR IT.*

## Requirements

- Python 3.x
- `os`, `hashlib`, `time`, `platform`, `random`, `string`, `pathlib` modules (included in standard Python library)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/galaxyytriponmobile/ALXX-WEBSTER.git
   cd ALXX-WEBSTER
   ```

2. Run the encryption script:

   ```bash
   python main.py
   ```

   You will be prompted to enter the encryption key and the target folder path for encryption.

   If you would like to decrypt, run the `main.py` file, but all file names will be lost, use at caution.
