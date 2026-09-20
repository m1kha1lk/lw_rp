from pathlib import Path
import json
bow_name=Path(__file__).parent.name
# print(bow_name)
crossbow_parent_template={
    "parent": 'minecraft:item/crossbow',
    'textures': {
        'layer0': ''
    }
}

# crossbow_names=[ f'{bow_name}_crossbow_standby', f'{bow_name}_crossbow_pulling_0', f'{bow_name}_crossbow_pulling_1', f'{bow_name}_crossbow_pulling_2' ]
with open(f'{bow_name}_crossbow.json', 'w') as f:
    tmp=crossbow_parent_template.copy()
    tmp["textures"]["layer0"]=f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_standby"
    json.dump(tmp, f, indent=2)
with open(f'{bow_name}_crossbow_arrow.json', 'w') as f:
    tmp=crossbow_parent_template.copy()
    tmp["textures"]["layer0"]=f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_arrow"
    json.dump(tmp, f, indent=2)
with open(f'{bow_name}_crossbow_firework.json', 'w') as f:
    tmp=crossbow_parent_template.copy()
    tmp["textures"]["layer0"]=f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_firework"
    json.dump(tmp, f, indent=2)

for i in range(0, 3):
    with open(f'{bow_name}_crossbow_pulling_{i}.json', 'w') as f:
        temp_skeleton=crossbow_parent_template.copy()
        temp_skeleton["parent"]= f"minecraft:item/crossbow_pulling_{i}"
        temp_skeleton["textures"]["layer0"]=f"new_format:item/armorsets/{bow_name}/{bow_name}_crossbow_pulling_{i}"
        json.dump(temp_skeleton, f, indent=2)
