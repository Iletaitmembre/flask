from pprint import pprint

from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def base():
    return render_template("base.html")


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/promotion')
def promotion():
    return render_template("promotion.html")


@app.route('/image_mars')
def image_mars():
    params = {"filename": url_for('static', filename='img/image_mars.png')}
    return render_template("image_mars.html", **params)


@app.route('/promotion_image')
def promotion_image():
    params = {"filename": url_for('static', filename='img/image_mars.png')}
    return render_template("promotion_image.html", **params)


@app.route('/astronaut selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return render_template("astronaut_selection.html")
    elif request.method == 'POST':
        print("Данные из формы:")
        value = dict(request.form)
        pprint(value)
        return '''<link rel="icon" href="data:;base64,=">
        <center><h1>Форма отправлена</h1></center>'''


def main():
    app.run(port=8081, host='127.0.0.1')


if __name__ == '__main__':
    main()
