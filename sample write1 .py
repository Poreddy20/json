import json
data = [
    {"emp id ":21,"age":22,"name":"mno"}
    ]
with open ('write 1.json','w') as file:
    json.dump(data,file,indent=4)
