from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    title = title
    return render_template('base.html', title=title)


@app.route('/list_prof/<val>')
def list_prof(val):
    return render_template('List of professions.html', val=val)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
