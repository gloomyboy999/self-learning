def read_file(filename):
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line.strip())
        return lines

def convert(lines):
    new = []
    person = None
    calvin_word_count = 0
    justina_word_count = 0
    calvin_sticker_count = 0
    justina_sticker_count = 0
    calvin_image_count = 0
    justina_image_count = 0
    for line in lines:
        s = line.split(" ")
        time = s[0]
        name = s[1]
        if name == "Calvin":
            if s[2] == "貼圖":
                calvin_sticker_count += 1
            elif s[2] == "圖片":
                calvin_image_count += 1
            else:
                for m in s[2:]:
                    calvin_word_count += len(m)
        elif name == "Justina":
            if s[2] == "貼圖":
                justina_sticker_count += 1
            elif s[2] == "圖片":
                justina_image_count += 1
            else:
                for m in s[2:]:
                    justina_word_count += len(m)
            
    print("Calvin 說了", calvin_word_count, "個字")
    print("Calvin 傳了", calvin_sticker_count, "個貼圖")
    print("Calvin 傳了", calvin_image_count, "個圖片")
    print("Justina 說了", justina_word_count, "個字")
    print("Justina 傳了", justina_sticker_count, "個貼圖")
    print("Justina 傳了", justina_image_count, "個圖片")

def write_file(filename, lines):
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

def main():
    lines =  read_file("[Line]Justina.txt")
    lines = convert(lines)
    # write_file("output.txt", lines)

main()