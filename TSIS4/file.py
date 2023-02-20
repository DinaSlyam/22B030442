import json

file = open ("sampledata.json", "r")
sampledata = file.read()
file.close()

imdata = json.loads(sampledata)

print(imdata['imdata'][0]['l1PhysIf']['attributes']['dn'], imdata['imdata'][0]['l1PhysIf']['attributes']['mtu'], imdata['imdata'][0]['l1PhysIf']['attributes']['speed'] )
print(imdata['imdata'][1]['l1PhysIf']['attributes']['dn'], imdata['imdata'][1]['l1PhysIf']['attributes']['mtu'], imdata['imdata'][1]['l1PhysIf']['attributes']['speed'] )
print(imdata['imdata'][2]['l1PhysIf']['attributes']['dn'], imdata['imdata'][2]['l1PhysIf']['attributes']['mtu'], imdata['imdata'][2]['l1PhysIf']['attributes']['speed'] )
