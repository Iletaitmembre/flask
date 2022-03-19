from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def nothing_func():
    return '<link rel="icon" href="data:;base64,=" />'


@app.route('/choice/<planet_name>')
def choice_func(planet_name):
    params = {"planet_name": planet_name}
    if planet_name in ["Меркурий',Венера", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун"]:
        params["proximity"] = "Эта планета близка к Земле;"
    else:
        params["proximity"] = "Эта планета очень далека от Земли;"
    return render_template("promotion_image.html", **params)


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
