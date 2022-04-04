from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    title = title
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template('In-flight training.html', occupation=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
