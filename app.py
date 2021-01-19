import requests
from bs4 import BeautifulSoup

def digest(T) -> str:
    title = T.find('li', class_="item_deka_no content-title").text
    content = T.find('li', class_="item_short_text content-detail").text
    return '\n' + title + '\n' + content + '\n'

URL =  'https://deka.supremecourt.or.th/search'
form_data = '/show_item_remark=0&show_item_primartcourt_deka_no=0&show_item_deka_black_no=0&show_item_department=0&show_item_primarycourt=1&show_item_judge=1&show_item_source=1&show_item_long_text=0&show_item_short_text=1&show_item_law=1&show_item_litigant=1&show_result_state=1&search_form_type=basic&search_type=1&start=true&search_doctype=1&search_word=&search_deka_no_ref=&search_deka_no=&search_deka_start_year=&search_deka_end_year='
# d = {}
# for x in s.split('&'):
#     k, sep, v = x.partition('=')
#     if sep != '=':
#        raise ValueError('malformed query')
#     k = k.split('%')[0]
#     if k in d:
#        if isinstance(d[k], list): d[k].append(v)
#        else: d[k] = [d[k], v]
#     else:
#       d[k] = v
response = requests.post(URL, data = form_data)
response.encoding = 'utf-8' # for thai language readability
text = response.text
soup = BeautifulSoup(text, 'html.parser')
results = soup.find(id='deka_result_info')
result_list = results.find('ul', class_='nav-search')
result_item = result_list.find_all('li', class_='clear result')
digested = map(digest, result_item)
for item in digested:
    print(item)