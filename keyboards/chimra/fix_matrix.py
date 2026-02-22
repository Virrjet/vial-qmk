import json
import sys

# Update keyboard.json
with open("keyboard.json", "r") as f:
    data = json.load(f)

data["matrix_size"] = {"rows": 10, "cols": 7}

for item in data["layouts"]["LAYOUT"]["layout"]:
    m = item["matrix"]
    row, col = m[0], m[1]
    if col >= 7:
        item["matrix"] = [row + 5, col - 7]

with open("keyboard.json", "w") as f:
    json.dump(data, f, indent=4)

# Update vial.json
with open("keymaps/vial/vial.json", "r") as f:
    vdata = json.load(f)

vdata["matrix"] = {"rows": 10, "cols": 7}

for key_layer in vdata["layouts"]["keymap"]:
    for item in key_layer:
        if "matrix" in item:
            m = item["matrix"]
            row, col = m[0], m[1]
            if col >= 7:
                item["matrix"] = [row + 5, col - 7]

with open("keymaps/vial/vial.json", "w") as f:
    json.dump(vdata, f, indent=4)

