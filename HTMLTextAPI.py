from flask import Flask, request, jsonify
import pandas as pd
import json
import os
import urllib, json
import urllib.request
import html2text

app = Flask(__name__)


@app.route('/htmltext', methods=['GET', 'POST'])
def html2text():
    if request.method == 'POST':
        request_json = request.get_json(force=True)
        unclean_input = pd.DataFrame(request_json, index=[0])
        if unclean_input['url'][0] == None:
            result = {"response": 'failure'}
            return (jsonify(result), 403)
        url = unclean_input['url'][0]

        f = urllib.request.urlopen(url)

        input = str(f.read())

        h = html2text.HTML2Text()
        h.ignore_links = True
        x = h.handle(input)
        result = {
            "response": 'success',
            "result": x
        }
        return (jsonify(result), 200)


if __name__ == '__main__':
    app.run(debug=True)