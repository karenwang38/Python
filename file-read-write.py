fp=open('filetest.txt', 'w')
if fp !=None:
    print('open file success')
fp.close()

fp=open('filetest.txt', 'w')
if fp !=None:
    fp.write('A dog')
fp.close()

fp=open('filetest.txt', 'w')
if fp !=None:
    fp.write('A cat')
fp.close()

fp=open('filetest.txt', 'r')
if fp !=None:
    str=fp.read()
    print('----- file context read(): -----')
    print(str)
fp.close()

fp=open('filetest.txt', 'r')
if fp !=None:
    strList=fp.readlines()
    print('----- file context readlines(): -----')
    print(strList)
fp.close()

array=['a', 'b', 'c' ,'d']
fp=open('filetest.txt', 'w')
if fp !=None:
    for a in array:
        fp.write(a)
        fp.write(",")
fp.close()
