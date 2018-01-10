#Main driver file.
import json
#import violate,analyse
def assessment():
    with open('data.json') as json_data:
        data=json.load(json_data)
        print(data)
    analyse.json_analyse(data)
    with open('data_a') as json_data:
        data_a=json.load(json_data)
    violate.json_violate(data_a)
    with open('data_v') as json_data:
        data_v=json.load(json_data)
        print(data_v)
assessment()