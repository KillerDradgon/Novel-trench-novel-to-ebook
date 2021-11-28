import json


def save_info_json(list,name):
    with open(name,"w") as f:
        json.dump(list,f)

def save_chapter_as_json(chapter,number):
    if chapter:
        path = "./chapterJ1/only i am a necromancer 26.json".format(number)
        with open("./chapterJ1/only i am a necromancer 26.json".format(number),"a") as f:
            s = ""
            for i in range(1,len(chapter)):
                s += str(chapter[i])
            json.dump({"chapterNumber":number,"content":s},f)
            f.write(',')
        return path
    else:
        print("CHAPTER NOT AVAILABLE")



def save_chapter(chapter,number):
    path = "./chapterJ2/only i am a necromancer {}.txt".format(number)
    with open("./chapterJ2/only i am a necromancer {}.txt".format(number),"a",encoding="utf-8") as f:

        if chapter:
            s = ""
            for i in range(1,len(chapter)):
                print(chapter[i])
                s += str(chapter[i])
            f.writelines(s)
        else:
            print("CHAPTER NOT AVAILABLE")

    return path

