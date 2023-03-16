import requests
x=0
y=0
#Запрос на сервер
r = requests.get('http://65.108.222.51/check_material?x={x:.2f}&y={y:.2f}'.format(x=x,y=y), auth=('user', 'pass'))
r=r.text
#Обработка
if r.count("{")>0:
    ans="-"
else:
    ans=r.split('"')[1]
