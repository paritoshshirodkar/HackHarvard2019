from flask import Flask, request, jsonify
import pandas as pd
import json
import os
import urllib, json
import urllib.request
import html2text
from helper import give_top_words, get_meme_urls
app = Flask(__name__)


@app.route('/meme_generator', methods=['GET', 'POST'])
def meme_generator():
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

        result = {
            "response": 'success',
            "meme_urls": result
        }
        return (jsonify(result), 200)


if __name__ == '__main__':
    app.run(debug=True)