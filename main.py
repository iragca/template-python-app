from src.config import DirectoryPaths as dir
from src.utils import greetings, ensure_path, ensure_file
from typer import Typer

app = Typer()


@app.command()
def main():
    greetings(dir.PROJECT_ROOT.value.name)


@app.command()
def init_dirs():
    ensure_file(dir.ENV_FILE.value)
    ensure_path(dir.DATA.value)
    ensure_path(dir.EXTERNAL_DATA.value)


if __name__ == "__main__":
    app()
