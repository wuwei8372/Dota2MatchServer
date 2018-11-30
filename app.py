from flask import Flask, render_template, request, json
from outcome_prediction_knn_final import predict_knn
from flask_cors import CORS
from recommend import recommend

app = Flask(__name__)
CORS(app)

@app.route('/predictMatch', methods=['POST'])
def predictMatch():
    myTeam = request.get_json().get('myTeam')
    opponentTeam = request.get_json().get('opponentTeam')
    tier = int(request.get_json().get('tier'))
    
    # print(type(tier))
    
    # myTeam = [3,5,12,34,64]
    # opponentTeam = [87,3,34,2,14]
    # opponentTeam = [73, 102, 2, 38, 55]
    # myTeam = [68, 1, 113, 65, 66]
    # tier = 35
    # print(type(tier))
    print(myTeam)
    print(opponentTeam)
    print(tier)
    outcome = predict_knn(opponentTeam, myTeam, tier)
    print(outcome)
    res = json.dumps({
        'res': outcome
    })
    return res

@app.route('/recommend', methods=['POST'])
def recommendRoute():
    tier = request.get_json().get('tier')
    id = request.get_json().get('id')
    tier = int(tier)
    # myTeam = [3,5,12,34,64]
    # opponentTeam = [87,3,34,2,14]
    print(tier)
    print(id)
    outcome = recommend(tier, id)
    print outcome
    res = json.dumps({
        'res': outcome
    })
    return res
    
  
    


if __name__=="__main__":
    app.run()