from backyard.module import ReadJSON, ReadCSV, ReadText, WriteTextLines
from pathlib import Path

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
            print("error. either sub_jp or sub_en wasn't found.")
            exit(-1)
        try:
            subEn = ReadCSV(subEnPath.absolute())
            subJp = ReadCSV(subJpPath.absolute())
        except (UnicodeDecodeError):
            print(f"\033[33mfatal: UnicodeDecodeError at {folder.name} !\033[0m")
            exit(-1)
        if not len(ReadText(subEnPath.absolute())) == len(ReadText(subJpPath)):
            print(f"\033[31mwrong range at {folder.name}!\033[0m")
            print(f"├─ JP len {len(subJp)}")
            print(f"└─ EN len {len(subEn)}")
        discrepancy = []
        valid = True
        for lineEn in subEn:
            valid = False
            for lineJp in subJp:
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

if __name__ == "__main__":
    main()
