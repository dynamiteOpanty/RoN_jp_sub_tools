from pathlib import Path

# VOの各フォルダの、sub_enの順番をソートするpythonプログラムです
# ソートはsub_en内の各接頭辞単位で行われます
# 使用しません　depricated　個人的な記録として残します

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
    folders = [folder for folder in VO.iterdir() if folder.is_dir()][0:5]
    for folder in folders:
        if folder.name in excludes or folder.name in noSub:
            continue
        for file in folder.iterdir():
            if file.name != "sub_en.csv":
                continue
            subEn = ReadCSV(file)
            subEnContent = subEn[1:]
            result = []
            name = ""
            i = 0
            while i < len(subEnContent[0:5]):
                line = subEnContent[i]
                line_name = line[0].split("_")[0]
                if name != line_name:
                    pass
                i += 1
            # WriteCSV(f"{folder}/test.csv", result)
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