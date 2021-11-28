
import scrapingNovel
import saveFile
import time
import os
import ebook
book = []


#test_url = "https://noveltrench.com/manga/only-i-am-a-necromancer/chapter-{}/".format(3)
#scrapingNovel.scrape_chapter(test_url, headers_dict)

def get_novel_name(url):
    novel_name = url.split("noveltrench.com/")[1].split("/")[1]
    return novel_name

headers_dict = {"Connection":"keep-alive","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}
test_url2 = "https://noveltrench.com/manga/the-runesmith/"


#latest_chapter = scrapingNovel.scrape_latest_chapter_number(test_url2)
novel_name = get_novel_name(test_url2)
path_to_novel = "./"+str(novel_name)
if os.path.isdir(path_to_novel) == False:
    os.mkdir(path_to_novel)

for x in range(1,scrapingNovel.scrape_latest_chapter_number(test_url2)+1):
    test_url = "https://noveltrench.com/manga/the-runesmith/chapter-{}/".format(x)
    chapter = scrapingNovel.scrape_chapter(test_url, headers_dict)
    if chapter == None:
        continue
    s = ""
    for i in range(1, len(chapter)):
        s += str(chapter[i])
    print(x)
    book.append({"chapterNumber":int(x),"content":s})
    time.sleep(0.09)

saveFile.save_info_json(book,path_to_novel+"/{}.json".format(novel_name))
ebook.make_an_ebook("{}/{}.json".format(path_to_novel,novel_name),novel_name)








