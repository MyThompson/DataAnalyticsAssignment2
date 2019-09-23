import xlrd
import json

# excel = xlrd.open_workbook("resources/Project2DataTrimmed.xlsx")
# sheet = excel.sheet_by_index(0)

# data={}
# temp={}
# data['data'] = []
# for i in range(0,sheet.nrows):
#     for j in range(0,sheet.ncols):
#         # print (sheet.cell(i,j).value)
#         temp['{}'.format(sheet.cell(0,j).value)]=sheet.cell(i,j).value

#     if i > 0 :
#         tempList = [(k,v) for k,v in temp.items()]
#         data['data']=data['data']+tempList
# print (data['data'])


keylist = []
temp={}
data={}
data['data']=[]

file = open("resources/Project2DataTrimmed.csv", "r")
for x in file.readline().split(","):
    keylist.append(x)

for lines in file:
    array = lines.split(",")
    for i in range(len(keylist)):
        temp['{}'.format(keylist[i])]=array[i]
        

    tempList = [(k,v) for k,v in temp.items()]
    data['data']=data['data']+tempList
print(data['data'])

print(json.dumps(data))
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

