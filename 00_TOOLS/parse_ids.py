#!/usr/bin/env python3
import re

# Read the txt file
with open('/Users/marcelgaertner/Desktop/Projekte/dekota/00_TOOLS/ID_lebensmittel.txt', 'r') as f:
    content = f.read()

# Split by lines
lines = [l.strip() for l in content.split('\n') if l.strip()]

# Parse ID and Name pairs
products = {}
i = 0
while i < len(lines):
    if lines[i].isdigit():
        id_num = lines[i]
        # Skip empty lines or non-name entries
        j = i + 1
        while j < len(lines) and (lines[j] == '' or lines[j].isdigit() or lines[j] in ['Document ID', 'gastro_id', 'id', 'name']):
            j += 1
        if j < len(lines) and lines[j].startswith('"') and lines[j].endswith('"'):
            name = lines[j].strip('"')
            products[id_num] = name
            i = j + 1
        else:
            i += 1
    else:
        i += 1

# Sort by ID
sorted_products = sorted(products.items(), key=lambda x: int(x[0]))

# Output as clean list
with open('/Users/marcelgaertner/Desktop/Projekte/dekota/00_TOOLS/produkt_id_mapping.txt', 'w') as f:
    for id_num, name in sorted_products:
        f.write(f"{id_num}: {name}\n")

print(f"Extracted {len(products)} products!")
