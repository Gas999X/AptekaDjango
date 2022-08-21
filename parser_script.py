import re
import requests
from bs4 import BeautifulSoup as BS


# https://www.lsgeotar.ru/abc-pharma_tn/pg_00001.html
# https://www.lsgeotar.ru/abc-pharma_tn/pg_00143.html
# https://www.lsgeotar.ru/abc-pharma_tn/pg_00031.html


def get_parsing_lsgeotar():  # функция парсинга
    # определяем списки эллементов парсинга: имя, ссылка, пояснение
    # получает (Я-А)
    list_med_name = []
    list_med_href = []
    list_med_text = []

    url = 'https://www.lsgeotar.ru/abc-pharma_tn/pg_00143.html'

    while True:
        try:
            r = requests.get(url, verify=False)
            soup = BS(r.content, "lxml")
            elem = soup.find_all(class_="abc_aprior")
            elem1 = soup.find_all(class_="title-tn-link")
            elem2 = soup.find_all(class_="wrap-forma-vipuska")

            for i in elem:
                href = i['href']
            print(url, ": Страница")
            print("v" * len(url))
            url = href

            if len(elem1):
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
        except requests.ConnectionError as e:
            print(e)
            break
    # разворачиваем списки А-Я
    list_med_nameREVERCE = list_med_name[::-1]
    list_med_hrefREVERCE = list_med_href[::-1]
    list_med_textREVERCE = list_med_text[::-1]

    return list_med_nameREVERCE, list_med_hrefREVERCE, list_med_textREVERCE

