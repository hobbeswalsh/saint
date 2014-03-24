#!/usr/bin/env python

import os

from flask import Flask, render_template

app = Flask("saint")


@app.route("/")
def serve_index():
    return render_template("index.html")


@app.route("/1")
def serve_index1():
    return render_template("index2.html")

@app.route("/2")
def serve_index2():
    return render_template("index3.html")


def main():
    port = os.environ.get("PORT", 5555)
    app.run(port=port)
    
if __name__ == "__main__":
    main()
