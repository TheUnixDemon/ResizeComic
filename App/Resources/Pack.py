import os
import shutil
import zipfile

class Pack:
    def __init__(self, path: str):
        self.__path: str = path
        self.__unpackDir: str = os.path.splitext(self.__path)[0] # name of dir where path data lies

    # returns a list of paths with internal files
    def unpack(self) -> list[str]:
        with zipfile.ZipFile(self.__path, 'r') as zip_ref:
            zip_ref.extractall(self.__unpackDir)
            files: list[str] = zip_ref.namelist()
            paths: list[str] = [os.path.join(self.__unpackDir, file) for file in files]
        return paths

    def pack(self):
        with zipfile.ZipFile(self.__path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            for root, _, files in os.walk(self.__unpackDir):
                for file in files:
                    pathFile = os.path.join(root, file)
                    relPath = os.path.relpath(pathFile, self.__unpackDir)
                    zip_ref.write(pathFile, relPath)
        self.__cleanup()

    def __cleanup(self):
        shutil.rmtree(self.__unpackDir)