from module import ReadText, WriteTextLines, ReadCSV, WriteCSV, ReadJSON
from pathlib import Path

# VOの各フォルダの、sub_enの内容の順番を基準にして、sub_jpの内容の順番を変更するpythonプログラムです
# 出力として各sub_jp.csvを書き換えます
# excludes.txt、no_JP_sub_list.txtにリストアップされたフォルダは無視します

config = ReadJSON("config.json")
excludespath = config["excludeFileName"]
noSubList = config["noSubList"]

def main():
    VO = Path("./VO")
    try:
        excludes = ReadText(excludespath)
    except:
        WriteTextLines(excludespath)
        excludes = ""
    try:
        noSub = ReadText(noSubList)
    except:
        print("noSub list wasn't found")
        exit(-1)
    folders = [folder for folder in VO.iterdir() if folder.is_dir()]
    for folder in folders:
        if folder.name in excludes or folder.name in noSub:
            continue
        for file in folder.iterdir():
            if file.name == "sub_jp.csv":
                subJpPath = file
            elif file.name == "sub_en.csv":
                subEnPath = file
            continue
        try:
            type(subJpPath)
            type(subEnPath)
        except:
            print("error. either sub_jp or sub_en wasn't found.")
            exit(-1)
        subEn = ReadCSV(subEnPath.absolute())
        subJp = ReadCSV(subJpPath.absolute())
        subJpResult = [["Key", "Dialogue", "Context"]]
        for i in range(1, len(subEn)):
            for o in range(1, len(subJp)):
                if subEn[i][0] == subJp[o][0]:
                    subJpResult.append(subJp[o])
        WriteCSV(f"{folder}/sub_jp.csv", subJpResult)
    print("done")

if __name__ == "__main__":
    main()