import requests
from lxml import html
import json

orixa_tit = ''
orixa_img = ''
orixa_dia = ''
orixa_cor = ''
orixa_symbols = ''
orixa_element = ''
orixa_dominance = ''
orixa_salute = ''

url = 'https://ocandomble.com/os-orixas/nana/'

response = requests.get(url)
webpage = response.content

tree = html.fromstring(webpage)

xpath_day = '//*[@id="post-20"]/div[2]/p[3]'
xpath_color = '//*[@id="post-20"]/div[2]/p[4]'
xpath_symbols = '//*[@id="post-20"]/div[2]/p[5]'
xpath_element = '//*[@id="post-20"]/div[2]/p[6]'
xpath_dominance = '//*[@id="post-20"]/div[2]/p[7]'
xpath_salute = '//*[@id="post-20"]/div[2]/p[8]'
xpath_salutes = '//*[@id="post-20"]/div[2]/p[8]'
xpath_title = '//*[@id="post-20"]/div[1]/h2/a'
xpath_img = '//*[@id="post-20"]/div[2]/p[2]/strong/span/a/img'

data = tree.xpath(xpath_title)
for title in data:
    orixa_tit = title.text_content()
    print(orixa_tit)

data = tree.xpath(xpath_img + '/@src')
for img in data:
    orixa_img = img
    print(orixa_img)

data = tree.xpath(xpath_day)
for dia in data:
    orixa_dia = dia.text_content()
    print(orixa_dia)

data = tree.xpath(xpath_color)
for color in data:
    orixa_cor = color.text_content()
    print(orixa_cor)

data = tree.xpath(xpath_symbols)
for symbols in data:
    orixa_symbols = symbols.text_content()
    print(orixa_symbols)

data = tree.xpath(xpath_element)
for element in data:
    orixa_element = element.text_content()
    print(orixa_element)

data = tree.xpath(xpath_dominance)
for dominance in data:
    orixa_dominance = dominance.text_content()
    print(orixa_dominance)

data = tree.xpath(xpath_salutes)
for salute in data:
    orixa_salute = salute.text_content()
    print(orixa_salute)

orixa_info = {
    "título": orixa_tit.strip(),
    "imagem": orixa_img.strip(),
    "dia": orixa_dia.strip(),
    "cor": orixa_cor.strip(),
    "símbolos": orixa_symbols.strip(),
    "elemento": orixa_element.strip(),
    "domínio": orixa_dominance.strip(),
    "saudações": orixa_salute.strip()
}

with open('orixa_info.json', 'w', encoding='utf-8') as f:
    json.dump(orixa_info, f, ensure_ascii=False, indent=4)
