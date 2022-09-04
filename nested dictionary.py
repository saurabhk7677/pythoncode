a = {'course':'python', 'fees':5000, 1:{'course':'javascript', 'fees':7000}}
# print(a)
# print(a['course'])
# print(a['fees'])
# print(a[1]['course'])
# print(a[1]['fees'])
# a['fees']=3000
# print(a)
# a[1]['course']='react'
# print(a)
# del a['fees']
# print(a)
# del a[1]['fees']
# print(a)
# a[2]={'period':'6 months', 'laptop':'lenovo'}
# print(a)
# a[1][2]={'period':'6 months', 'laptop':'lenovo'}
# print(a)
# a[3]={'month':'july', 'date':15}
# print(a)
# a[1][2][3]={'month':'july','date':15}
# print(a)




#dictionary comprehension......

dict1 = {}
for n in range(10):
    dict1[n]=n*2
print(dict1)

dict2 = {n:n*2 for n in range(10)}
print(dict2)

dict3 = {}
for n in range(10):
    if n%2==0:
        dict3[n]=n*2
print(dict3)

dict4 = {n:n*2 for n in range(10) if(n%2==0)}
print(dict4)

dict5 = {}
for n in range(10):
    if (n%2==0):
        if(n%3==0):
            dict5[n]=n*2
print(dict5)


dict6 = {n:n*2 for n in range(10) if(n%2==0) if(n%3==0)}
print(dict6)

dict7 = {}
for n in range(10):
    if (n%2==0):
        dict7[n]=n
    else:
        dict7[n]="invalid"
print(dict7)

dict8 = {n: (n if n%2==0 else "invalid") for n in range(10)}
print(dict8)
