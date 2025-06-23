from flask import Flask, request
import os

app = Flask(__name__)
admin_password = os.getenv("ADMIN_PASSWORD")

@app.route("/")
def index():
    password = request.args.get("password")
    
    if password is None:
        return "<h2>Введите пароль в URL-параметре ?password=</h2>"

    if password == admin_password:
        return '<body style="background-color:green;"><h1>Добро пожаловать, администратор!</h1></body>'
    else:
        return '<body style="background-color:red;"><h1>Неверный пароль!</h1></body>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
