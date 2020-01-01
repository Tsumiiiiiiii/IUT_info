import os

def refined_name(name):
    name=name.split(' ')
    r_name=''
    for c in name:
        if c!=' ':
            r_name+=c
    return r_name

def check_name(name1,name2):
    return refined_name(name1)==refined_name(name2)

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
        if check_name(name,str(info[0])[:-1]):
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
        if subject in info[1]:
            position+=1
        if check_name(name,str(info[0])[:-1]):
            break
    p.close()
    return position
