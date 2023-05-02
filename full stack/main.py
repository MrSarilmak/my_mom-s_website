import json

from flask import *

app = Flask(__name__)
apploication_db = json.load(open("apploication_db.json", "r"))
last_id = 0
if apploication_db:
    last_id = int(apploication_db[-1]["id"])
else:
    apploication_db = []


@app.route("/", methods=["GET", "POST"])
def index_page():
    return render_template("index.html")


@app.route("/2", methods=["GET", "POST"])
def index2_page():
    return render_template("index2.html")


@app.route("/about_me", methods=["GET", "POST"])
def about_me_page():
    return render_template("about_me.html")


@app.route("/services", methods=["GET", "POST"])
def services_page():
    return render_template("services.html")


@app.route("/tests/i.2", methods=["GET", "POST"])
def test_indexd2_page():
    return render_template("tests/index.2.html")


@app.route("/tests/i2.2", methods=["GET", "POST"])
def test_index2d2_page():
    return render_template("tests/index2.2.html")


def create_apploication(first_name, last_name, email):
    global last_id
    last_id = last_id + 1
    apploication = {"id": str(last_id), "first_name": first_name,
                    "last_name": last_name, "email": email}
    apploication_db.append(apploication)
    with open("apploication_db.json", "w") as db_file:
        json.dump(apploication_db, db_file, indent=4)


@app.route("/contact", methods=["GET", "POST"])
def contact_api():
    if request.method == "GET":
        return render_template("errors/error_404.html")
    else:
        # response = {"responce": {"type": "", "data": ""}}
        # return json.dumps(response)
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("e-mail")
        url = request.form.get("url")
        if not url:
            url = "/"
        create_apploication(first_name, last_name, email)
        print(url)
        return redirect(url)


def login_required(lq_session):
    return True


@app.route("/contacts", methods=["GET", "POST"])
def contacts_page_api():
    if login_required(session):
        if request.method == "GET":
            return render_template("contacts.html")
        else:
            response = {"responce": {"type": "", "data": ""}}
            return json.dumps(response)
    else:
        return render_template("errors/error_404.html"), 404


def adminka_login(login, password):
    return False


@app.route("/adminka", methods=["GET", "POST"])
def adminka_page_api():
    if login_required(session):
        if request.method == "GET":
            return render_template("adminka.html")
        else:
            response = {"responce": {"type": "", "data": ""}}
            return json.dumps(response)
    else:
        if request.method == "GET":
            return render_template("adminka_login.html")
        else:
            login = request.form.get("login")
            password = request.form.get("password")
            if adminka_login(login, password):
                return render_template("adminka.html")
            else:
                return render_template("adminka_login.html")


@app.errorhandler(404)
def error_404_page(err):
    return render_template("errors/error_404.html", err=err)


@app.errorhandler(500)
def error_404_page(err):
    return render_template("errors/error_500.html", err=err)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3610)
