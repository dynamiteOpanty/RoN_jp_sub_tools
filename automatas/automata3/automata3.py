from pathlib import Path

# VOの各フォルダの、sub_enの順番をソートするpythonプログラムです
# ソートはsub_en内の各接頭辞単位で行われます
# 使用しません　depricated　個人的な記録として残します

dir = "./automata/"
excludesname = "excludes"
noSubname = "no_JP_sub_list"
excludespath = f"{dir}/{excludesname}.txt"
noSubList = f"{dir}/{noSubname}.txt"
outputFileName = "sub_en_sorted.csv"

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
        print(folder.name)
        for file in folder.iterdir():
            if file.name != "sub_en.csv":
                continue
            subEn = ReadCSV(file)
            subEnContent = subEn[1:]
            group_prefix = ""
            groups = []
            i = 0
            result = []
            while i < len(subEnContent):
                first_line = subEnContent[i]
                line_prefix = first_line[0].split("_")[0]
                if group_prefix != line_prefix:
                    group_prefix = line_prefix
                    groups.append(group_prefix)
                i += 1
            for prefix in groups:
                group = []
                for record in subEnContent:
                    if record[0].split("_")[0] == prefix:
                        group.append(record)
                try:
                    group2 = [[record, int(record[0].split("_")[-1])] for record in group]
                except:
                    print(f"an error occured in {folder.name}, {prefix}")
                    exit(-1)
                group3 = [record[0] for record in sort2D(group2)]
                result += group3
            result.insert(0, ["Key", "Dialogue", "Context"])
            WriteCSV(f"{folder}/{outputFileName}", result)
    print("done")

def sort2D(group: list):
    result = []
    for i in range(len(group)):
        result += [line for line in group if line[1] == i]
    return result

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
    # main()
    pass