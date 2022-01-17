import statistics
import numpy as np

from flask import Flask
from flask import request
from heapq import nsmallest
from heapq import nlargest

app = Flask(__name__)

@app.route("/")
def hello():
    return "Math API, use /min, /max, /avg, /median, /percentile end points to get the results for your input"


@app.route('/min',methods=['GET'])
def minimumNumbers():
    data = request.get_json()
    return str(nsmallest(data['quantifier'], data['list']))


@app.route('/max',methods=['GET'])
def maxNumbers():
    data = request.get_json()
    return str(nlargest(data['quantifier'], data['list']))

@app.route('/avg',methods=['GET'])
def avgOfNumbers():
    data = request.get_json()
    list = data['list']
    if len(list)!=0 : return str(sum(list) / len(list))
    else: return str(0)

@app.route('/median',methods=['GET'])
def medianOfNumbers():
    data = request.get_json()
    if len(data['list'])== 0 :
        return 'Empty List'
    else: return str(statistics.median(data['list']))


@app.route('/percentile',methods=['GET'])
def percentile():
    data = request.get_json()
    return str(np.percentile(data['list'],data['quantifier']))

if __name__ == "__main__":
    app.run()