import argparse

class Argument:
    def __init__(self):
        parser: argparse = argparse.ArgumentParser()
        parser.add_argument("-p", "--path", help = "pass a path that is to be used for converting", required = True)
        parser.add_argument("-q", "--quality", help = "quality of converted image in procent", type = int, default = 80)
        parser.add_argument("-r", "--resize", help = "gives a max width solution in pixel and downscales the images that are bigger", type = int, default = 0)
        self.__args: argparse = parser.parse_args()

    def getPath(self) -> str:
        return self.__args.path

    def getQuality(self) -> int:
        return self.__args.quality

    def getResize(self) -> int:
        return self.__args.resize