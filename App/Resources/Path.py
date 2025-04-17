import os

class Path:
    def __init__(self, targetDir: str):
        self.__targetDir: str = targetDir
        self.__checkDir()

    # returns all paths to files in targetDir
    def getPaths(self) -> dict[str, str]:
        try:
            paths: list[str] = []
            for root, dirs, files in os. walk(self.__targetDir):
                for file in files:
                    path: str = os.path.join(root, file)
                    paths.append(path)
            return paths
        except Exception as e:
            print(f"Error occurred: {e}")

    # checks if passed directory can be found
    def __checkDir(self):
        try:
            if not os.path.exists(self.__targetDir):
                raise f"Directory *{self.__targetDir}* not found"
        except Exception as e:
            print(f"Error occurred: {e}")
            exit()