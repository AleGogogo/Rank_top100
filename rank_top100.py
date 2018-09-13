import pandas as pd
import numpy as np
import xlrd


excel = pd.read_excel('top100.xlsx',sheet_name = '汇总',header=0,encoding ='utf-8')
#统计所有上榜游戏次数
game_list={}
excel = excel.drop(['排名'],axis=1)
#print(excel.info())
#print(type(excel['易观']))
#app_names =excel['易观'].values
#print(type(app_names))
#print(app_names)
#以易观数据为基准统计
"""for app_name in app_names:
    count_game[app_name] =1"""

"""data_1=np.zeros((2,n+1))
data_1=pd.DataFrame(data_1)
test=pd.DataFrame(columns=id_column)
a=test.append(data_1，columns=id_column"""
i=0
for ix, col in excel.iteritems():
    print('ix = '+str(ix))
    app_names = excel[ix].values

    for app_name in app_names:
        if game_list.get(app_name) is None:
            game_list[app_name] = 1
            continue
        game_list[app_name]+=1
    print(game_list)
print(len(game_list))
count_list = pd.DataFrame(game_list)
print(count_list)
#count_list.to_excel("游戏频次统计")