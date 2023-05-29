from flask import Flask, render_template
app = Flask(__name__)


@app.route("/play")
def play():
    num = 3
    color = "#9fc5f8"
    return render_template("index.html", num=num, color=color)


@app.route("/play/<int:num>")
def playwithnum(num):
    color = "#9fc5f8"
    return render_template("index.html", num=num, color=color)

@app.route("/play/<int:num>/<string:color>")
def hello_world(num, color):
    return render_template("index.html", num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)