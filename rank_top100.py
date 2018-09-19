# -*- coding: utf-8 -*
import pandas as pd
import numpy as np
import xlrd
import decimal

excel = pd.read_excel('top100.xlsx',sheet_name = '汇总',header=0,encoding ='utf-8')
#统计所有上榜游戏次数
game_list={}
#print(excel.info())
#print(type(excel['易观']))
#app_names =excel['易观'].values
#print(type(app_names))
#print(app_names)
# step1 频次统计

import re
excel = pd.read_excel('top100.xlsx',sheet_name = '汇总',header=0,encoding ='utf-8')
#统计所有上榜游戏次数
game_list={}
i=0
for ix, col in excel.iteritems():
    print('ix = '+str(ix))
    if ix == '排名':
        continue
    app_names = excel[ix].values
    for app_name in app_names:
        key =""
        pattern = re.compile(u'[\u4e00-\u9fa5]+\d*|[a-zA-Z]+')
        c_name= re.findall(pattern,str(app_name))
        for name in c_name:
            key +=str(name)
        if game_list.get(key) is None:
            game_list[key] = 1
            continue
        game_list[key]+=1
count_list = pd.DataFrame(game_list,index=['频次']).T
count_list = count_list.sort_values(by='频次',ascending=False)
#print(count_list)
# step2 频次排序
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
        if not (part_list['频次'].get(row)is None):
            print (ix)
            name = row
            part_list['频次'][row] = str(ix)+'_'+str(excel[excel[ix]==name]['排名'].values[0])
df_count01 = pd.DataFrame(part_list)
df_count01 =df_count01.T
df_count01.to_excel('频次为1的游戏.xls')
#计算前75个的排名
#sep3=======重现初始化一遍dict
top_81 = {}
part_list = count_list[count_list['频次']>1]
part_list = part_list.T.to_dict()
for (key,values )in part_list['频次'].items():
    top_81[key]=[]
for ix, col in excel.iteritems():
    print('ix = ' + str(ix))
    if ix == '排名':
        continue
    if ix == '易观':
        k = 0.3
    if ix == 'talkingdata':
        k = 0.4
    if ix == '应用宝(N0.1)':
        k = 0.1
    if ix == '360市场(N0.2)':
        k = 0.1
    if ix == '百度(N0.3)':
        k = 0.1

    for row in excel.loc[:, ix]:
        if row is np.nan:
            continue
        key = ""
        pattern = re.compile(u'[\u4e00-\u9fa5]+\d*|[a-zA-Z]+')
        c_name = re.findall(pattern, str(row))
        for name in c_name:
            key += str(name)
        print(key)
        rank = 0
        if not (part_list['频次'].get(key) is None):
            rank = (excel[excel[ix] == row]['排名'].values[0]) * k
            ctx = decimal.Context()
            rank = ctx.create_decimal(repr(rank))
            top_81.get(key).append(str(rank))

#排名取平均
pre ={}
pre = top_81
for key in pre.keys():
    rank =0
    n=0
    values = pre[key]
    for value in values:
        n +=1
        rank +=int(value)
        print('rank is %f',rank)
        pre[key]= rank/n
top_pre = pd.DataFrame(pre, index=['排名'])
top_pre=top_pre.T
top_pre.to_excel('top81.xls')

#step4====处理后25个，以易观为基准
yiguan_list = {}
for row in excel.loc[:,'易观']:
    print ( 'row is %s', row)
    if not (part_list['频次'].get(row)is None):
        name = row
        print ( 'row is'+ str(row))
        yiguan_list[row]=excel[excel['易观']==name]['排名'].values[0]
yiguan_list = pd.DataFrame(yiguan_list,index=['排名'])
yiguan_list=yiguan_list.T
yiguan_list.to_excel('top_to100.xls')