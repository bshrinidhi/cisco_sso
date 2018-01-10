import json

def json_analyse(data):

    #data = json.load(open('data.json'))
    devices = data['network']['devices']

    #iterate over the devices list
    for device in devices:
        #process every interface
        for interface in device['interfaces']:
            broadcast = interface['broadcasts']
            packet = interface['input_packets']

            if packet != 0:
                interface['broadcast_percent'] = float("{0:.2f}".format((broadcast/packet)*100))
            else:
                interface['broadcast_percent'] = 0


    #Dump the dictionary into JSON
    with open('data_a.json', 'w') as fp:
        json.dump(data, fp, indent=3)