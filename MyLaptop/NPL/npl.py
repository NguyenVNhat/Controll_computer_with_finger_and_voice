import pandas as pd
import json

def getData():
    data = pd.read_csv('NPL/data.csv', encoding='utf-8')
    data.fillna('', inplace=True)

    with open('NPL/dct.json', encoding='utf-8') as file:
        datajson = json.load(file)
    dct = {}
    for key,value in datajson.items():
        dct[key] = value
    return data,dct

def transformer(string):
    data,dct = getData()

    for key,value in dct.items():
        string = string.replace(key,value)

    ans = {'DanhTu':'','Ydinh':'','DongTu':'','ChuThe':'','LoaiChuThe':'','Url':'','Value':'','DongTu2':'','LoaiDongTu2':'','UrlFind':''}
    words = string.split()
    for item in words:
        for column in data.columns:
            if  item.isdigit():
                ans['Value'] = item
            if item in data[column].values:
                ans[column] = item
    index_of_row = data[data['ChuThe'] == ans['ChuThe']].index[0]
    index_of_folder = data[data['DongTu2'] == ans['DongTu2']].index[0]

    loai_chu_the_value = data.loc[index_of_row, 'LoaiChuThe']
    ans['LoaiChuThe'] = loai_chu_the_value

    url_value = data.loc[index_of_row, 'Url']
    ans['Url'] = url_value

    urlfind_value = data.loc[index_of_row, 'UrlFind']
    ans['UrlFind'] = urlfind_value

    LoaiDongTu2 = data.loc[index_of_folder, 'LoaiDongTu2']
    ans['LoaiDongTu2'] = LoaiDongTu2

    return ans,string

