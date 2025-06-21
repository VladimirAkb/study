from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def home():
    user_data = {}
    if request.method == 'POST':
        user_data['name'] = request.form.get('name')
        user_data['city'] = request.form.get('city')
        user_data['hobby'] = request.form.get('hobby')
        user_data['age'] = request.form.get('age')

    return render_template('blog.html', user_data=user_data)
