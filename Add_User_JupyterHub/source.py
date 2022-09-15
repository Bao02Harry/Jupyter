#!/usr/bin/python3
import pandas as pd
path = "/home/harry/Add_User_JupyterHub/20KDL.xlsx"
def user_name(path):
    data = pd.read_excel(path, engine = 'openpyxl', dtype = str)
    list_user = []
    row_number = len(data.index)
    for i in range(row_number):    
        new_user = int(data.iloc[i][0])
        list_user.append(str(new_user) + "_")
    return list_user
def create_txt_file(List):
    with open("List_Users.txt", "a") as f:
        f.seek(0)
        f.truncate()
        for i in List:
            f.write(i + "\n")

users = user_name(path)
create_txt_file(users)