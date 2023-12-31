def main():
    hoge = ["test_1", "test_0", "test_3", "test_2", "hoge_0"]
    name = ""
    i = 0
    while i < len(hoge):
        line = hoge[i]
        line_name = hoge[i].split(sep="_")[0]
        if name != line_name:
            name = line_name
            o = 0
            group = [[linetmp.split(sep="_")[0], linetmp.split(sep="_")[1]] for linetmp in hoge if linetmp.split(sep="_")[0] == name]
            print(f"group: {group}")
            sort2D(group)
        i += 1

def sort2D(group : list[list[str]]):
    result = []
    for i in range(len(group)):
        result.append([test for test in group if int(test[1]) == i])
    print(f"result: {result}")

if __name__ =="__main__":
    main()