from flask import Flask, jsonify, request
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping():
  return jsonify('pong')

BOOKS = [
    {
        'title': 'Nevernight',
        'author': 'Jay Kristoff',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': True
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': False
    }
]

@app.route('/books', methods=['GET', 'POST'])
def get_books():
  response = {'status':'success'}

  if (request.method == "POST"):

    post_data = request.get_json()
    BOOKS.append({
        'title': post_data.get('title'),
        'author': post_data.get('author'),
        'read': post_data.get('read')
    })
    response['message'] = 'Book added'
  else:
    response['books'] = BOOKS
  
  return jsonify(response)

if __name__ == '__main__':
  app.run()
