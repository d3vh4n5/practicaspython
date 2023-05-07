import datetime
'''
mi_dia=datetime.date.today()
print(mi_dia)
proxSemana=mi_dia+datetime.timedelta(days=7)
print(proxSemana)


t1=datetime.time(12,55,0)
t2=datetime.time(13,5,9)
print('t1<t2', t1<t2)
'''
'''
print('Ahora: ', datetime.date.today())
campos=['year', 'month', 'day']
print(campos)

d=datetime.date.today()
for att in campos:
    print(att,getattr(d, att))

t=datetime.time(12,5,0)
d=datetime.date.today()
dt=datetime.datetime.combine(d,t)
print('dt: ', dt)


dt=datetime.datetime.now()
print('Firmato ISO: ', dt)
latam=dt.strftime('%d/%m/%Y')
print('Formato Latam: ', latam)
print('format(): {:%d/%m/%Y}'.format(dt))
print('format(): {:%d %m %Y %H:%M}'.format(dt))
'''

#aca empezamos con VSC y BBDD

