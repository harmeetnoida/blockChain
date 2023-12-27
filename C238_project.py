import hashlib

filename = "MESSI.jpg"

with open(filename, "rb") as f:
	fila_data = f.read()

image_hash = hashlib.sha3_256(fila_data)
print(image_hash.hexdigest())