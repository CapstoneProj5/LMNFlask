
from utils.scheduler.tasks import scheduler
from flask import render_template, Flask, current_app
from flask_app import app

log = app.logger  # log.info(), log.warn(), log.err


@app.route('/')
def hello_world():
    return render_template("hello.html")


@app.route('/goodbye')
def goodbye_world():
    return render_template("goodbye.html")


def factory():
    app = Flask(__name__)
    return app


if __name__ == '__main__':
    app.debug = False
    scheduler.start()
    app.run()
