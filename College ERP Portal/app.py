
from flask import Flask, render_template, request, redirect, url_for,session,send_file
import mysql.connector
import pdfkit
import os

app = Flask(__name__)
app.secret_key="NihalAhmad@123"
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Nihal@123',
    'database': 'project'
}
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
output_path = os.path.join(os.getcwd(), "admitcard.pdf")
db = mysql.connector.connect(**db_config)
query = db.cursor()

college="IEC College of Engineering and Technology"
college_address="Plot no. 4 , Knowledge Park - 1 , Greater Noida (UP) , 201310"


@app.route("/")
def home():
    return render_template("join.html")

@app.route('/submit', methods=['GET',"post"])
def submit():
    input = request.args.get('input')
    if input=='student-portal':
        return redirect(url_for("studentportal"))
    elif input=='faculty-portal':
        return redirect(url_for("facultyportal"))
    elif input=='admin-portal':
        return redirect(url_for("adminportal"))
    elif input=='admission-portal':
        return redirect(url_for("admissionportal"))
    elif input=='registration-portal':
        return redirect(url_for("registrationportal"))

@app.route("/studentportal")
def studentportal():
    return render_template("student.html")

@app.route("/facultyportal")
def facultyportal():
    return render_template("faculty.html")

@app.route("/adminportal")
def adminportal():
    return render_template("admin.html")

@app.route("/admissionportal")
def admissionportal():
    return render_template("admission.html")

@app.route("/admresponse")
def admresponse():
    return render_template("res-adm.html")

@app.route("/registrationportal")
def registrationportal():
    return render_template("registration.html")

@app.route("/regresponse")
def regresponse():
    return render_template("res-reg.html")

@app.route("/studentlogin",methods=["POST","get"])  
def studentlogin():
    input = request.args.get('input')
    if input=='faculty-portal':
        return redirect(url_for("facultyportal"))
    username = request.form['Roll_no']
    password = request.form['Password']
    
    qry = "SELECT * FROM studentusers WHERE Roll_no = %s AND Password = %s"
    query.execute(qry, (username, password))
    user = query.fetchone()
    qry="select Firstname,Middlename,Lastname from studentusers where Roll_no=%s and Password=%s "
    query.execute(qry,(username,password))
    tpl=query.fetchone()
    x,name="",""
    for i in tpl:
        x=x+i
    name=x.replace("-"," ")
    session['data']=name
    session['roll_no']=username
    if user:
        return redirect(url_for('studentui',username=name))
    else:
        error = 'Invalid username or password. Please try again.'
        return render_template('student.html', error=error)


@app.route("/facultylogin",methods=["POST","get"])  
def facultylogin():
    input = request.args.get('input')
    if input=='student-portal':
        return redirect(url_for("studentportal"))
    username = request.form['Username']
    password = request.form['Password']
    qry = "SELECT * FROM facultyusers WHERE Username = %s AND Password = %s"
    query.execute(qry, (username, password))
    user = query.fetchone()
    session['data']=username
    session['password']=password
    if user:
        return redirect(url_for('facultyui',username=username))
    else:
        error = 'Invalid username or password. Please try again.'
        return render_template('faculty.html', error=error)


@app.route("/adminlogin",methods=["POST","get"])  
def adminlogin():
    username = request.form['Username']
    password = request.form['Password']
    qry = "SELECT * FROM adminusers WHERE Username = %s AND Password = %s"
    query.execute(qry, (username, password))
    user = query.fetchone()
    session['data']=username

    if user:
        return redirect(url_for('adminui',username=username))
    else:
        error = 'Invalid username or password. Please try again.'
        return render_template('admin.html', error=error)

@app.route('/studentui/<username>')
def studentui(username):
    data=session.get('data')
    return render_template('student-ui.html',username=username)

@app.route('/facultyui/<username>')
def facultyui(username):
    data=session.get('data')
    return render_template('faculty-ui.html',username=username)

@app.route('/adminui/<username>')
def adminui(username):
    data=session.get('data')
    return render_template('admin-ui.html',username=username)

@app.route("/studentchoice",methods=["get"])
def studentchoice():
    data=session.get("data")
    input = request.args.get('input')
    if input=="dashboard":
        return redirect(url_for("studentdashboard",username=data))
    elif input=="profile":
        return redirect(url_for("studentprofile",username=data))
    elif input=="attendance":
        return redirect(url_for("studentattendance",username=data))
    elif input=="admitcard":
        return redirect(url_for("studentadmitcard",username=data))
    elif input=="result":
        return redirect(url_for("studentresult",username=data))
    elif input=="registrationform":
        return redirect(url_for("registrationportal",username=data))
    

@app.route("/facultychoice",methods=["get"])
def facultychoice():
    data=session.get('data')
    input = request.args.get('input')
    if input=="dashboard":
        return redirect(url_for("facultydashboard",username=data))
    elif input=="profile":
        return redirect(url_for("facultyprofile",username=data))
    elif input=="attendance":
        return redirect(url_for("facultyattendance",username=data))
    elif input=="lecture":
        return redirect(url_for("facultylecture",username=data))
    elif input=="marks":
        return redirect(url_for("facultymarksupload",username=data))   


@app.route("/studentdashboard/<username>")
def studentdashboard(username):
    roll_no=session.get("roll_no")
    qry="select course from studentdata where roll_no={}".format(roll_no)
    query.execute(qry)
    course=query.fetchone()
    session['course']=course[0]
    qry='select count(*) from 5semsubjects'
    query.execute(qry)
    total_subjects=query.fetchone()
    session['total_subjects']=total_subjects[0]
    attendance='90%'
    # data=session.get('data')
    return render_template("student-dashboard.html",name=username,roll_no=roll_no,course=course[0],total_subjects=total_subjects[0],attendance=attendance)

@app.route("/studentprofile/<username>")
def studentprofile(username):
    # data=session.get('data')
    roll_no=session.get("roll_no")
    qry="select * from studentprofile where roll_no={}".format(roll_no)
    query.execute(qry)
    data=query.fetchone()
    name=data[3]
    enrollment_no=data[2]
    fathername=data[4]
    mothername=data[5]
    contact=data[6]
    email=data[7]
    course=data[8]
    stream=data[9]
    year=data[10]
    section=data[11]
    address=data[12]

    return render_template("student-profile.html",roll_no=roll_no,name=username,enrollment_no=enrollment_no,college=college,fathername=fathername,mothername=mothername,
                           contact=contact,email=email,course=course,stream=stream,year=year,section=section,address=address)

@app.route("/studentattendance/<username>")
def studentattendance(username):
    # data=session.get('data')
    return render_template("student-attendance.html",name=username)

@app.route("/studentadmitcard/<username>")
def studentadmitcard(username):
    # data=session.get('data')
    return render_template("student-admitcard.html",name=username,visible=False)

@app.route("/studentresult/<username>")
def studentresult(username):
    # data=session.get('data')
    return render_template("student-result.html",name=username)

@app.route("/examdetails",methods=["post"])
def examdetails():
    name=session.get('data')
    roll_no=session.get('roll_no')
    exam=request.form['examname']
    qry = "SELECT * FROM 5semsubjects"
    query.execute(qry)
    subjects = query.fetchall()
    qry="select * from studentdata where roll_no={}".format(roll_no)
    query.execute(qry)
    row=query.fetchone()
    session['exam']=exam
    session['college']=college
    session['college_address']=college_address
    session['subjects']=subjects
    session['course']=row[3]
    session['section']=row[4]
    return render_template("student-admitcard.html",name=name,visible=True,college=college,college_address=college_address,roll_no=roll_no,course=row[3],section=row[4],exam=exam,subjects=subjects)

@app.route("/download-admitcard",methods=['post'])
def downloadadmitcard():
    name=session.get('data')
    roll_no=session.get('roll_no')
    college=session.get('college')
    college_address=session.get('college_address')
    course=session.get('course')
    section=session.get('section')
    exam=session.get('exam')
    subjects=session.get('subjects')
    rendered=render_template("admitcard.html",name=name,college=college,college_address=college_address,roll_no=roll_no,course=course,section=section,exam=exam,subjects=subjects)
    pdf = pdfkit.from_string(rendered, False,configuration=config)

    with open(output_path, 'wb') as file:
        file.write(pdf)

    return send_file(output_path, as_attachment=True)


@app.route("/facultydashboard/<username>")
def facultydashboard(username):
    password=session.get('password')
    qry="select * from facultyprofile where password={}".format(password)
    query.execute(qry)
    data=query.fetchone()
    faculty_id=data[0]
    department=data[8]
    return render_template("faculty-dashboard.html",username=username,faculty_id=faculty_id,department=department,subjects_alloted=1,name=username)

@app.route("/facultyprofile/<username>")
def facultyprofile(username):
    password=session.get('password')
    qry="select * from facultyprofile where password={}".format(password)
    query.execute(qry)
    data=query.fetchone()
    faculty_id=data[0]
    name=data[1]
    address=data[2]
    fathername=data[3]
    mothername=data[4]
    contact=data[5]
    email=data[6]
    qualification=data[7]
    department=data[8]
    return render_template("faculty-profile.html",name=username,username=username,faculty_id=faculty_id,fathername=fathername,mothername=mothername,contact=contact,email=email,qualification=qualification,college=college,department=department,address=address)

@app.route("/facultyattendance/<username>")
def facultyattendance(username):
    return render_template("attendanceupload.html",username=username)

@app.route("/facultylecture/<username>")
def facultylecture(username):
    return render_template("faculty-lecture.html",username=username)

@app.route("/facultymarksupload/<username>")
def facultymarksupload(username):
    return render_template("faculty-marksupload.html",username=username)

@app.route('/uploaded',methods=['post'])
def uploaded():
    return render_template("upload-res.html")
    
@app.route("/adminchoice",methods=["get"])
def adminchoice():
    data=session.get('data')
    input = request.args.get('input')
    if input=="dashboard":
        return redirect(url_for("admindashboard",username=data))
    elif input=="profile":
        return redirect(url_for("adminprofile",username=data))
    elif input=="studentrecord":
        return redirect(url_for("adminstudentrecord",username=data))
    elif input=="lectures":
        return redirect(url_for("adminlectures",username=data))
    elif input=="facultyrecord":
        return redirect(url_for("adminfacultyrecord",username=data))
    elif input=="admissionrequest":
        return redirect(url_for("adminadmissionrequest",username=data))
    elif input=="registrationrequest":
        return redirect(url_for("adminregistrationrequest",username=data))
    
@app.route("/admindashboard/<username>")
def admindashboard(username):
    return render_template("admin-dashboard.html",username=username)

@app.route("/adminprofile/<username>")
def adminprofile(username):
    return render_template("admin-profile.html",username=username)

@app.route("/adminstudentrecord/<username>")
def adminstudentrecord(username):
    return render_template("admin-studentrecord.html",username=username)

@app.route("/adminlectures/<username>")
def adminlectures(username):
    return render_template("admin-lectures.html",username=username)

@app.route("/adminfacultyrecord/<username>")
def adminfacultyrecord(username):
    return render_template("admin-facultyrecord.html",username=username)

@app.route("/adminadmissionrequest/<username>")
def adminadmissionrequest(username):
    return render_template("admin-admissionrequest.html",username=username)

@app.route("/adminregistrationrequest/<username>")
def adminregistrationrequest(username):
    return render_template("admin-registrationrequest.html",username=username)


if __name__ == '__main__':
    app.run(debug=True)
