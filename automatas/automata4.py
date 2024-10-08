from pathlib import Path

# VOの各フォルダの、sub_ja.csvをsub_jp.csvにリネームします
# Home invasionリリースにより字幕が表示されなくなった問題に対処します
# ReadyOrNot/Contents/ ディレクトリの中に配置して実行してください

def main():
    VO = Path("./VO")
    if not VO.exists():
        print("VO folder wasn't found!\nmake sure to run this in correct directory")
        exit()
    folders = [folder for folder in VO.iterdir() if folder.is_dir()]
    for folder in folders:
        for file in folder.iterdir():
            if file.name == "sub_ja.csv":
                file.rename(f"{folder}/sub_jp.csv")
                print("changed in " + folder.name)
    print("done!")

if __name__ == "__main__":
    main()