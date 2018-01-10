#script to get violated info
import json

#json_data = json.load(open('data.json','r'))
def json_violate(json_data):
    interface_list = json_data['network']['devices'][0]['interfaces']
    for e,x in enumerate(interface_list):
        value = x['broadcast_percent']
        if value < 16: # <16
            interface_list[e]["violation"] = "green"
        elif value < 30: #>15 and <30
            interface_list[e]["violation"] = "yellow"
        else: #>30
            interface_list[e]["violation"] = "red"

    json_data['network']['devices'][0]['interfaces'] = interface_list

    #writing the new json data to the new file 'data_v.json'
    with open('data_v.json', 'w') as file:
        json.dump(json_data, file)