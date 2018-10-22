#-*- coding:utf-8 -*-
import datetime
from openpyxl import load_wordbook
from openpyxl import Workbook

wk = load_wordbook('courses.xlsx')
student_sheet = wk['student']
time_sheet = wk['time']

def combine():
    combine_sheet = wk.create_sheet(title="combine")
    combine_sheet.append('CreateTime','CourseName','StudentNum','StudyTime')
    for stu in student_sheet.values:
        if stu[2]!= "学习人数":
            for time in time_sheet.values:
                if time[1]== stu[1]:
                    combine_sheet.append(list(stu)+ [time[2]])
    wk.save('course.xlsx')
def split():
    combine_sheet = wk['combine']
    split_name = []
    for item  in combine_sheet.values:
        if item[0] != "CreatTime":
            split_name.append(tiem[0].strftime('%Y'))
   
    for name in set(split_name):
        wk_temp = Workbook()
        wk_temp.remove(wk_temp.active)
        ws = wk.create_sheet(title="name")
        for item_by_year in combine_sheet.values:
            if item_by_year[0] != "CreateTime":
                if item_by_year[0].strftime('%Y') == name :
                    ws.append(item_by_year)

        wk_temp.save('{}.xlsx'.format(name))
if __name__ == "__main__":
    combine()
    split()
    
        


