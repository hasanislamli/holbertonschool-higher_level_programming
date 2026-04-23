#!/usr/bin/python3
"""
Flask app with JSON, CSV and SQLite support
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# ---------------- JSON ----------------
def read_json():
    with open("products.json", "r") as f:
        return json.load(f)


# ---------------- CSV ----------------
def read_csv():
    products = []
    with open("products.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products


# ---------------- SQLITE ----------------
def read_sql():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()

        conn.close()

        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })

        return products

    except Exception as e:
        return {"error": str(e)}


# ---------------- ROUTE ----------------
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # invalid source
    if source not in ["json", "csv", "sql"]:
        return render_template("product_display.html", error="Wrong source")

    # load data
    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        sql_data = read_sql()

        # DB error
        if isinstance(sql_data, dict) and "error" in sql_data:
            return render_template("product_display.html", error="Database error")

        data = sql_data

    # filter by id
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
