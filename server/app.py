from flask import Flask, jsonify, request
from gptCalls.getImageVerification import verify  
from dashboard import dashboardResponse
from stats.leaderboards import leaderboard
from check_firebase_auth import check_firebase_auth
from bets import betResponse
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(verify)
app.register_blueprint(dashboardResponse)
app.register_blueprint(betResponse)
app.register_blueprint(leaderboard)

@app.route("/")
def landing():
    return '<p>helloworld</p>'


if __name__ == '__main__':
    app.run(debug=True)