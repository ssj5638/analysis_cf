import collection.crawler as cw
import pandas as pd
import urllib
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup
from itertools import count
from collection.data_dict import sido_dict, gungu_dict

RESULT_DIRECTORY = '__result__/crawling'

# def proc(html):
#     print("processing..." + html)
#
#
# def store(result):
#     pass
# cw.crawling(
#     url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
#     encoding='cp949')
    # proc=proc,
    # store=store)

def crawling_pelicana():
    results = []
    for page in count(start=1):    # range(1, 3)
        url = 'http://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=&page=%d' % page
        html = cw.crawling(url=url)

        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_table = tag_table.find('tbody')
        tags_tr = tag_table.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break
        # print(page, len(tags_tr), sep=':')

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            results.append( (name,address) + tuple(sidogu))
    print(results)

    #store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gungu'])
    table.to_csv('{0}/pelicana_table.csv'.format(RESULT_DIRECTORY),
                 encoding='utf-8',
                 mode='w',
                 index=True)

    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))


def proc_nene(xml):
    root = et.fromstring(xml)
    results = []
    # elements_item = root.findall('item')
    for el in root.findall('item'):
        name= el.findtext('aname1')
        sido= el.findtext('aname2')
        gungu= el.findtext('aname3')
        address= el.findtext('aname5')

        results.append((name, address, sido, gungu))

    return results



def store_nene(data):
    table = pd.DataFrame(data, columns=['name', 'address', 'sido', 'gungu'])
    table.to_csv('{0}/nene_table.csv'.format(RESULT_DIRECTORY),
                 encoding='utf-8',
                 mode='w',
                 index=True)

    table['sido'] = table.sido.apply(lambda v: sido_dict.get(v, v))
    table['gungu'] = table.gungu.apply(lambda v: gungu_dict.get(v, v))

if __name__ == '__main__':
    # pelicana
    crawling_pelicana()

    # nene
    cw.crawling(
        url='http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s '
            % (urllib.parse.quote('전체'), urllib.parse.quote('전체')),
        proc=proc_nene,
        store=store_nene)