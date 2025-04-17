from Argument import Argument
from Resources.Path import Path

# argument variables
#argument: Argument = Argument()
#targetDir: str = argument.getPath()
targetDir: str = "./Compressed" # only for testing, afterwards its argument.getPath()

# paths to the internal files of targetDir
path: Path = Path(targetDir)
print(path.getPaths())