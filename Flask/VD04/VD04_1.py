from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y %H:%M:%S")
    html = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Текущее время</title>
    </head>
    <body>
        <h1>Текущее дата и время:</h1>
        <p>{{ time }}</p>
    </body>
    </html>
    '''
    return render_template_string(html, time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
