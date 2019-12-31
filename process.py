import os

def findSubjectAndScholarship(name):
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, 'information.txt')
    p=open(path,'r')
    f=p.readlines()
    response=0
    subject=0
    scholarship=0
    for line in f:
        info=line.split(',')
        if name==str(info[0])[:-1]:
            response=1
            subject=info[1]
            scholarship=info[2]
            break
    p.close()
    return response,subject,scholarship

def findPosition(name,subject):
    position=0
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, 'information.txt')
    p=open(path,'r')
    f=p.readlines()
    for line in f:
        info=line.split(',')
        #print(info[1])
        if subject in info[1]:
            #print(subject)
            position+=1
        if name==str(info[0])[:-1]:
            break
    p.close()
    return position
