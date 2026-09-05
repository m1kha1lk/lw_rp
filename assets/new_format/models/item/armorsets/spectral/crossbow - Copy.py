# from pathlib import Path
import json
# bow_name=Path(__file__).parent.name
# print(bow_name)
crossbow_parent_template={
    "parent": 'minecraft:item/crossbow',
    'textures': {
        'layer0': ''
    }
}
cases = []
crossbow_names=["energy", "spectral", "elven"]
# crossbow_names=[ f'{bow_name}_crossbow_standby', f'{bow_name}_crossbow_pulling_0', f'{bow_name}_crossbow_pulling_1', f'{bow_name}_crossbow_pulling_2' ]
for bow_name in crossbow_names:
    cases.append(
        {
            "when": bow_name,
            "model": {
    "type": "minecraft:select",
    "cases": [
      {
        "model": {
          "type": "minecraft:model",
          "model": f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_arrow"
        },
        "when": "arrow"
      },
      {
        "model": {
          "type": "minecraft:model",
          "model": f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_firework"
        },
        "when": "rocket"
      }
    ],
    "fallback": {
      "type": "minecraft:condition",
      "on_false": {
        "type": "minecraft:model",
        "model": f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow"
      },
      "on_true": {
        "type": "minecraft:range_dispatch",
        "entries": [
          {
            "model": {
              "type": "minecraft:model",
              "model": f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_pulling_1"
            },
            "threshold": 0.58
          },
          {
            "model": {
              "type": "minecraft:model",
              "model": f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_pulling_2"
            },
            "threshold": 1
          }
        ],
        "fallback": {
          "type": "minecraft:model",
          "model": f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_pulling_0"
        },
        "property": "minecraft:crossbow/pull"
      },
      "property": "minecraft:using_item"
    },
    "property": "minecraft:charge_type"
            }
        }
    )

print(json.dumps(cases, indent=2))
# with open(f'{bow_name}_crossbow.json', 'w') as f:
#     tmp=crossbow_parent_template.copy()
#     tmp["textures"]["layer0"]=f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_standby"
#     json.dump(tmp, f, indent=2)
# with open(f'{bow_name}_crossbow_arrow.json', 'w') as f:
#     tmp=crossbow_parent_template.copy()
#     tmp["textures"]["layer0"]=f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_arrow"
#     json.dump(tmp, f, indent=2)
# with open(f'{bow_name}_crossbow_firework.json', 'w') as f:
#     tmp=crossbow_parent_template.copy()
#     tmp["textures"]["layer0"]=f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_firework"
#     json.dump(tmp, f, indent=2)

# for i in range(0, 3):
#     with open(f'{bow_name}_crossbow_pulling_{i}.json', 'w') as f:
#         temp_skeleton=crossbow_parent_template.copy()
#         temp_skeleton["parent"]= f"minecraft:item/crossbow_pulling_{i}"
#         temp_skeleton["textures"]["layer0"]=f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_pulling_{i}"
#         json.dump(temp_skeleton, f, indent=2)
