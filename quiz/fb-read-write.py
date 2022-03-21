import os # operating system

# 讀取檔案
def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())
        return lines
# 轉換檔案
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == "Calvin":
            person = "Calvin"
            continue
        elif line == "Eddie":
            person = "Eddie"
            continue
        if person:
            new.append(person + ": " + line)
    return new


# 寫入檔案
def write_file(filename, lines):
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    filename = "input.txt"
    if os.path.isfile(filename): # 檢查檔案在不在
        lines =  read_file(filename)
        print("yeah! 找到檔案了")
    else:
        print("找不到檔案...")
    lines = convert(lines)
    write_file("output.txt", lines)

main()