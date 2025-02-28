d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
b = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

dicto = {'Geeks':1,'for':2,'geeks':3}
print(dicto.get('for'))
dicto["Good"]= 4
for key,values in dicto.items():
    print(key,values)
print(dicto.values())
list1 = [1,2,3,4,5]

def square(n):
    return n**2
res = list(map(square,list1))
print(res)