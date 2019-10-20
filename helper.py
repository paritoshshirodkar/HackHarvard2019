
import html2text
import string
import re
import urllib,json
import urllib.request

def remove_punctuation(text):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    return regex.sub('',text)

def load_english_words():
    with open('/rodrigueskevin2/HeackHarvard2019/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().lower().split())
    
    return valid_words

def load_stop_words():
    with open('/rodrigueskevin2/HeackHarvard2019/stop_words.txt') as word_file:
        valid_words = set(word_file.read().lower().split())
    
    return valid_words

def clean_html(text):
    h = html2text.HTML2Text()
    text_from_html = h.handle(text)
    
    return text_from_html


def give_top_words(text):
    

    text_from_html = clean_html(text)
    
    clean_text = remove_punctuation(text_from_html)
    #print(clean_text)
    
    words = clean_text.lower().split()
    
    english_words = {}
    
        
    
            
    english_words = load_english_words()
    stop_words = load_stop_words()
    
              
    # demo print
    
    cleaned_words = {}
    for word in words:
        if word in english_words and word not in stop_words:
            cleaned_words[word] = cleaned_words.get(word, 0) + 1
            
    tf_list = []
    for k,v in cleaned_words.items():
        tf_list.append((v,k))
        
    tf_list.sort(reverse = True) 
    
    top_5_words = [x[1] for x in tf_list[:5]]
    
    return top_5_words


def get_meme_urls(search_term):
    search_term = search_term.replace(' ', '+')
    data = json.loads(urllib.request.urlopen(
        "http://api.giphy.com/v1/gifs/search?q=" + search_term + "&api_key=Dz1Ij8dpmMBrMy9Ayxmte4vUQifziIZf&limit=5").read())
    result = json.dumps(data, sort_keys=True, indent=4)
    r = []
    gifs = json.loads(result)
    for i in range(5):
        gif = gifs['data'][i]['images']
        gif = gif['looping']['mp4']
        r.append(gif)
    return r


    
