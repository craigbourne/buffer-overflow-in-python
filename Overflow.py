"""This demonstrates a buffer overflow attempt in Python."""

buffer=[None]*10
for i in range(0,14):
    buffer[i]=7

print(buffer)
