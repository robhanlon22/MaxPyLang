"""Create a MIDI note selector patch with counter routing."""

import maxpylang as mp

patch = mp.MaxPatch()

# Objects (titled abbreviation of object name)
num_notes = 10
toggle_position = num_notes * 80 + 100
tg = patch.place("toggle", num_objs=num_notes, starting_pos=[0, 100])
gt = patch.place("gate", num_objs=num_notes, starting_pos=[0, 200])
btn = patch.place("button", num_objs=num_notes, starting_pos=[0, 300])

rnd = patch.place("random 120", num_objs=1, starting_pos=[0, 400])[0]
num = patch.place("number", num_objs=1, starting_pos=[0, 500])[0]
mn = patch.place("makenote 100 100 2", num_objs=1, starting_pos=[0, 600])[0]
no = patch.place("noteout int 1", num_objs=1, starting_pos=[0, 700])[0]

tg2 = patch.place("toggle", num_objs=1, starting_pos=[toggle_position, 100])[0]
mtr = patch.place("metro 100", num_objs=1, starting_pos=[toggle_position, 150])[0]
cnt = patch.place(
    f"counter {num_notes} 1", num_objs=1, starting_pos=[toggle_position, 200]
)[0]
num2 = patch.place("number", num_objs=1, starting_pos=[toggle_position, 250])[0]

# creating a sel object to filter counter signals for each num notes value
sel_helper = "sel "
for index in range(1, num_notes + 1):
    sel_helper += str(index)
    sel_helper += " "
sel = patch.place(sel_helper, num_objs=1, starting_pos=[toggle_position, 300])[0]

# Connecting objects
for toggle_obj, gate_obj in zip(tg, gt):
    patch.connect([toggle_obj.outs[0], gate_obj.ins[0]])

for gate_obj, btn_obj in zip(gt, btn):
    patch.connect([gate_obj.outs[0], btn_obj.ins[0]])

for gate_obj, btn_obj in zip(gt, btn):
    patch.connect([gate_obj.outs[0], btn_obj.ins[0]])

for btn_obj in btn:
    patch.connect([btn_obj.outs[0], rnd.ins[0]])

patch.connect([rnd.outs[0], num.ins[0]])
patch.connect([num.outs[0], mn.ins[0]])
patch.connect([mn.outs[0], no.ins[0]])
patch.connect([mn.outs[1], no.ins[1]])

patch.connect([tg2.outs[0], mtr.ins[0]])
patch.connect([mtr.outs[0], cnt.ins[0]])
patch.connect([cnt.outs[0], num2.ins[0]])
patch.connect([num2.outs[0], sel.ins[0]])

for index, gate_obj in enumerate(gt):
    patch.connect([sel.outs[index], gate_obj.ins[1]])

patch.save("tester2.maxpat")
