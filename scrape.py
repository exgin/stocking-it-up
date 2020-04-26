from bs4 import BeautifulSoup, NavigableString, Tag
import requests

ticker = 'FB'

src = requests.get(f'https://finviz.com/quote.ashx?t={ticker}').text
soup = BeautifulSoup(src, 'lxml')

stock_table = soup.find('table', class_='snapshot-table2').find_all('td')

data = []

names_list = []
def get_names():
    """Get all of the categories of the stock fundamentals"""
    for rows in stock_table[::2]:
        names = rows.text
        names_list.append(names)
    return names_list

vals_list = []
def get_names_values():
    """Get all of the stock's data for its fundamental"""
    for rows in stock_table[1::2]:
        vals = rows.text
        vals_list.append(vals)
    return vals_list


def combine(l1, l2):
    """Combine both togther with a tuple for easy to read/understand"""
    data = [(l1[i], l2[i]) for i in range(0, len(l1))]
    return data

combine(names_list, vals_list)
