import collection.crawler as cw


# def proc(html):
#     print("processing..." + html)
#
#
# def store(result):
#     pass


result = cw.crawling(
    url='http://movie.naver.com/movie/sdb/rank/rmovie.nhn',
    encoding='cp949')
    # proc=proc,
    # store=store)