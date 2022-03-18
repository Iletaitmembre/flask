from flask import Flask, render_template, url_for

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


def main():
    app.run(port=8081, host='127.0.0.1')  # если я использую порт 8080 - сайт ломается


if __name__ == '__main__':
    main()
