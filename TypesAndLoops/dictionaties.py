# Dictionaries are key, value collections
# Similar to JSON object

dic = {
    1:0,
    2:1,
    3:2
}

print(dic)

# dic = {
#     'Name': input('Enter your name: '),
#     'Age': int(input('Enter your age: ')),
#     'Mood': input('Enter you current main emotion: ')
# }

print(dic)

print(dic.keys())

dic_sof= {
    'name':'sofia',
    'age':21,
    'favourite color':['green','purple']
}

dic_jor= {
    'name':'jorge',
    'age':21,
    'favourite color':'red'
}

json_array = [dic_sof,dic_jor]

print(json_array[1]['age'])

for key,value in dic_sof.items():
    print(f'key: {key}, value: {value}')
else:
    print('dictionary already printed')
    
    
dic_sof['Programming languages'] = ['Python','Java','C']
print(dic_sof)