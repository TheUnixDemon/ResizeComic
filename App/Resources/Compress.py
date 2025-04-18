from PIL import Image
import os 

# check the type and more ...
class Compress:
    def __init__(self, quality: int):
        self.__quality: int = quality

    def compressImage(self, path: str):
        # skips file if not image
        self.__path: str = path
        if not self.__verifyFormat():
            return None
        # converts file into jpeg and makes it smaller
        try: 
            with Image.open(path) as img:
                print("Here" + path)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                convertPath: str = f"{os.path.splitext(path)[0]}.jpeg"
                convertPathTemp: str = f"{convertPath}.temp"
                img.save(convertPathTemp, format = "JPEG", quality = self.__quality)
            # checks if origin or new compression is more effizient and saves only that version
            if self.isSmaller(path, convertPathTemp):
                self.__cleanup(path)
                os.rename(convertPathTemp, convertPath)
            else:
                self.__cleanup(convertPathTemp)
        except Exception as e:
            print(f"Error occured: {e}")

    # checks if the compression is more efficient or not
    def isSmaller(self, originPath: str, convertPath: str) -> bool:
        origin: int = os.path.getsize(originPath)
        convert: int = os.path.getsize(convertPath)
        if convert < origin:
            return True
        return False

    def __verifyFormat(self):
        try:
            with Image.open(self.__path) as img:
                img.verify()
            return True
        except Exception:
            return False
        
    def __cleanup(self, path: str):
        os.remove(path)