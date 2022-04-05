from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
data = None


@app.route("/")
def base():
    return render_template("base.html")


@app.route('/astronaut selection', methods=['POST', 'GET'])
def astronaut_selection():
    global data
    if request.method == 'GET':
        return render_template("astronaut_selection.html")
    elif request.method == 'POST':
        print("Данные из формы:")
        data = request.form.to_dict()
        if 'accept' not in data:
            data['accept'] = 'False'
        data['job'] = ', '.join(request.form.getlist('job'))
        del data['email']
        del data['file']
        print(data)
        return '''<link rel="icon" href="data:;base64,=">
        <center><h1>Форма отправлена</h1></center>'''


@app.route("/answer")
@app.route("/auto_answer")
def auto_answer():
    global data
    if data:
        return render_template("auto_answer.html", data=data)
    else:
        return '''<link rel="icon" href="data:;base64,=">
                <center><h1>Форма не отправлена!</h1></center>'''


def main():
    app.run(port=8081, host='127.0.0.1')


if __name__ == '__main__':
    main()
