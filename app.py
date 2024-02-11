from flask import Flask

import json
import os

app = Flask(__name__)


@app.route("/api/on", methods=["POST"])
def turn_on_screen():
    os.system("xset -d :0 dpms force on")
    return {"status": "ok"}


@app.route("/api/off", methods=["POST"])
def turn_off_screen():
    os.system("sleep 1 && xset -d :0 dpms force off")
    return {"status": "ok"}


if __name__ == "__main__":
    with open("configs.json") as file:
        configs = json.load(file)

    host = configs["host"] if "host" in configs.keys() else None
    port = configs["port"] if "port" in configs.keys() else None
    debug = configs["debug"] if "debug" in configs.keys() else None

    app.run(host=host, port=port, debug=debug)
