def ReadText(path: str) -> list[str]:
    with open(file=path, mode="r", encoding="utf-8") as file:
        result = []
        for line in file:
            result.append(line.replace("\n", ""))
        return result

def WriteTextLines(path: str, text=""):
    with open(file=path, mode="w", encoding="utf-8") as file:
        for line in text:
            file.write(f"{line}\n")

def ReadCSV(path: str) -> list[list[str]]:
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

def ReadJSON(path: str):
    from json import load
    with open(path, 'r', encoding="utf-8") as file:
        return load(file)