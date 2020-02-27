import json
import os

# loading data of the file 
with open('data.json') as f:
  data = json.load(f)

# converting dictionary format to command format
packages = []
for k,v in data.items():
  temp = k+'=='+v
  packages.append(temp)

# applying pip install on each package and returning whether installed successfully or not
for i in packages:
  cmd = 'pip install -q '+i
  value = os.system(cmd)
  if value == 0:
    print(i," successfully installed")
  else:
    print(i," not installed")
