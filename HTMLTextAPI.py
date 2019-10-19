from flask import Flask, request, jsonify
import pandas as pd
import json
import os
import urllib,json
import urllib.request
import html2text

app = Flask(__name__)


@app.route('/htmltext', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        request_json = request.get_json(force=True)
        unclean_input = pd.DataFrame(request_json, index=[0])
        if unclean_input['url'][0] == None:
            result = {"response": 'failure'}
            return (jsonify(result), 403)
        url = unclean_input['url'][0]
        
        # url = "https://en.wikipedia.org/wiki/Lionel_Messi"
        f = urllib.request.urlopen(url)
        # print(f.read())
        # f = codecs.open(f)
        input = str(f.read())

        h = html2text.HTML2Text()
        h.ignore_links = True
        x = h.handle(input)

            #print(probability[prediction])
        result = {
            "response": 'success',
            "result": x
        }
        return (jsonify(result),200)

# @app.route('/predict2', methods=['GET', 'POST'])
# def predict2():
#     seckey = os.environ["API_KEY"]
#     if request.method == 'POST':
#         request_json = request.get_json(force=True)
#         unclean_input = pd.DataFrame(request_json, index=[0])
#         if int(unclean_input['API_KEY'][0]) != int(seckey):
#             result = {"response": 'failure',
#                       "message": 'forbidden request',
#                       "error": 'Invalid API KEY'}
#             return jsonify(result), 403
#         else:
#             validator_result, reason = validate(unclean_input)
#             if validator_result == False:
#                 result = {
#                     "response": 'failure',
#                     "message": 'Invalid Request',
#                     "error": "Data Validation Failed for " + reason
#                 }
#                 return (jsonify(result), 422)
#             input = preprocessing(unclean_input)
#             slot_model = load("/var/www/html/DataScience/svm_slot_model.joblib")
#             prob = slot_model.predict_proba(input)
#             prob = prob[0]
#             delay = (15 * prob[0]) + (45 * prob[1]) + (75 * prob[2]) + (105 * prob[3]) + (150 * prob[4])
#             result = {
#                 "response": 'success',
#                 "model name": 'svm',
#                 "estimated delay": delay
#             }
#             return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
