from flask import Flask
import redis
import os

app = Flask(__name__)

redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = os.getenv("REDIS_PORT", 6379)
r = redis.Redis(host=redis_host, port=redis_port)

@app.route("/")
def index():
    try:
        r.incr("visits")
        count = r.get("visits").decode("utf-8")
    except redis.exceptions.ConnectionError:
        count = "Brak połączenia z Redisem"
    return f"Liczba odwiedzin: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)