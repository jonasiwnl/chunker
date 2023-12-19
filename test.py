from chunker import chunk_file, reconstruct_file

import hashlib
import os


CHUNK_SIZE = 1 # 1 byte lol.
DATA = b'''
Hello, World! this is supposed to be a long file! mrrp mrrp. I am a cat.
This text will be copilot generated. Long live copilot! I am a cat. Meow.
Hello, World! this is supposed to be a long file! mrrp mrrp. I am a cat.
This text will be copilot generated. Long live copilot! I am a cat. Meow.
Hello, World! this is supposed to be a long file! mrrp mrrp. I am a cat.
This text will be copilot generated. Long live copilot! I am a cat. Meow.
Hello, World! this is supposed to be a long file! mrrp mrrp. I am a cat.
This text will be copilot generated. Long live copilot! I am a cat. Meow.
Hello, World! this is supposed to be a long file! mrrp mrrp. I am a cat.
This text will be copilot generated. Long live copilot! I am a cat. Meow.
Hello, World! this is supposed to be a long file! mrrp mrrp. I am a cat.
This text will be copilot generated. Long live copilot! I am a cat. Meow.
'''

def main():
    print('Testing checksum...')

    original_hash = hashlib.sha256()
    with open('test.txt', 'wb') as file:
        file.write(DATA)
        original_hash.update(DATA)

    file_metadata = chunk_file('test.txt', CHUNK_SIZE)
    reconstruct_file(file_metadata, remove=True)

    reconstructed_hash = hashlib.sha256()
    with open('test.txt', 'rb') as file:
        reconstructed_hash.update(file.read())

    os.remove('test.txt')

    assert original_hash.digest() == reconstructed_hash.digest()

    print('PASSED.\n')

if __name__ == '__main__':
    main()
