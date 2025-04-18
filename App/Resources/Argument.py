import argparse

class Argument:
    def __init__(self):
        parser: argparse = argparse.ArgumentParser()
        parser.add_argument("-p", "--path", help = "pass a path that is to be used for converting", required = True)
        parser.add_argument("-q", "--quality", help = "quality of converted image in procent", type = int, default = 75)
        self.__args: argparse = parser.parse_args()

    def getPath(self) -> str:
        return self.__args.path

    def getQuality(self) -> int:
        return self.__args.quality