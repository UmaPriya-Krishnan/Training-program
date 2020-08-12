from flask import Flask, jsonify,render_template, redirect, request, url_for, Response, make_response
from flask_mysqldb import  MySQL
from flask_cors import CORS
import sys, os.path
#sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'test'))
sys.path.append("C:\\Users\\umapriya.krishnan\\Desktop\\student_project\\Student_project-kanth_feature\\src\\test")
import unittest
from ut import *

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'studentdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSON_SORT_KEYS'] = False
CORS(app)
mysql=MySQL(app)

# @app.route('/unittest',methods=["GET", "POST"])
# def unittest():
#     obj = student_unittesting.check_student()
#     return obj

@app.route('/testing', methods=["POST", "GET"])
def testing():
    #print(request.form)
    if request.method == "POST" :  
        table_name = request.form ["tabname"]
        print(table_name)
        test_name = 'test_%s_creation' % table_name
        test = test_creation(table_name)
        setattr(check_student, test_name, test)
        test_name = 'test_%s_validation' % table_name
        test2 = test_validations(table_name)
        setattr(check_student, test_name, test2)
        test_name = 'test_%s_insertion' % table_name
        test1 = test_insertion(table_name)
        setattr(check_student, test_name, test1)
        #with open ("templates\\testing.html", "r+") as data:
        data = open ("templates\\testing.html", "r+")
        data.seek(0)
        data.truncate()
        runner = unittest.TextTestRunner(data)
        unittest.main(testRunner=runner, exit = False)
        data.flush()
        data.close()          
        return redirect(url_for('output'))
    else:
        return render_template("index.html")

@app.route('/ang', methods=["POST", "GET"])
def ang():
    if request.method == "POST" :  
        # resp = make_response("hello")
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        #return resp
        name = request.form['tablename']   
        print(name)
        return "True"

@app.route('/output')
def output():
    return render_template("testing.html")

# @app.route("/<val>")
# def user(val):
#     return val

@app.route('/tables')
def tables():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES")
    fetchdata = cur.fetchall()
    tables = jsonify(fetchdata)
    return tables
    cur.close()

@app.route('/details_main')
def details_main():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM details_main")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    return response
    cur.close()

@app.route('/dimension_calender_details')
def dimension_calender_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_calender_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    return response
    cur.close()

@app.route('/dimension_course_details')
def dimension_course_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_course_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    return response
    cur.close()

@app.route('/dimension_degree_details')
def dimension_degree_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_degree_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/dimension_department_details')
def dimension_department_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_department_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/dimension_exam_details')
def dimension_exam_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_exam_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/dimension_grade_details')
def dimension_grade_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_grade_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/dimension_payment_details')
def dimension_payment_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_payment_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/dimension_placement_details')
def dimension_placement_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_placement_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/dimension_staff_details')
def dimension_staff_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_staff_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/fact_academics')
def fact_academics():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fact_academics")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/fact_attendence')
def fact_attendence():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fact_attendence")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/fact_payment')
def fact_payment():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fact_payment")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/fact_placement')
def fact_placement():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fact_placement")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/fact_student')
def fact_student():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fact_student")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/test',methods=["GET"])
def test():
    table = request.args.get('tablename')
    return table

app.run(debug = True)