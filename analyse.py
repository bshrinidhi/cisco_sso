import json
def json_analyse(data):
    for network in data:
        for node_list in data[network].items():
            for devices in  node_list[1::]:
                for each_device in devices:
                    for each_interface in each_device['interfaces']:
                        broadcast=each_interface['broadcasts']
                        ip=each_interface['input_packets']
                        if ip>0:
                            bp=(broadcast/ip)*100
                        else:
                            bp=(broadcast/1.0)*100
                        bp=round(bp,2)
                        each_interface['broadcast_percent']=bp
    with open("data_a.json",'w') as outf:
        json.dump(data,outf,indent=4)

