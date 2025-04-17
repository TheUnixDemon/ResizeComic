import os

class Path:
    def __init__(self, targetDir: str):
        self.__targetDir: str = targetDir

    # returns all paths to files in targetDir
    def getPaths(self) -> dict[str, str]:
        try:
            paths: dict[str, str] = {}
            for root, dirs, files in os. walk(self.__targetDir):
                for file in files:
                    sourcePath: str = os.path.join(root, file)
                    paths[sourcePath] = sourcePath.replace(self.__targetDir, self.__targetDir)
            return paths
        except Exception as e:
            print(f"Error occurred: {e}")

    # checks if passed directory can be found
    def checkDir(self):
        try:
            if not os.path.exists(self.__targetDir):
                raise f"Directory *{self.__sourceDirectory}* not found"
        except Exception as e:
            print(f"Error occurred: {e}")
            exit()