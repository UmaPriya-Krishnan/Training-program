from flask import Flask, jsonify,render_template,request,redirect,url_for
from flask_mysqldb import  MySQL
from flask_cors import CORS
import sys
sys.path.append("C:\\Users\\umapriya.krishnan\\Desktop\\student_project\\Student_project-kanth_feature\\src\\test")
import unittest
from ut import *
#print(sys.path)
#import student_unittesting

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'mysql'
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSON_SORT_KEYS'] = False

CORS(app)
CORS()
mysql=MySQL(app)

@app.route('/tables')
def tables():
    cur = mysql.connection.cursor()
    cur.execute("SHOW TABLES")
    fetchdata = cur.fetchall()
    tables = jsonify(fetchdata)
    return tables
    cur.close()

@app.route('/')
def tab():
    return render_template('index.html') 

@app.route('/testing', methods=["POST", "GET"])
def testing():
    if request.method == 'POST':
      result = request.data
      #print(result)
      result=result.decode("utf-8")
      table_name=result.split(":")[1].replace("{", "").replace("'","").replace("}","").replace('"','')
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
      data = open ("C:\\Users\\umapriya.krishnan\\Desktop\\angular\\grid\\src\\app\\testing\\testing.component.html", "r+")
      data.seek(0)
      data.truncate()
      runner = unittest.TextTestRunner(data)
      unittest.main(testRunner=runner, exit = False)
      data.flush()
      data.close()          
    return "True"
 


@app.route('/details_main')
def details_main():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM details_main")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/dimension_calender_details')
def dimension_calender_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_calender_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
    return response
    cur.close()

@app.route('/dimension_course_details')
def dimension_course_details():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dimension_course_details")
    fetchdata=cur.fetchall()
    response=jsonify(fetchdata)
    #response.status_code=200
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

@app.route('/dummy/<string:ename>', methods=["POST", "GET", "PUT", "DELETE"])
def dummy(ename):
    if request.method == "DELETE":
        return "TRUE"
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM dummmy where clg = %s", [ename])
    fetchdata=cur.fetchone()
    response=jsonify(fetchdata)
    mysql.connection.commit()
    cur.close()
    #response.status_code=200
    return response

@app.route('/update_fact_student', methods=["POST", "GET"])
def update_fact_student():
    if request.method == 'POST':
        dataa = request.data
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"rowData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "update fact_student set DEP_ID = %s, COURSE_ID = %s, STAFF_ID = %s where STUDENT_ID = %s "  
        cur.execute(sql,[dl[1], dl[2], dl[3], dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "ABCD" 

@app.route('/update_details_main', methods=["POST", "GET"])
def update_details_main():
    if request.method == 'POST':
        dataa = request.data
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
    return "ABCD"

@app.route('/delete_fact_student', methods=["POST", "GET"])
def delete_fact_student():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from fact_student where STUDENT_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_fact_academics', methods=["POST", "GET"])
def delete_fact_academics():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from fact_academics where STUDENT_ID = %s;"  
        d2 = dl[0].split(",")
        cur.execute(sql,[d2[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_fact_attendence', methods=["POST", "GET"])
def delete_fact_attendence():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        print(dl)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from fact_attendence where STUDENT_ID = %s;" 
        d2 = dl[0].split(",")
        cur.execute(sql,[d2[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_fact_payment', methods=["POST", "GET"])
def delete_fact_payment():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from fact_payment where STUDENT_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_fact_placement', methods=["POST", "GET"])
def delete_fact_placement():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from fact_placement where STUDENT_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_details_main', methods=["POST", "GET"])
def delete_details_main():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from details_main where STUDENT_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_dimension_calender_details', methods=["POST", "GET"])
def delete_dimension_calender_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_calender_details where TIME_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_dimension_course_details', methods=["POST", "GET"])
def delete_dimension_course_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_course_details where COURSE_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_dimension_degree_details', methods=["POST", "GET"])
def delete_dimension_degree_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_degree_details where DEGREE_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_dimension_department_details', methods=["POST", "GET"])
def delete_dimension_department_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_department_details where DEP_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_dimension_exam_details', methods=["POST", "GET"])
def delete_dimension_exam_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_exam_details where EXAM_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_dimension_grade_details', methods=["POST", "GET"])
def delete_dimension_grade_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_grade_details where GRADE_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_dimension_payment_details', methods=["POST", "GET"])
def delete_dimension_payment_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        print(dt)
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_payment_details where FEE_ID = %s;" 
        d2 = dl[0].split("\"")
        d2 = d2[0].lstrip("\"")
        print(d2)
        cur.execute(sql,[d2] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True"

@app.route('/delete_dimension_placement_details', methods=["POST", "GET"])
def delete_dimension_placement_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_placement_details where COMPANY_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 

@app.route('/delete_dimension_staff_details', methods=["POST", "GET"])
def delete_dimension_staff_details():
    if request.method == 'POST':
        dataa = request.data
        dataa = dataa.decode("utf-8")
        dt = dataa.split(",\"")
        dl = []
        for i in range(len(dt)):
            st = (dt[i].strip("{\"delData\":[")) 
            sw = st.strip("\"]}")
            dl.append(sw)
        for i in range(len(dl)):
            print(dl[i])
        cur = mysql.connection.cursor()
        query = "SET foreign_key_checks=0"
        cur.execute(query)
        sql = "delete from dimension_staff_details where STAFF_ID = %s;"  
        cur.execute(sql,[dl[0]] )
        print(sql)
        mysql.connection.commit()
        cur.close()
    return "True" 
    
app.run(debug = True)