from flask import Flask

app = Flask(__name__)


@app.route("/sensor1", methods=["GET"])
def entry_point():
    return 'Hello Sensor 1!'


app.run(host="0.0.0.0", debug=True, port=3000)
