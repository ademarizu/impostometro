# coding=utf-8
from flask import Flask, app, request, Response
from client import ImpostometroClient
import json

app = Flask(__name__)

ic = ImpostometroClient()

@app.route('/counter')
def counter():
    state = request.args.get('state')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    callback = request.args.get('callback')

    counter = handle_counter(state, start_date, end_date)
    if callback:
        result = "{0}({1});".format(callback, counter)
    else:
        result = counter

    return Response(result, mimetype='application/javascript')


def handle_counter(state, start_date, end_date):
    return ic.get_counter(state, start_date, end_date)


if __name__ == '__main__':
    app.run(debug=True)
