from flask import Flask, jsonify, request, abort


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Python'


if __name__ == "__main__":
  app.run()
  