from flask import render_template
from flask_app import app


@app.route('/')
def hello_world():
    return render_template("hello.html")


@app.route('/goodbye')
def goodbye_world():
    return render_template("goodbye.html")


if __name__ == '__main__':
    app.run()
