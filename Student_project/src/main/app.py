from flask import Flask, jsonify,render_template,request
from flask_mysqldb import  MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JSON_SORT_KEYS'] = False
CORS(app)
mysql=MySQL(app)

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

@app.route('/test',methods=["GET"])
def test():
    table = request.args.get('tablename')
    #tb=table.get('tablename')
    #print(tb)
    return table

app.run(debug = True)