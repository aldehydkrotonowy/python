import json
from pprint import pprint

# read file
with open('scikit-learn/WIG20-candlestick.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)

pprint("url: " + str(obj['main'][0]))
pprint("url: " + str(len(obj['main'])))
pprint(obj['profileData'])
