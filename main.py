import re
import requests
from bs4 import BeautifulSoup as BS

list_med_name = []
list_med_href = []
list_med_text = []


# https://www.lsgeotar.ru/abc-pharma_tn/pg_00001.html
# https://www.lsgeotar.ru/abc-pharma_tn/pg_00031.html
def get_parsing_lsgeotar():
    url = 'https://www.lsgeotar.ru/abc-pharma_tn/pg_00031.html'
    while True:

        r = requests.get(url, verify=False)
        soup = BS(r.content, "lxml")
        elem = soup.find_all(class_="abc_aprior")
        elem1 = soup.find_all(class_="title-tn-link")
        elem2 = soup.find_all(class_="wrap-forma-vipuska")

        for i in elem:
            href = i['href']
        print(url)
        url = href

        if (len(elem1)):
            for i in elem1:
                href = i['href']
                name = i.text
                name = re.sub('[!@#$®\n]', '', name)
                list_med_name.append(name)
                list_med_href.append(href)
                print(name)
            for i in elem2:
                text = i.text
                list_med_text.append(text)
        else:
            break

get_parsing_lsgeotar()


def attach_list_parsing():
    for i in range(len(list_med_name)):
        name = list_med_name[i]
        href = list_med_href[i]
        text = list_med_text[i]
        print()
        print(f"{name} \n {href}\n {text}")


attach_list_parsing()
