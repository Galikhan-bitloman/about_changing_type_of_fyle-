import json

def foo():
    with open("json_file_task_four.json") as json_file:
        data = json.load(json_file)
        data.pop("table")
        for i,j in data.items():
            print(i,": ", j)

foo()

""""
print()
op_type :  I
op_ts :  2020-11-11 21:29:16.004203
current_ts :  2020-11-11T21:29:17.336012
pos :  00000333300036553944
after :  {'ID': 296102701069, 'CLASS_ID': 'FORM_CLIENT', 'C_NUM': '209918551', 'C_DOC_DATE': '2019-12-23 12:33:48', 
'C_PARENT_FDOC': None, 'C_STATUS_DOC': 3704273, 'C_DATE_AUDIT': '2020-11-1
"""

def foo2():
    with open("json_f_t_fourdva.json") as json_file:
        data2 = json.load(json_file)
        data2.pop("table")
        for k,l in data2.items():
            print(k,": ", l)

foo2()
"""
print()
op_type :  D
op_ts :  2020-11-10 11:15:32.006560
current_ts :  2020-11-10T11:15:33.127015
pos :  00000330990105307403
before :  {'ID': 295847056205}
"""

def foo3():
    with open("json_f_t_fourtri.json") as json_file:
        data3 = json.load(json_file)
        data3.pop("table")
        for p,m in data3.items():
            print(p,": ", m)

foo3()

"""
print()
op_type :  U
op_ts :  2020-11-10 15:48:37.002705
current_ts :  2020-11-10T15:48:38.621015
pos :  00000331310397552705
before :  {}
after :  {'ID': 262769361334, 'C_TYPE_INFO': 8822633, 'C_SUMMA': None, 'COLLECTION_ID': 262769361326, 
'C_CURR': 3684609, 'SN': 1, 'SU': 1600672298}

"""