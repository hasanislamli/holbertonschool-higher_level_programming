#!/usr/bin/python3
"""
Flask app to display products from JSON or CSV
"""

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


# --- Read JSON ---
def read_json():
    with open("products.json", "r") as f:
        return json.load(f)


# --- Read CSV ---
def read_csv():
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # --- Validate source ---
    if source not in ["json", "csv"]:
        return render_template("product_display.html", error="Wrong source")

    # --- Load data ---
    if source == "json":
        data = read_json()
    else:
        data = read_csv()

    # --- Filter by id ---
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Product not found")

        data = [p for p in data if p["id"] == product_id]

        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
