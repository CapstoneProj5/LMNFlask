
from flask import Flask, render_template

app = Flask(__name__)
log = app.logger  # log.info(), log.warn(), log.err


@app.route('/')
def hello_world():
    return render_template("hello.html")


@app.route('/goodbye')
def goodbye_world():
    return render_template("goodbye.html")


if __name__ == '__main__':
    app.run()
