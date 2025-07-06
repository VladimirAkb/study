from flask import Flask, render_template, request
import requests

quote = None

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   choice = None
   quote = None
   if request.method == 'POST':
       choice = request.form['choice']
       if choice == 'q1':
           quote = get_quote1()
       elif choice == 'q2':
           quote = get_quote2()
       elif choice == 'q3':
           quote = get_quote3()
   #print(quote)
   return render_template("index.html", quote = quote)

def get_quote1():
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url)
    return(response.json())

def get_quote2():
    url = 'https://zenquotes.io/api/random'
    response = requests.get(url, headers={'X-Api-Key': 'P6jgxgSsALziI20SferWRA==K3INlYTLuddSuxQX'})
    #print(response.json())
    return(response.json())

def get_quote3():
    quotes_collection = []
    url = 'https://quoteslate.vercel.app/api/quotes/random'
    response = requests.get(url)
    #print(response.json())
    #return(response.json())
    if response.status_code == 200:
        data = response.json()
        # Предполагаем, что в ответе есть поля 'quote' и 'author'
        quote = data.get('quote')
        author = data.get('author')
        # Добавляем в коллекцию в нужном формате
        quotes_collection.append({
        'q': quote,
        'a': author
        })
        print(quotes_collection)
    else:
        print('Ошибка при получении данных с API:', response.status_code)
        quotes_collection.append({
        'q': 'none',
        'a': 'none'
        })
    return (quotes_collection)


if __name__ == '__main__':
   app.run(debug=True)