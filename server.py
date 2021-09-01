from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


# @app.route("/")
# def hello_world():
#     return render_template("index.html")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_csv(data)
            return redirect("/thanks.html")
        except:
            return "Did not save to database"
    else:
        return "something went wrong"


# def write_db(data):
#     with open("database.txt", mode="a") as database:
#         email = data["email"]
#         subject = data["name"]
#         message = data["message"]
#         file = database.write(f"\n{email},{subject},{message}")


def write_csv(data):
    with open("database.csv", mode="a") as database:
        email = data["email"]
        subject = data["name"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
