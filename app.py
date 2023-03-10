from flask import Flask
from flask import render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def sample():
    return "Welcome to Flask"


@app.route("/<name>")
def sample1(name):
    return f'Hi {name}'


@app.route("/templates")
def sample2():
    return render_template('index.html')


@app.route("/templates/<name>")
def sample3(name):
    return render_template("index2.html", name=name)


@app.route("/route/templates/<role>")
def sample4(role):
    if role == "guest":
        return redirect(url_for('sample2'))
    else:
        return redirect(url_for('sample3', name=role))


# List Rendering using for loop/for tag
@app.route("/list/rendering")
def sample5():
    lst = ["abc", "def", "ghi"]
    return render_template('index3.html', lst=lst)


@app.route("/templates/templateinheritance")
def sample6():
    lst = ["Suraj Kumar", "Arun Chodwary", "Vachaspathi Gnaneswar", "Ventaka Ramana"]
    return render_template('home.html', lst=lst)


@app.route("/form/studentform")
def sample7():
    return render_template('/studentform.html')


@app.route("/conditionalrendering")
def sample8():
    return render_template('iftag.html', value=1)


@app.route("/form/datahandling", methods=['GET', 'POST'])
def sample9():
    if request.method == "POST":
        name = request.form.get('std_name')
        number = request.form.get('std_mobile')
        return name
    return render_template('studentdetails.html')


if __name__ == "__main__":
    app.run(debug=True)
