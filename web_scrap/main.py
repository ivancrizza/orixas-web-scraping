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


def extract_text(tree_html, xpath):
    data = tree_html.xpath(xpath)
    return data[0].text_content().strip() if data else None


def extract_attribute(tree_html, xpath, attribute):
    data = tree_html.xpath(xpath + '/@' + attribute)
    return data[0] if data else None


url = 'https://ocandomble.com/os-orixas/iroko/'

response = requests.get(url)
webpage = response.content

tree = html.fromstring(webpage)
xpaths = {
    "title": '//*[@id="post-263"]/div[1]/h2/a',
    "img": '//*[@id="post-263"]/div[2]/p[1]/strong/a/img',
    "day": '//*[@id="post-263"]/div[2]/p[2]',
    "color": '//*[@id="post-263"]/div[2]/p[3]',
    "symbols": '//*[@id="post-263"]/div[2]/p[4]',
    "element": '//*[@id="post-263"]/div[2]/p[4]',
    "dominance": '//*[@id="post-263"]/div[2]/p[6]',
    "salutes": '//*[@id="post-263"]/div[2]/p[7]'
}

# IANSA PRECISA FAZER NA MAO
# nana_xpaths = {
#     "title": '//*[@id="post-20"]/div[1]/h2/a',
#     "img": '//*[@id="post-20"]/div[2]/p[2]/strong/span/a/img',
#     "day": '//*[@id="post-20"]/div[2]/p[3]',
#     "color": '//*[@id="post-20"]/div[2]/p[4]',
#     "symbols": '//*[@id="post-20"]/div[2]/p[5]',
#     "element": '//*[@id="post-20"]/div[2]/p[6]',
#     "dominance": '//*[@id="post-20"]/div[2]/p[7]',
#     "salutes": '//*[@id="post-20"]/div[2]/p[8]'
# }
orixa_info_iroko = {
    "título": extract_text(tree, xpaths["title"]),
    "imagem": extract_attribute(tree, xpaths["img"], "src"),
    "dia": extract_text(tree, xpaths["day"]),
    "cor": extract_text(tree, xpaths["color"]),
    "símbolos": extract_text(tree, xpaths["symbols"]),
    "elemento": extract_text(tree, xpaths["element"]),
    "domínio": extract_text(tree, xpaths["dominance"]),
    "saudações": extract_text(tree, xpaths["salutes"])
}
# print(extract_text(tree, xpaths["title"]))
# print(extract_attribute(tree, xpaths["img"], "src"))
# print(extract_text(tree, xpaths["day"]))
# print(extract_text(tree, xpaths["color"]))
# print(extract_text(tree, xpaths["symbols"]))
# print(extract_text(tree, xpaths["element"]))
# print(extract_text(tree, xpaths["dominance"]))
# print(extract_text(tree, xpaths["salutes"]))

with open('orixa_info_iroko.json', 'w', encoding='utf-8') as f:
    json.dump(orixa_info_iroko, f, ensure_ascii=False, indent=4)
