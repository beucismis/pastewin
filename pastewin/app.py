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
    size = pretty_size(text)

    return render_template("paste.html", id=id, size=size, text=text)


@app.route("/about")
def about():
    return render_template("about.html")


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
        attachment_filename=f"pastewin_{id}.txt",
        mimetype="text/text/plain",
    )


@app.errorhandler(404)
def paste_not_found(error):
    return render_template("paste_not_found.html"), 404


with app.test_request_context():
    url_for("static", filename="style.css")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
