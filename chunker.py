from typing import Optional

import os
import math


CHUNK_SIZE = 8 * 1024 * 1024 # 8 MB

class FileChunksMetadata:

    def __init__(self, base_path: str, chunk_count: int, chunk_size: int):
        self.base_path = base_path
        self.chunk_count = chunk_count
        self.chunk_size = chunk_size

    def get_chunk_path(self, chunk_index: int) -> Optional[str]:
        if not chunk_index < self.chunk_count:
            return None
        return f'{self.base_path}.{chunk_index}'


def chunk_file(file_path: str, chunk_size: int = CHUNK_SIZE) -> FileChunksMetadata:
    chunk_count = math.ceil( os.path.getsize(file_path) / chunk_size )

    with open(file_path, 'rb') as file:
        for chunk_index in range(chunk_count):
            chunk_path = f'{file_path}.{chunk_index}'

            with open(chunk_path, 'wb') as chunk_file:
                chunk = file.read(chunk_size)
                chunk_file.write(chunk)

    return FileChunksMetadata(file_path, chunk_count, chunk_size)

def reconstruct_file(file_metadata: FileChunksMetadata, remove: bool = False) -> None:
    with open(file_metadata.base_path, 'wb') as file:
        for chunk_index in range(file_metadata.chunk_count):
            chunk_path = file_metadata.get_chunk_path(chunk_index)

            with open(chunk_path, 'rb') as chunk_file:
                chunk = chunk_file.read()
                file.write(chunk)

            if remove:
                os.remove(chunk_path)
