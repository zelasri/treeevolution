from flask import Flask
import json
from treevolution.base.geometry import Point
W_WIDTH, W_HEIGHT = 100, 100
app = Flask(__name__)
@app.route('/')
def index():
    """
        Route which generates random point
    """
    point = Point.random(W_WIDTH, W_HEIGHT)
    return json.dumps({"x": point.x, "y": point.y})