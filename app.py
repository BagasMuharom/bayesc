from flask import Flask, make_response, render_template, jsonify, session, request, json
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import io
import bayesian
import numpy as np
import dataset

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', datasets = dataset.dataset)

@app.route('/testing')
def testing():
    data = request.args.get('data').split(',')
    data = list(map(int, data))
    hasil = bayesian.test(data)

    return jsonify(
        hasil = np.array(hasil).tolist()
    )

if __name__ == '__main__':
    app.secret_key = 'bayesian'
    app.run(debug=True)