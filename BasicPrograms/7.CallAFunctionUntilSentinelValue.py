from functools import partial
#Call a function until a sentinel value
blocks=list()
f=23.3
for block in iter(partial(f.read,32),''):
    blocks.append(block)

print(blocks)
