import datetime

from flask import Flask , render_template , request

app = Flask(__name__)

@app.route('/hello',methods =["POST"])
def hello():
    name = request.form.get("name")
    name = name.title().strip()
    if name[:7] == "Ajinkya":
        now = datetime.datetime.now()
        birthday = now.month == 1 and now.day == 9
        date = "January 9"
        return render_template("hb.html", birthday=birthday , name=name, date = date)
    elif name[:6] == "Gaurav":
        now = datetime.datetime.now()
        birthday = now.month == 6 and now.day == 18
        date = "June 18"
        return render_template("hb.html", birthday=birthday, name = name , date=date)
    elif name == "Random":
        now = datetime.datetime.now()
        birthday = now.month == 7 and now.day == 2
        date = "July 2"
        return render_template("hb.html", birthday=birthday, name = name , date=date)
    elif name[:5] == "Anant":
        now = datetime.datetime.now()
        birthday = now.month == 10 and now.day == 15
        date = "October 15"
        return render_template("hb.html", birthday=birthday, name = name , date=date)
    elif name[:9] == "Shubhangi":
        now = datetime.datetime.now()
        birthday = now.month == 4 and now.day == 28
        date = "April 28"
        return render_template("hb.html", birthday=birthday, name = name , date=date)
    elif name[:7] == "Krishna":
        now = datetime.datetime.now()
        birthday = now.month == 11 and now.day == 25
        date = "November 25"
        return render_template("hb.html", birthday=birthday, name = name , date=date)
    elif name[:6] == "Mangal":
        now = datetime.datetime.now()
        birthday = now.month == 30 and now.day == 12
        date = "December 30"
        return render_template("hb.html", birthday=birthday, name = name , date=date)
    else:
        return render_template("details.html")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/details', methods = ["POST"])
def details():
    name = request.form.get("name")
    name = name.title().strip()
    month = request.form.get("month")
    month = month.capitalize().strip()
    dates = request.form.get("date")
    date = month +" "+ dates

    long_month_name = month
    datetime_object = datetime.datetime.strptime(long_month_name, "%B")
    month_number = datetime_object.month


    now = datetime.datetime.now()
    birthday = now.month == month_number and now.day == int(dates)
    return render_template("hb.html", birthday=birthday, name = name , date=date)
