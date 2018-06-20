import collection.crawler as cw
from bs4 import BeautifulSoup
from itertools import count

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
    for page in range(1, 2):    #count(start=1)
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



if __name__ == '__main__':
    # pelicana
    crawling_pelicana()