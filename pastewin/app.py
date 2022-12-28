import flask
import utils
from io import BytesIO


version = "0.3.0"
app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.redirect("/about")


@app.route("/about")
def about():
    return flask.render_template("about.html", version=version)


@app.route("/<id>")
def paste(id: str):
    content = utils.paste_content(id)

    return flask.render_template(
        "paste.html", id=id, size=utils.pretty_size(content), content=content,
    )


@app.route("/raw/<id>")
def raw(id: str):
    return flask.Response(utils.paste_content(id), mimetype="text/plain")


@app.route("/dl/<id>")
def download(id: str):
    buffer = BytesIO()
    buffer.write(utils.paste_content(id))
    buffer.seek(0)

    return flask.send_file(
        buffer,
        as_attachment=True,
        download_name=f"pastewin_{id}",
        mimetype="text/plain",
    )


@app.errorhandler(404)
def not_found(error):
    return flask.render_template("not_found.html"), 404


with app.test_request_context():
    flask.url_for("static", filename="style.css")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=utils.PORT, debug=True)
