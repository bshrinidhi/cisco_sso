import json

data = json.load(open('C:/Users/samalagi/Assignment/cisco_sso/data.json'))
network = data['network']
devices = network['devices']

for device in devices:
    for interface in device['interfaces']:
        broadcast = interface['broadcasts']
        packet = interface['input_packets']
        if packet != 0:
            interface['broadcast_percent'] = broadcast/packet

print(data)
with open('data_a.json', 'w') as fp:
    json.dump(data, fp, indent=4)

