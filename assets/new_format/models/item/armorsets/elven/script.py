from pathlib import Path
import json
bow_name=Path(__file__).parent.name
# print(bow_name)
format = {
  "model": {
    "type": "minecraft:condition",
    "on_false": {
      "type": "minecraft:model",
      "model": "minecraft:item/bow"
    },
    "on_true": {
      "type": "minecraft:range_dispatch",
      "entries": [
        {
          "model": {
            "type": "minecraft:model",
            "model": "minecraft:item/bow_pulling_1"
          },
          "threshold": 0.65
        },
        {
          "model": {
            "type": "minecraft:model",
            "model": "minecraft:item/bow_pulling_2"
          },
          "threshold": 0.9
        }
      ],
      "fallback": {
        "type": "minecraft:model",
        "model": "minecraft:item/bow_pulling_0"
      },
      "property": "minecraft:use_duration",
      "scale": 0.05
    },
    "property": "minecraft:using_item"
  }
}
bow_skeleton={
    "parent": "minecraft:item/bow",
    "textures": {
        "layer0": f"new_format:item/armorsets/{bow_name}"
     }
}

with open(f'{str(bow_name)}_bow.json', 'w') as f:
    tmp=bow_skeleton.copy()
    tmp["textures"]["layer0"]=f"new_format:item/armorsets/{str(bow_name)}/{bow_name}"
    json.dump(tmp, f, indent=2)

for i in range(0, 3):
    with open(f'{str(bow_name)}_bow_pulling_{i}.json', 'w') as f:
        temp_skeleton=bow_skeleton.copy()
        temp_skeleton["parent"]= f"minecraft:item/bow_pulling_{i}"
        temp_skeleton["textures"]["layer0"]=f"new_format:item/armorsets/{str(bow_name)}/{bow_name}_bow_pulling_{i}"
        json.dump(temp_skeleton, f, indent=2)
