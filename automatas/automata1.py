from module import ReadText, WriteTextLines, ReadJSON
from pathlib import Path

# VOの各フォルダのうち、sub_jp.csvファイルが無いフォルダの名前をリストアップするpythonプログラムです
# 出力は"no_JP_sub_list.txtに書かれます
# excludes.txtにリストアップされたフォルダは無視します

config = ReadJSON("automatas/config.json")

EXCLUDES_PATH = config["excludeFileName"]
RESULT_LIST = config["noSubList"]

def main():
    VO = Path("./VO")
    try:
        excludes = ReadText(EXCLUDES_PATH)
    except:
        WriteTextLines(EXCLUDES_PATH)
        excludes = ""
    result = []
    folders = [folder for folder in VO.iterdir() if folder.is_dir()]
    for folder in folders:
        if folder.name in excludes:
            continue
        if not "sub_jp.csv" in [file.name for file in folder.iterdir() if file.is_file()]:
            print(f"no sub_jp.csv in {folder.name}")
            result.append(folder.name)
    WriteTextLines(RESULT_LIST, result)

if __name__ == "__main__":
    main()