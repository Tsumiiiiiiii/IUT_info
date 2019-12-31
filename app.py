
# A python web app to display the admission status of a student

from flask import Flask,request
#from process import findSubjectAndScholarship,findPosition

import requests
import bs4

def findSubjectAndScholarship(name):
    url='http://admission.iutoic-dhaka.edu/admitted-list/8'
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    global students
    students=soup.find_all('tr')
    response=0
    subject=0
    scholarship=0
    for student in students:
        info=list(student)
        student_name=info[7]
        if name in student_name:
            response=1
            subject=str(info[11])[24:-5]
            if 'Self' in subject:
                scholarship='NONE(SELF)'
                subject=subject[:-5]
            elif 'Full Scholarship' in subject:
                scholarship='FULL'
                subject=subject[:-17]
            else:
                scholarship='PARTIAL'
            break
    return response,subject,scholarship

def findPosition(name,subject):
    position=0
    for student in students:
        info=list(student)
        if subject in str(info[11]):
            position+=1
        if name in str(info[7]):
            break
    return position

app = Flask(__name__)
#app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    if request.method=='POST':
        #name=request.form.get('name').upper()
        name=request.form['name'].upper()
        response,subject,scholarship=findSubjectAndScholarship(name)
        if response:
            position=findPosition(name,subject)
            return '''
                <html>
                    <body>
                        <p>NAME                   : {name}</p>
                        <p>DEPARTMENT             : {subject}</p>
                        <p>POSITION IN DEPARTMENT : {position}</p>
                        <p>SCHOLARSHIP            : {scholarship}</p>
                        <p><a href="http://sadhobbit12345.pythonanywhere.com/">Click here to search again</a></p>
                    </body>
                </html>
            '''.format(name=name,subject=subject,position=position,scholarship=scholarship)
        else:
            return '''
                <html>
                    <body>
                        <p>ERROR! NAME NOT FOUND</p>
                        <p>LENGTH IS {len}</p>
                        <p><a href="http://sadhobbit12345.pythonanywhere.com/">Click here to search again</a></p>
                    </body>
                </html>
            '''.format(len(name))
    return '''
        <html>
            <body>
                <p>ENTER YOUR NAME(THAT YOU USED IN IUT) :</p>
                <form method="post" action=".">
                    <p><input name="name" /></p>
                    <p><input type="submit" value="GET MY INFO" /></p>
                </form>
            </body>
        </html>
    '''

if __name__=='__main__' :
    app.run()