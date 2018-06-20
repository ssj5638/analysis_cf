from bs4 import BeautifulSoup


html ='<td class="title"><div class="tit3">' \
      '<a href="/movie/bi/mi/basic.nhn?code=154285" ' \
      'title="쥬라기 월드: 폴른 킹덤">쥬라기 월드: 폴른 킹덤</a></div></td>'

# 1. tag 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs)

    tag = bs.td
    print(tag)

    tag = bs.a          # 앵커태그 <a> ~</a>
    print(tag)
    print(tag.name)

    tag = bs.td         # td태그 밑의 div태그
    print(tag.div)


# 2. attributes 값
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])

    tag = bs.div
    # 에러 id가 없어서 오류
    # print(tag['id'])
    print(tag.attrs)


# 3. attributes 조회
def ex3():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.find('td', attrs={'class':'title'})
    print(tag)

    tag = bs.find(attrs={'class':'tit3'})
    print(tag)


if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()