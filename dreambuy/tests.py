import datetime
def prdtcode():
    import datetime
    nums =[1,2,3,4,5,6,7,8,9,0]
    alphs = ['a','b','c','d','e','f','g','h','i','j']
    now = datetime.datetime.now()
    datestr = str(now.year)
    if now.month < 10:
        datestr += '0'
    datestr += str(now.month)
    if now.day < 10:
        datestr += '0'
    datestr += str(now.day)
    if now.hour < 10:
        datestr += '0'
    datestr += str(now.hour)
    if now.minute < 10:
        datestr += '0'
    datestr += str(now.minute)
    datestrc =''
    # print (datestr)
    for i in  (datestr):
        datestrc += (alphs[int(i)-1])
    return (datestrc)

print(prdtcode())
