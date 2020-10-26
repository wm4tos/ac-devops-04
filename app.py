import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def main():
  numbers = []

  nterms = 50

  n1, n2 = 0, 1
  count = 0

  while count < nterms:
    numbers.append(f"{n1}")
    nth = n1 + n2

    n1 = n2
    n2 = nth
    count += 1

  return "<br>".join(numbers)

if __name__ == '__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)