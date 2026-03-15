"""Create a randomized oscillator-driven polyphonic test patch."""

import maxpylang as mp

patch = mp.MaxPatch()

# Objects
num_notes = 12

tg = patch.place("toggle", num_objs=1, starting_pos=[0, -1])[0]
multislider = patch.place("multislider", num_objs=1, starting_pos=[0, 100])[0]

unpack_helper = "unpack"
for _i in range(num_notes):
    unpack_helper += " 0."
unp = patch.place(unpack_helper, num_objs=1, starting_pos=[0, 250])[0]

mtr = patch.place("metro 100", num_objs=num_notes, starting_pos=[0, 315])
rnd = patch.place("random 500", num_objs=num_notes, starting_pos=[0, 345])
add = patch.place("+ 500", num_objs=num_notes, starting_pos=[0, 375])
num = patch.place("number", num_objs=num_notes, starting_pos=[0, 405])
cyc = patch.place("cycle~ ", num_objs=num_notes, starting_pos=[0, 435])
met = patch.place("meter~ ", num_objs=num_notes, starting_pos=[0, 487])
gn = patch.place("gain~ ", num_objs=num_notes, starting_pos=[0, 505])


mult = patch.place("*~ 0.05", num_objs=1, starting_pos=[0, 665])[0]
ez = patch.place("ezdac~ ", num_objs=1, starting_pos=[0, 700])[0]

# Connection
patch.connect([multislider.outs[0], unp.ins[0]])

for m, r in zip(mtr, rnd):
    patch.connect([m.outs[0], r.ins[0]])

for r, a in zip(rnd, add):
    patch.connect([r.outs[0], a.ins[0]])

for a, n in zip(add, num):
    patch.connect([a.outs[0], n.ins[0]])

for n, c in zip(num, cyc):
    patch.connect([n.outs[0], c.ins[0]])

for c, g in zip(cyc, gn):
    patch.connect([c.outs[0], g.ins[0]])

for g, m in zip(gn, met):
    patch.connect([g.outs[0], m.ins[0]])

for gain in gn:
    patch.connect([gain.outs[0], mult.ins[0]])

for metro_obj in mtr:
    patch.connect([tg.outs[0], metro_obj.ins[0]])

patch.connect([mult.outs[0], ez.ins[0]])
patch.connect([mult.outs[0], ez.ins[1]])

for index, gain in enumerate(gn):
    patch.connect([unp.outs[index], gain.ins[0]])


patch.save("tester3.maxpat")
