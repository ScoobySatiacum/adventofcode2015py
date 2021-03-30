import hashlib

m = hashlib.md5()
m.update(b'bgvyzdsv')
print(m.hexdigest())