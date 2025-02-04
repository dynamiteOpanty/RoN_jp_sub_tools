from backyard.module import ReadJSON, ReadCSV, ReadText, WriteTextLines
from pathlib import Path

# sub_en、sub_jp間の齟齬を検出しリストアップします
# sub_enとsub_jpの行数の齟齬、sub_enにあるがsub_jpに無いKeyが対象です
# 出力結果はコンソールに表示されます

config = ReadJSON("./automatas/backyard/config.json")
EXCLUDES_PATH = f"./automatas/backyard/{config['excludeFileName']}.txt"
NOSUB_LIST = f"./automatas/backyard/{config['noSubList']}.txt"


def main():
    VO = Path("./VO")
    try:
        excludes = ReadText(EXCLUDES_PATH)
    except:
        WriteTextLines(EXCLUDES_PATH)
        excludes = ""
    try:
        noSub = ReadText(NOSUB_LIST)
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
            print(f"error. either sub_jp or sub_en at {folder.name} wasn't found.")
            continue
        try:
            subEnCsv = ReadCSV(subEnPath.absolute())
            subJpCsv = ReadCSV(subJpPath.absolute())
        except (UnicodeDecodeError):
            print(f"\033[33mfatal: UnicodeDecodeError at {folder.name} !\033[0m")
            continue
        subEnText = ReadText(subEnPath.absolute())
        subJpText = ReadText(subJpPath.absolute())
        if not len(subEnText) == len(subJpText):
            print(f"\033[31mwrong range at {folder.name}!\033[0m")
            print(f"├─ JP len {len(subEnText)}")
            print(f"└─ EN len {len(subJpText)}")
        discrepancy = []
        valid = True
        for lineEn in subEnCsv[1:]:
            valid = False
            for lineJp in subJpCsv:
                if lineEn[0] == lineJp[0]:
                    valid = True
            if valid:
                continue
            discrepancy.append(lineEn[0])
        if 0 < len(discrepancy):
            print(f"\033[33mdiscrepancy at {folder.name}!\033[0m")
            for line in discrepancy:
                if line == discrepancy[-1]:
                    prefix = "└─"
                else:
                    prefix = "├─"
                print(f"{prefix} {line}")
            # print(f"└─ {len(discrepancy)}")
    print("done!")

if __name__ == "__main__":
    main()
