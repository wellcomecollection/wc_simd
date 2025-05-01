#!/usr/bin/env python3
import json
import sys

if len(sys.argv) != 2:
    print("Usage: python find_big_by_exec_count.py notebook.ipynb")
    sys.exit(1)

path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

sizes = []
for cell in nb.get('cells', []):
    if cell.get('cell_type') != 'code':
        continue
    exec_count = cell.get('execution_count')
    # skip cells never run
    if exec_count is None:
        continue
    raw = json.dumps(cell, ensure_ascii=False)
    sizes.append((exec_count, len(raw)))

# sort descending by size
for count, sz in sorted(sizes, key=lambda x: x[1], reverse=True)[:10]:
    print(f"Cell [{count:>3}]: {sz / 1024:8.2f} KB")
