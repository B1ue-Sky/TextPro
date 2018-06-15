import re
import sys
import os,glob


path = os.getcwd()
NewPaths=[]


CheckText={
    'DynamicHysteresisResult':'HysSumm',
    'DynamicHysteresis':'Hys'
    }

CheckAgainText={
    'Table':'Info',
    'Time':'Data'
    }




DataList=os.listdir(path)
os.chdir(path)
for DataFile in DataList:
    if DataFile[0] == '_' or not os.path.isfile(path+'\\'+DataFile):
        print(DataFile+'>>Skip#')
        continue
    fs = open(DataFile,'r')
    print(DataFile+'>>Open')
    Start = 0
    for line in fs.readlines():
        SuffixText = line.split()
        if SuffixText != [] and SuffixText[0] in CheckText.keys():
            if Start == 0:
                Start = 1
                NewPath=path+'\\'+'_'+os.path.splitext(DataFile)[0]
                NewPaths.append(NewPath)
                try:             
                    os.mkdir(NewPath)
                except WindowsError:
                    print('Fatal Error: Already Processed!!!!')
                    fs.close()
                    os.system("pause")
                    sys.exit()
                os.chdir(NewPath)
                print(NewPath+'>>In!')
            else:
                sv.write('\n')
                sv.close()
                print(OutFile + '>>Done!')
            OutFile = '_' + os.path.splitext(DataFile)[0] + '_' + CheckText.get(SuffixText[0])
            sv=open(OutFile,'w')
            sv.write(line)
        elif Start != 0:
            sv.write(line)
        else:
            print(DataFile + '>>Data Error:Not start with specific text!!')
            break
    if Start != 0:
        sv.write('\n')
        sv.close()
        os.chdir(path)
        print(OutFile + '>>Done!>>Leave!')
    else:
        print(DataFile + '>>Skip!')
    fs.close()
print('See you Again')


for NewPath in NewPaths:
    DataList=os.listdir(NewPath)
    os.chdir(NewPath)
    Count=0
    for DataFile in DataList:
        if DataFile[0] != '_' or DataFile[1] == '_' or not os.path.isfile(NewPath+'\\'+DataFile):
            print(DataFile+'>>Skip##')
            fs.close()
            continue
        fs = open(DataFile,'r')
        print(DataFile+'>>Open Again')
        Order = 0
        Start = 0
        for line in fs.readlines():
            SuffixText = line.split()
            if SuffixText != [] and SuffixText[0] in CheckText.keys():
                OutFile = '_' + DataFile
                sv=open(OutFile,'w')
                sv.write(line)
                Start = 1
            elif Start != 0:            
                if SuffixText != [] and SuffixText[0] in CheckAgainText.keys():
                    sv.write('\n')
                    sv.close()
                    print(OutFile + '>>Done Again!')
                    OutFile = '_' + DataFile + '.'+CheckAgainText.get(SuffixText[0])+str(int(Order/2)+1)+'.txt'
                    Order=Order+1
                    sv=open(OutFile,'w')
                sv.write(line)
            else:
                print(DataFile + '>>Data Error:Do not use character _ for you personal file name!!')
                break
        if Start != 0:
            sv.write('\n')
            sv.close()
            print(OutFile + '>>Done Again!')
        else:
            print(DataFile + '>>Skip Again!')
        fs.close()
        os.remove(DataFile)
        Count=max(Count,int((Order-1)/2)+1)
    print(DataFile+'>>>>Finished!')
    sv=open(NewPath+'\\'+'_Total_'+str(Count)+'_Data','w')
    sv.close()
print('Success!\nBye')
os.system("pause")



