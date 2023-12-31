from pathlib import Path

# VOの各フォルダの、sub_enの内容の順番を基準にして、sub_jpの内容の順番を変更するpythonプログラムです
# 出力として各sub_jp.csvを書き換えます
# excludes.txt、no_JP_sub_list.txtにリストアップされたフォルダは無視します

dir = "./automata/"
excludesname = "excludes"
noSubname = "no_JP_sub_list"
excludespath = f"{dir}/{excludesname}.txt"
noSubList = f"{dir}/{noSubname}.txt"

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

def ReadText(path: str):
    with open(file=path, mode="r", encoding="utf-8") as file:
        result = []
        for line in file:
            result.append(line.replace("\n", ""))
        return result

def WriteTextLines(path: str, text=""):
    with open(file=path, mode="w", encoding="utf-8") as file:
        for line in text:
            file.write(f"{line}\n")

def ReadCSV(path: str):
    from csv import reader
    result = []
    with open(path, "r", encoding="UTF-8") as file:
        row = reader(file)
        for cells in row:
            result.append(cells)
        return result


def WriteCSV(path: str, list2D: list[list[str]]):
    from csv import writer
    with open(path, "w", encoding="UTF-8") as file:
        writer2 = writer(file, delimiter=",")
        writer2.writerows(list2D)

if __name__ == "__main__":
    main()