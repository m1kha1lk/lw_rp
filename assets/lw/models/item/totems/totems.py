import json
list_ =  """3nedeli.png
4ort.png
BaNaN4.png
Bleak_Hawk.png
dapte.png
dipxi.png
Egorizik.png
Gay.png
killside.png
mashroow.png
mellon16.png
misha.png
POP_HAUS__.png
saldatic.png
sparki.png
vertix.png
Yanda_.png""".replace(".png", '').split("\n")
# print(list_)
cases=[]
for i in list_:
    with open(f'{i.lower()}.json', 'w') as f:
        skeleton={
            "parent": "minecraft:item/generated",
            "textures":{
                "layer0": f"lw:item/totems/{i.lower()}"
            }
        }
        json.dump(skeleton, f, indent=2)
    cases.append({
        "when": i,
        "model": {
            "type": "minecraft:model",
            "model": f"lw:item/totems/{i.lower()}"
        }
    })
print(json.dumps(cases, indent=2))
    