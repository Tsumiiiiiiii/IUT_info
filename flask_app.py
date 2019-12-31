
# A python web app to display the admission status of a student

from flask import Flask,request
from process import findSubjectAndScholarship,findPosition

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    if request.method=='POST':
        #name=request.form.get('name').upper()
        name=str(request.form['name']).upper()
        response,subject,scholarship=findSubjectAndScholarship(name)
        if response:
            position=findPosition(name,subject)
            return '''
                <html>
                    <body>
                        <p>NAME                   : {name}</p>
                        <p>DEPARTMENT             : {subject}</p>
                        <p>POSITION IN DEPARTMENT : {position}</p>
                        <p>OIC-SCHOLARSHIP            : {scholarship}</p>
                        <p><a href="http://sadhobbit12345.pythonanywhere.com/">Click here to search again</a></p>
                        <p>DISCLAIMER: THIS IS NOT THE FINAL POSITION. POSITION MIGHT CHANGE AFTER FURTHER MIGRATIONS </p>
                    </body>
                </html>
            '''.format(name=name,subject=subject,position=position,scholarship=scholarship)
        else:
            return '''
                <html>
                    <body>
                        <p>ERROR! NAME NOT FOUND</p>
                        <p><a href="http://sadhobbit12345.pythonanywhere.com/">Click here to search again</a></p>
                    </body>
                </html>
            '''
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
