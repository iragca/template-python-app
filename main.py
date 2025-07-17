from src.config import DirectoryPaths as dir
from src.utils import greetings


def main():
    greetings(dir.PROJECT_ROOT.value.name)


if __name__ == "__main__":
    main()
