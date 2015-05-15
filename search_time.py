import glob
fw=open("result.txt",'a')

for name in glob.glob('output*'):
    str=name[7:len(name)]
    list=str.split('_')
    fw.write(list[0]+' '+list[1]+' ')
    fr=open(name,'r')
    for line in fr:
        if 'time in fmm main' in line:
            fw.write(next(fr))
    fr.close()

fw.close()

