from bitarray import bitarray
import hashlib

class BitMap:
	"""BitMap"""
	def __init__(self, size):
		self.size = size
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)

	def hash(self, s):
		return int(hashlib.sha1(s.encode()).hexdigest(), 16) % self.size

	def add(self, s):
		key = self.hash(s)
		self.bit_array[key] = 1

	def lookup(self, s):
		key = self.hash(s)
		if self.bit_array[key] == 0:
			return 'Nope'
		return 'Probably'


bm = BitMap(5000000)		
bm.add('Ozil')
print(bm.lookup('Ozil'))
bm.add('Rashford')
print(bm.lookup('Rashford'))
print(bm.lookup('Henry'))