import shutil, os
from typing import BinaryIO


class FileEditor:
    
    @staticmethod
    async def upload_file(filename: str, content: BinaryIO) -> bool:
        if not os.path.exists(f'forms/{filename}'):
            with await open(f'forms/{filename}', "wb") as wf:
                shutil.copyfileobj(content, wf)
                content.close()
            return True