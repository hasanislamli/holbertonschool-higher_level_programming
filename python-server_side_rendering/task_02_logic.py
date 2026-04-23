#!/usr/bin/python3
"""
Flask app with dynamic JSON + Jinja loop/conditions
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    # JSON faylını oxu
    with open('items.json', 'r') as file:
        data = json.load(file)

    items_list = data.get("items", [])

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
