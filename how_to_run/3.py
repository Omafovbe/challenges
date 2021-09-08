from flask import Flask

app = Flask(__name__)

app.route("/", defaults={"path": ""})

@app.route("/<path:path>")
def catch_all(path):
    return "False"


@app.route("/good")
def result():
    return "True"

if __name__ == '__main__':
    app.run()
