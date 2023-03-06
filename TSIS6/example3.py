f =open('rawdata.txt', mode = 'r')


f.readline()
fpath = './rawdata.txt'
with open(fpath, mode = 'w')  as f:
      print(f.read())
      
