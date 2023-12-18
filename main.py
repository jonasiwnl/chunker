from chunker import chunk_file, reconstruct_file

import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <FILE>")
        return
    
    file_path = sys.argv[1]

    print('chunking...')
    file_metadata = chunk_file(file_path)

    print('reconstructing...')
    reconstruct_file(file_metadata, False)

    print("success.")

if __name__ == '__main__':
    main()
