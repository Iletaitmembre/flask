from flask import Flask, render_template

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


def main():
    app.run()


if __name__ == '__main__':
    main()
