import pandas as pd
import matplotlib.pyplot as plt

# pelicana
pelicana_table = pd.DataFrame.from_csv('__result__/crawling/pelicana_table.csv', encoding='utf-8', index_col=0, header=0).fillna('')

# 비어 있는곳은 제거
pelicana_table = pelicana_table[pelicana_table.sido != '']
pelicana_table = pelicana_table[pelicana_table.gungu != '']

# 'sido gungu' 별 매장수
pelicana = pelicana_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts()
# print(pelicana)


# nene
nene_table = pd.DataFrame.from_csv('__result__/crawling/nene_table.csv',
                                       encoding='utf-8',
                                       index_col=0,
                                       header=0).fillna('') # fillna(0) 비어있는 숫자들은 0으로 채우기

#  비어있는 곳은 제거(판다스 기능 제공)
nene_table = nene_table[nene_table.sido != '']
nene_table = nene_table[nene_table.gungu != '']
# 지역별 매장수
nene = nene_table.apply(lambda r : str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts() # axis=0은 인덱스, 1은 컬럼 기준
# print(nene)


# kyochon
kyochon_table = pd.DataFrame.from_csv('__result__/crawling/kyochon_table.csv',
                                       encoding='utf-8',
                                       index_col=0,
                                       header=0).fillna('') # fillna(0) 비어있는 숫자들은 0으로 채우기

#  비어있는 곳은 제거(판다스 기능 제공)
kyochon_table = kyochon_table[kyochon_table.sido != '']
kyochon_table = kyochon_table[kyochon_table.gungu != '']
# 지역별 매장수
kyochon = kyochon_table.apply(lambda r : str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts() # axis=0은 인덱스, 1은 컬럼 기준
# print(kyochon)


# goobne
goobne_table = pd.DataFrame.from_csv('__result__/crawling/goobne_table.csv', encoding='utf-8', index_col=0, header=0).fillna('')

# 비어 있는곳은 제거
goobne_table = goobne_table[goobne_table.sido != '']
goobne_table = goobne_table[goobne_table.gungu != '']

# 'sido gungu' 별 매장수
goobne = goobne_table.apply(lambda r: str(r['sido']) + ' ' + str(r['gungu']), axis=1).value_counts()
# print(goobne)


chicken_table = pd.DataFrame({'pelicana' : pelicana, 'nene' : nene, 'kyochon' : kyochon, 'goobne' : goobne})
chicken_table = chicken_table.drop(chicken_table[chicken_table.index == '00 18'].index)
chicken_table = chicken_table.drop(chicken_table[chicken_table.index == '테스트 테스트구'].index)

chicken_sum_table = chicken_table.sum(axis=0)

plt.figure()
chicken_sum_table.plot(kind='bar')
plt.show()