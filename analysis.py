import pandas as pd

# pelicana
pelicana_table = pd.DataFrame.from_csv('__result__/crawling/pelicana_table.csv',
                                       encoding='utf-8',
                                       index_col=0,
                                       header=0).fillna('') # fillna(0) 비어있는 숫자들은 0으로 채우기

#  비어있는 곳은 제거(판다스 기능 제공)
pelicana_table[pelicana_table.sido != '']
pelicana_table[pelicana_table.gungu != '']
# 지역별 매장수
pelicana = pelicana_table.apply(lambda r : str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts() # axis=0은 인덱스, 1은 컬럼 기준


# nene


# kyochon


# goobne