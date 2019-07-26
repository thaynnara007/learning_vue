from flask import Flask, jsonify
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
  return jsonify({
    "status": "success",
    "books": BOOKS
  })

if __name__ == '__main__':
  app.run()
