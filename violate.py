import json
def json_violate(data):
    for network in data:
        for node_list in data[network].items():
            for devices in  node_list[1::]:
                for each_device in devices:
                    for each_interface in each_device['interfaces']:
                        bp = each_interface['broadcast_percent']
                        if bp<16:
                            each_interface['violation']="green"
                        elif bp<30:
                            each_interface['violation']="yellow"
                        else:
                            each_interface['violation']="red"
    with open("data_v.json",'w') as outf:
        json.dump(data,outf,indent=4)