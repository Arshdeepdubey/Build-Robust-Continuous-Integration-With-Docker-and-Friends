# src/page_tracker/app.py

import os
from functools import cache

from flask import Flask
from redis import Redis

app = Flask(__name__)
# redis = Redis()

@app.get("/")
def index():
#    page_views = redis.incr("page_views")
    page_views = redis().incr("page_views")
    return f"This page has been seen {page_views} times."

@cache
def redis():
    return Redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
