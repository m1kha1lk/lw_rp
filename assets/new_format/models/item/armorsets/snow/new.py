import json
names = [ 'elven', 'energy', 'snow']

cases=[]
for name in names:
    cases.append(
        {
  "when": name,
  "model": {
    "type": "minecraft:condition",
    "on_false": {
      "type": "minecraft:model",
      "model": f"new_format:item/armorsets/{name}/{name}_bow"
    },
    "on_true": {
      "type": "minecraft:range_dispatch",
      "entries": [
        {
          "model": {
            "type": "minecraft:model",
            "model": f"new_format:item/armorsets/{name}/{name}_bow_pulling_1"
          },
          "threshold": 0.65
        },
        {
          "model": {
            "type": "minecraft:model",
            "model": f"new_format:item/armorsets/{name}/{name}_bow_pulling_2"
          },
          "threshold": 0.9
        }
      ],
      "fallback": {
        "type": "minecraft:model",
        "model": f"new_format:item/armorsets/{name}/{name}_bow_pulling_0"
      },
      "property": "minecraft:use_duration",
      "scale": 0.05
    },
    "property": "minecraft:using_item"
  }
}
    )
print(json.dumps(cases, indent=2))