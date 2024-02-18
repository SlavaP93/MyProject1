import hashlib
import mmh3
data = "Hello"
hash_value = mmh3.hash(data)
print(hash_value)  # Выводит хеш-значение MurmurHash



data = "Hello, World!"
hash_object = hashlib.sha256(data.encode())
hex_digest = hash_object.hexdigest()
print(hex_digest) # Выводит хеш-значение SHA-256
