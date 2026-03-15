"""Create a Max patch that reroutes csv data through makenote."""

import maxpylang as mp

patch = mp.MaxPatch(load_file="tester2.maxpat")

for obj in patch.objs.values():
    if obj.name == "makenote":
        makenote = obj
        break

csv = patch.place("csvReader")[0]
toggle = patch.place("toggle")[0]

patch.connect(
    (csv.outs[0], makenote.ins[1]),
    (csv.outs[1], makenote.ins[2]),
    (toggle.outs[0], csv.ins[0]),
)

patch.save("tester2-edited.maxpat")
