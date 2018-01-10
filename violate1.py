#script to get violated info

import json

def json_violate(data):
  #with open('data_c.json') as json_file:
       # data = json.load(json_file)
        #print(data)
        #update={}
        #update['violation']
    interface_data=data['network']['devices'][0]['interfaces']
    print(interface_data)
    for p in interface_data:
        if p['broadcast_percent']>=0 and p['broadcast_percent']<=15:
                p['violation_color']='green'
        elif (p['broadcast_percent']>15 and p['broadcast_percent']<=30):
                p['violation_color']='yellow'
        else:
                p['violation_color']='red'

    print(data)
    with open('data_v.json','w') as fp:
        json.dump(data,fp,indent=4)
    return




    

