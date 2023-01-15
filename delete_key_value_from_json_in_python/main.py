import json
with open('states1.json') as f:
  data = json.load(f)
for state in data['states']:
  del state['area_codes']
with open('new_states1.json', 'w') as f:
  json.dump(data, f, indent=2)
  
  #output
  Process finished with exit code 0
