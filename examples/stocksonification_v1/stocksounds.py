"""Replace qualifying random objects with stocksounds abstractions."""

import maxpylang as mp

patch = mp.MaxPatch(load_file="mcfm.maxpat")

# create a smaller dictionary, only holding "random"
# objects that will be replaced with "stocksounds" abstraction patch
SELECTIVE_RANDOM_LIMIT = 10
replace = {
    obj_num: obj
    for obj_num, obj in patch.objs.items()
    if obj.name == "random" and int(obj.args[0]) > SELECTIVE_RANDOM_LIMIT
}

# loop through dict of all "random objects" and replace with abstraction patch
for obj_num in replace:
    patch.replace(obj_num, "stocksounds", retain=True, verbose=True)

patch.save("stockSonification.maxpat")
