from os import environ
from io import BytesIO

import urllib3
from flask import abort
from flask import Flask
from flask import url_for
from flask import redirect
from flask import Response
from flask import send_file
from flask import render_template

from utils import pretty_size


version = "0.1.0"

app = Flask(__name__)
http = urllib3.PoolManager()


def get_paste(id: str):
    r = http.request("GET", f"https://pastebin.com/raw/{id}")

    if r.status != 200:
        abort(404)

    return r


@app.route("/")
def index():
    return redirect("/about")


@app.route("/<id>")
def paste(id: str):
    paste = get_paste(id)  # Test ID: B5EfdLF6
    text = paste.data.decode("utf-8")

    return render_template("paste.html", id=id, size=pretty_size(text), text=text)


@app.route("/about")
def about():
    return render_template("about.html", version=version)


@app.route("/raw/<id>")
def raw(id: str):
    paste = get_paste(id)

    return Response(paste.data.decode("utf-8"), mimetype="text/plain")


@app.route("/dl/<id>")
def download(id: str):
    paste = get_paste(id)

    buffer = BytesIO()
    buffer.write(paste.data)
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name=f"pastewin_{id}",
        mimetype="text/plain",
    )


@app.errorhandler(404)
def paste_not_found(error):
    return render_template("paste_not_found.html"), 404


with app.test_request_context():
    url_for("static", filename="style.css")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)), debug=True)
