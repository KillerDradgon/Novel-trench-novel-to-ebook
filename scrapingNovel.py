import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

#class="wp-manga-chapter    "

def scrape_latest_chapter_number(url):
    session = HTMLSession()
    r = session.get(url)
    r.html.render(timeout=20)
    x = r.html.absolute_links
    lt = []
    for i in x:
        if "the-runesmith/chapter" in i:

            print(i)
            q = i.split("chapter-")[1].replace("/", "")
            lt.append(int(q))
    lt.sort(reverse=True)

    #soup = BeautifulSoup(r.content, "html.parser")
    #link = soup.find('ul', attrs={"class":"main version-chap no-volumn active"})
    #print(link)

    return lt[0]



def scrape_chapter(url , headers_dict):
    rs = requests.session()
    page = rs.get(url, headers=headers_dict)
    soup = BeautifulSoup(page.content, "html.parser")
    link = soup.find('div', attrs={"class": "text-left"})
    rs.close()
    if link != None:
        chap = link.contents
        return chap
    else:
        print("NO CHAPTER")
        return None
