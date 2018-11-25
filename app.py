from flask import Flask, render_template, request, json
from outcome_prediction_knn_final import predict_knn
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predictMatch', methods=['POST'])
def predictMatch():
    myTeam = request.get_json().get('myTeam')
    opponentTeam = request.get_json().get('opponentTeam')
    
    # myTeam = [3,5,12,34,64]
    # opponentTeam = [87,3,34,2,14]
    print(myTeam)
    print(opponentTeam)
    outcome = predict_knn(opponentTeam, myTeam)
    print outcome
    res = json.dumps({
        'res': outcome
    })
    return res
    
  
    


if __name__=="__main__":
    app.run()