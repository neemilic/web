from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>форма</title>
                          </head>
                          <body>
                            <div>
                                <form class="login_form" method="post">
                                    <h1>Анкета претендента 
                                    на участие в миссии</h1>
                                    <br>
                                    <input class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <br>
                                    <input class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите ваш email" name="email">
                                    <br>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное образование</option>
                                          <option>Среднее образование</option>
                                          <option>Высшее образование</option>
                                        </select>
                                     </div>
                                    <br>
                                    <label for="form-check">Какие у вас есть профессии?</label>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="first" name="first">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="second" name="second">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="second" name="second">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="second" name="second">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                    </div>
                                    <div>
                                        <input type="checkbox" class="form-check-input" id="second" name="second">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="4" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8000, host='0.0.0.0')
