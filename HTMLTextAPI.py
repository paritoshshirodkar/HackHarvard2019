from flask import Flask, request, jsonify, Response
import pandas as pd
import json
import os
import urllib
import json
import urllib.request
import html2text
from helper import give_top_words, get_meme_urls
app = Flask(__name__)


@app.route('/meme_generator', methods=['GET', 'POST'])
def meme_generator():
    print("1", request.method)
    if request.method == 'POST':
        request_json = request.get_json(force=True)
        unclean_input = pd.DataFrame(request_json, index=[0])
        if unclean_input['url'][0] == None:
            result = {"response": 'failure'}
            return (jsonify(result), 403)
        url = unclean_input['url'][0]
        f = urllib.request.urlopen(url)
        input = str(f.read())
        important_words = give_top_words(input)
        meme_list = []
        result = []
        for word in important_words:
            meme_list.append(get_meme_urls(word))
        for i in range(len(meme_list)):
            for url in meme_list[i]:
                result.append(url)
        l = []
        output = {"response": 'success',"meme_urls": result}
        l.append(output)
        return Response(json.dumps(l))
    else:
        print(request.method)
        return jsonify({"code": 500, "message": "Not working"})


if __name__ == '__main__':
    app.run(debug=True)
