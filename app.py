from flask import Flask, render_template, request, jsonify
from face_auth import verify_face
from assistant import execute

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/verify", methods=["POST"])
def verify():

    image = request.files["image"]

    path = "uploads/captured.jpg"

    image.save(path)

    verified, username = verify_face(path)

    if verified:
        return jsonify({
            "success": True,
            "username": username
        })

    return jsonify({
        "success": False
    })


@app.route("/dashboard/<username>")
def dashboard(username):
    return render_template(
        "dashboard.html",
        username=username
    )

@app.route("/command/<path:cmd>")
def command(cmd):

    answer = execute(cmd)

    return {
        "success": True,
        "answer": answer
    }

if __name__ == "__main__":
    app.run(debug=True)