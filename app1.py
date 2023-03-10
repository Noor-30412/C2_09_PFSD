from flask import *
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")

db = client['STUDENT']

studentdetails = db.DETAILS

app = Flask(__name__)


@app.route("/crudexample")
def sample10():
    return render_template('studentform.html')


@app.route("/success", methods=['GET', 'POST'])
def onsubmit():
    fname = request.form.get('fn')
    lname = request.form.get('ln')
    rollno = request.form.get('regno')
    mob = request.form.get('mb')

    a = {"First Name": fname, "Last Name": lname,
         "Regd Number": rollno, "Mobile Number": mob}

    studentdetails.insert_one(a)

    # Retrive

    b = studentdetails.find()
    return render_template('retrive.html', b=b)


if __name__ == "__main__":
    app.run()
