#! /usr/bin/python3
import pandas as pd
path = "/home/20KDL.xlsx"
# transform excel file to csv file
def user_name(path):
    data = pd.read_excel(path, engine = 'openpyxl', dtype = str)
    list_user = []
    row_number = len(data.index)
    for i in range(row_number):    
        new_user = int(data.iloc[i][0])
        list_user.append(str(new_user))
    return list_user

users = user_name(path)