import ast, sys, json, collections
src = open(sys.argv[1], encoding="utf-8").read()
tree = ast.parse(src)
dtc = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "DTC":
        dtc = ast.literal_eval(node.value)
json.dump(dtc, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False)
print(len(dtc)); print(collections.Counter(k[:2] for k in dtc).most_common(20))
for k in ["P0010","P0300","P0420","P0171","P060A","U0100","C0035","B0001","P2101","P0700"]: print(k, "|", dtc.get(k))
words = collections.Counter(w.strip('(),/"').lower() for v in dtc.values() for w in v.split())
print(len(words)); print([w for w,_ in words.most_common(140)])
