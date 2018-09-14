# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import xlrd


excel = pd.read_excel('top100.xlsx',sheet_name = '汇总',header=0,encoding ='utf-8')
#统计所有上榜游戏次数
game_list={}
#print(excel.info())
#print(type(excel['易观']))
#app_names =excel['易观'].values
#print(type(app_names))
#print(app_names)
# step1 频次统计

i=0
for ix, col in excel.iteritems():
    print('ix = '+str(ix))
    if ix =='排名':
        continue
    app_names = excel[ix].values

    for app_name in app_names:
        if game_list.get(app_name) is None:
            game_list[app_name] = 1
            continue
        game_list[app_name]+=1
    print(game_list)
print(len(game_list))
count_list = pd.DataFrame(game_list,index=['频次']).T
#print(count_list)
# step2 频次排序
count_list = count_list.sort_values(by='频次',ascending=False)
print(count_list)
count_list.to_excel('频次统计.xlsx',encoding='utf-8')

# step2 筛选出频次==1的
part_list = count_list[count_list['频次']==1]
part_list = part_list.T.to_dict()
for ix, col in excel.iteritems():
    print('ix = '+str(ix))
    if ix == '排名':
        continue
    for row in excel.loc[:,ix]:
        print ( 'row is %s', row)
        if not (part_list.get(row)is None):
            print (ix)
            name = row
            part_list.get(row)['频次'] = str(ix)+'_'+str(excel[excel[ix]==name]['排名'].values[0])
df_count01 = pd.DataFrame(part_list)
df_count01 =df_count01.T
df_count01.to_excel('频次为1的游戏.xls')