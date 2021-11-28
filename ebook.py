from ebooklib import epub
import json

"""
def get_file_content(path):
    with open(path,"r",encoding="utf-8") as f:
        x = f.readlines()
        b = ""
        for i in range(1,len(x)):
            b += x[i]
        return b
"""
def make_an_ebook(path,name):
    x = []
    with open("{}".format(path), "r")as f:
        book_info = json.load(f)

    book = epub.EpubBook()

    book.set_identifier('id12126')
    book.set_title(str(name))
    book.set_language('en')
    book.add_author('Mortal')

    for chapters in range(len(book_info)):
        # create chapter
        chapter = epub.EpubHtml(title="Chapter "+str(book_info[chapters]['chapterNumber']), file_name="chapter " +str(book_info[chapters]['chapterNumber']) + ".xhtml", lang='en')
        chapter.content = book_info[chapters]['content']
        chapter.id = str(book_info[chapters]['chapterNumber'])
       # print(chapter.id)
        print(chapter)
        book.add_item(chapter)
        x.append(chapter)
       # print(x)

    book.toc = (epub.Link("intro.xhtml", 'Introduction', 'intro'),
                (epub.Section(str(name)),
                 (x))
                )
    print("21")

    book.spine = x
    print("22")
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    print("23")
    epub.write_epub("{}.epub".format(name),book,{})
    print("24")

