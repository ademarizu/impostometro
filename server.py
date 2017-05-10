# coding=utf-8
from flask import Flask, app, request, Response
from client import ImpostometroClient
import json

app = Flask(__name__)

ic = ImpostometroClient()

@app.route('/counter')
def counter():
    state = request.args.get('state')
    city = request.args.get('city')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    callback = request.args.get('callback')

    if city:
        counter = ic.get_city_counter(state, city, start_date, end_date)
    else:
        counter = ic.get_state_counter(state, start_date, end_date)

    if callback:
        result = "{0}({1});".format(callback, counter)
    else:
        result = counter

    return Response(result, mimetype='application/javascript')


if __name__ == '__main__':
    app.run(debug=True)
