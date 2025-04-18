from PIL import Image
import os

from Resources.Argument import Argument
from Resources.Path import Path
from Resources.Compress import Compress
from Resources.Pack import Pack

# argument variables
argument: Argument = Argument()
targetDir: str = argument.getPath()

# paths to the internal files of targetDir
path: Path = Path(targetDir)
paths: list[str] = path.getPaths()

compress: Compress = Compress(argument.getQuality())
for path in paths:
    # handles files that ends with a compression ending declared within formats
    endsWith: str = os.path.splitext(path)[1]
    if endsWith == ".cbz":
        pack: Pack = Pack(path)
        files: list[str] = pack.unpack()
        for file in files:
            compress.compressImage(file)
        pack.pack()

    compress.compressImage(path)