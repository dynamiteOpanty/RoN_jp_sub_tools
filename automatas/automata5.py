from backyard.module import ReadJSON, ReadText, WriteTextLines
from os import mkdir
from shutil import copy as shcopy
from pathlib import Path

# VOの各フォルダのsub_jp.csv、sub_en.csvのみのコピーを作成します
# 実行結果はautomatas/フォルダ内にVOという名前で出力されます

config = ReadJSON("./automatas/backyard/config.json")
EXCLUDES_PATH = f"./automatas/backyard/{config['excludeFileName']}.txt"
RESULT_DIRECTORY = f"./automatas/VO"


def main():
    VO = Path("./VO")
    try:
        excludes = ReadText(EXCLUDES_PATH)
    except:
        WriteTextLines(EXCLUDES_PATH)
        excludes = ""
    if not Path(RESULT_DIRECTORY).exists():
        mkdir(RESULT_DIRECTORY)
    folders = [folder for folder in VO.iterdir() if folder.is_dir()]
    for folder in folders:
        if folder in excludes:
            continue
        for file in folder.iterdir():
            if file.name == "sub_jp.csv" or file.name == "sub_en.csv":
                targetPath = Path(f"{RESULT_DIRECTORY}/{file.relative_to(VO)}").parent
                if not targetPath.exists():
                    mkdir(targetPath)
                shcopy(file.relative_to(""), targetPath)
    print("done!")


if __name__ == "__main__":
    main()
