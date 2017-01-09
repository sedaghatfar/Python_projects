
import string
import re
import requests
import json
from PIL import ImageFont

# valid text reference
sefariaRef="Mishnah_Berakhot.1.1" 


#set some more variables.
fontSize = 10
fontDrawSize = 18
font = ImageFont.truetype("MiriamMonoCLM-Book.ttf", fontDrawSize)
sampleDensity=1


def lookup(sefariaRef):
    #text input    
    url = 'http://www.sefaria.org/api/texts/'+sefariaRef
    params = dict(
    	commentary=0,
    	context=0
    )
    resp = requests.get(url=url, params=params)
        
    data = json.loads(resp.text)
     

    text = json.dumps(data['he']).decode('unicode-escape')
    eng = json.dumps(data['text']).decode('unicode-escape')    
    text = text.replace(u"\u05BE"," ")
    exclude = set(string.punctuation+u"\uFEFF"+"\n")
    text = ''.join(char for char in text if char not in exclude)
    strip_cantillation_vowel_regex = re.compile(ur"[^\u05d0-\u05f4\s]", re.UNICODE)
    text = strip_cantillation_vowel_regex.sub('', text)
    eng = eng.replace("<i>", "")
    eng = eng.replace("</i>", "")
    
    print '\n'    
    print text
    print '\n'
    print eng

if __name__ == '__main__':	
	lookup("Mishnah_Berakhot.1.1")
