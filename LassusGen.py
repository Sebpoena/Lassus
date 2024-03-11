import random

class Interval:
	def __init__(self, name, worth):
		self.name = name
		self.worth = worth
		self.values = []
		self.total = 0
		self.weights = []
		self.reference = []
		
		
	def setArguments(self, list):
		self.values = list
		if len(list) > 1:
			self.total = sum(self.values)
		else:
			self.total = list[0]
		self.weights = [round(i/self.total, 5) for i in self.values]
		
		
	def calculateNextInterval(self):
		a = random.choices(self.reference, self.weights)
		return a
		
		
	def ambitusRestrictedInterval(self, command):
		if command > 0:
			tempReference = [i for i in self.reference if i.worth < 0]
			tempIndex = [self.reference.index(i) for i in tempRefence]
			tempWeights = [self.weights[i] for i in tempIndex]
		else:
			tempReference = [i for i in self.reference if i.worth > 0]
			tempIndex = [self.reference.index(i) for i in tempRefence]
			tempWeights = [self.weights[i] for i in tempIndex]
		a = random.choices(tempReference, tempWeights)
		return a
		
	
	def setReference(self, list):
		self.reference = list
		
		
	def __repr__(self):
		return self.name

	
class modalScale:
	def __init__(self, name, basis, key, options):
		self.name = name
		self.key = key
		self.basis = basis
		self.options = options
		self.scale = [(i + self.key) for i in range(116) if i % 12 in self.basis]
		self.optionsByStep = []
		
		
	def modulate(self, newKey):
		self.key = newKey
		self.scale = [(i + self.key) for i in range(116) if i % 12 in self.basis]
		return None
		
		
	def degree(self, note):
		if note in self.scale:
			return self.scale.index(note)
		elif (note + 1) in self.scale:
			print("inexact: + 1")
			return self.scale.index(note + 1)
		elif (note - 1) in self.scale:
			print("inexact: - 1")
			return self.scale.index(note - 1)
		else:
			return none
		
	
	def stepWiseOptions(self, options, step):
		optionsInScale = [i for i in options if step + i.worth in self.scale]
		return tuple(optionsInScale)
		
		
	def setOptionsByStep(self, options):
		self.optionsByStep = options
	
	
	def setSetter(self, setter):
		self.setter = setter
		
		
	def setScaleArguments(self):
		self.setter.set()
	
		
	def __repr__(self):
		return self.name
		
		
class Setter:
	def __init__(self, mode, values, reference):
		self.mode = mode
		self.reference = reference
		self.values = values
		X.setArguments((1,))
		X.setReference((P1,))
		R.setArguments((1,))
		R.setReference((P1,))
		
		
	def set(self,):
		for i, j in enumerate(self.mode.options):
			j.setArguments(self.values[i])
			j.setReference(self.reference[i])
		

P1 = Interval('P1', 0)
m2_auf = Interval('m2_auf', 1)
m2_ab = Interval('m2_ab', -1)
M2_auf = Interval('M2_auf', 2)
M2_ab = Interval('M2_ab', -2)
m3_auf = Interval('m3_auf', 3)
m3_ab = Interval('m3_ab', -3)
M3_auf = Interval('M3_auf', 4)
M3_ab = Interval('M3_ab', -4)
d4_auf = Interval('d4_auf', 4)
P4_auf = Interval('P4_auf', 5)
P4_ab = Interval('P4_ab', -5)
A4_auf = Interval('A4_auf', 6)
P5_auf = Interval('P5_auf', 7)
P5_ab = Interval('P5_ab', -7)
m6_auf = Interval('m6_auf', 8)
M6_auf = Interval('M6_auf', 9)
P8_auf = Interval('P8_auf', 12)
P8_ab = Interval('P8_ab', -12)
R = Interval('R', 0)
X = Interval('X', 0)
		
Dorian = modalScale('Dorian', (0, 2, 3, 5, 7, 9, 10), 0, (P1, m2_auf, m2_ab, M2_auf, M2_ab, m3_auf, m3_ab, M3_auf, M3_ab, d4_auf, P4_auf, P4_ab, P5_auf, P5_ab, m6_auf, M6_auf, P8_auf, P8_ab))
Ionian = modalScale('Ionian', (0, 2, 4, 5, 7, 9, 11), 0, (P1, m2_auf, m2_ab, M2_auf, M2_ab, m3_auf, m3_ab, M3_auf, M3_ab, d4_auf, P4_auf, P4_ab, P5_auf, P5_ab, m6_auf, P8_auf, P8_ab))
Phrygian = modalScale('Phrygian', (0, 1, 3, 5, 7, 8, 10), 0, (P1, m2_auf, m2_ab, M2_auf, M2_ab, m3_auf, m3_ab, M3_auf, M3_ab, d4_auf, P4_auf, P4_ab, P5_auf, P5_ab, m6_auf, P8_auf, P8_ab))
Lydian = modalScale('Lydian', (0, 2, 4, 6, 7, 9, 11), 0, (P1, m2_auf, m2_ab, M2_auf, M2_ab, m3_auf, m3_ab, M3_auf, M3_ab, P4_auf, P4_ab, P5_auf, P5_ab, m6_auf, P8_auf, P8_ab))
Mixolydian = modalScale('Mixolydian', (0, 2, 4, 5, 7, 9, 10), 0, (P1, m2_auf, m2_ab, M2_auf, M2_ab, m3_auf, m3_ab, M3_auf, M3_ab, d4_auf, P4_auf, P4_ab, P5_auf, P5_ab, A4_auf, m6_auf, P8_auf, P8_ab))
Aeolian = modalScale('Aeolian', (0, 2, 3, 5, 7, 8, 10), 0, (P1, m2_auf, m2_ab, M2_auf, M2_ab, m3_auf, m3_ab, M3_auf, M3_ab, P4_auf, P4_ab, P5_auf, P5_ab, m6_auf, P8_auf, P8_ab))
	
DorianSetter = Setter(Dorian, ((147, 139, 118, 105, 66, 55, 42, 35, 34, 29, 23, 23, 16, 14, 6, 6, 1), (238, 158, 91, 72, 66, 60, 29, 27, 24, 14, 9, 9, 7, 7, 4), (518, 200, 87, 63, 34, 29, 28, 25, 12, 9, 9, 8, 3, 3, 1, 1), (403, 321, 204, 88, 64, 59, 47, 39, 27, 18, 17, 11, 8, 7, 7, 7, 3), (331, 331, 317, 123, 108, 84, 46, 32, 26, 26, 24, 16, 9, 9, 5, 3, 1, 1), (129, 84, 64, 30, 19, 14, 7, 3, 3, 3, 2, 1, 1), (70, 66, 57, 32, 26, 23, 16, 14, 10, 9, 7, 6, 3, 2), (41, 19, 19, 9, 8, 8, 6, 5, 3, 2, 2, 1), (44, 37, 23, 18, 15, 14, 8, 6, 2, 1, 1), (3, 3, 2, 2, 2, 1, 1, 1), (62, 54, 27, 21, 20, 12, 8, 6, 5, 3, 3, 3, 2, 1), (53, 31, 29, 25, 17, 14, 10, 7, 7, 6, 5, 4, 3, 3, 2, 1, 1), (23, 16, 14, 11, 10, 8, 8, 7, 7, 6, 5, 5, 4, 1, 1), (43, 28, 27, 19, 15, 15, 13, 10, 8, 8, 7, 7, 6, 4, 2, 1), (24, 9, 6, 3, 1, 1, 1, 1), (1,), (15, 15, 8, 5, 3, 3, 1), (9, 6, 4, 3, 3, 2, 2, 2, 1)), ((M2_ab, P1, m2_ab, M2_auf, m3_auf, m2_auf, P4_ab, m3_ab, P5_ab, M3_ab, P5_auf, P4_auf, R, M3_auf, P8_auf, m6_auf, P8_ab), (m2_ab, M2_auf, m3_ab, P1, R, P4_ab, M3_auf, X, P5_ab, m3_auf, M2_ab, P8_ab, P5_auf, M3_ab, P4_auf), (M2_ab, m2_auf, P1, R, P4_auf, M3_ab, m3_auf, P5_ab, X, P8_auf, m6_auf, d4_auf, P4_ab, M2_auf, P5_auf, m2_ab), (m2_auf, M2_auf, M2_ab, P1, R, P5_ab, M3_ab, P4_ab, m3_auf, m2_ab, P4_auf, m3_ab, P8_ab, d4_auf, X, P5_auf, m6_auf), (M2_auf, M2_ab, m2_ab, R, P1, m3_ab, P4_auf, P5_auf, m3_auf, M3_auf, X, P5_ab, P8_auf, P4_ab, m6_auf, M3_ab, P8_ab, m2_auf), (m2_ab, M2_auf, P1, m3_ab, P4_ab, M2_ab, M3_auf, P8_ab, R, P4_auf, P5_ab, m2_auf, m3_auf), (m3_auf, M2_ab, M2_auf, m2_auf, P1, P4_auf, P5_auf, M3_ab, m6_auf, R, P4_ab, m2_ab, P5_ab, P8_auf), (M2_ab, m2_auf, P1, M2_auf, P5_ab, M3_ab, P4_ab, P4_auf, m3_auf, R, m2_ab, P8_ab), (M2_auf, m2_ab, M3_auf, m3_ab, P1, R, P4_auf, P5_auf, M2_ab, P8_auf, P8_ab), (M3_auf, P1, P8_ab, R, m2_ab, m3_ab, M2_auf, P5_ab), (m2_ab, M2_ab, P1, m3_ab, M2_auf, P4_ab, X, R, M3_ab, P5_ab, M3_auf, m3_auf, P8_ab, m2_auf), (M2_auf, m2_auf, m3_auf, P1, R, P4_auf, m3_ab, P5_ab, m6_auf, M2_ab, P8_auf, m2_ab, M3_auf, M3_ab, P5_auf, X, P4_ab), (P1, M2_auf, M2_ab, m2_auf, m3_auf, m3_ab, R, P5_ab, M3_ab, m2_ab, P4_auf, P4_ab, P8_ab, M3_auf, X), (M2_auf, R, P4_auf, P1, P5_auf, m3_auf, P8_auf, X, m2_ab, M2_ab, M3_auf, m3_ab, m6_auf, m2_auf, P4_ab, M6_auf), (m2_ab, m3_ab, P1, P4_ab, P5_ab, R, M2_auf, M2_ab), (M2_ab,), (M2_ab, m2_ab, P5_ab, M3_ab, P1, P4_ab, P8_ab), (M2_auf, P4_auf, P5_auf, R, m2_auf, P1, M3_auf, m3_auf, P8_auf)))

IonianSetter = Setter(Ionian, ((38, 36, 33, 32, 25, 12, 10, 10, 9, 8, 7, 6, 6, 2, 1), (50, 45, 26, 25, 20, 16, 14, 7, 6, 5, 4, 2, 2, 1), (142, 52, 15, 11, 11, 9, 9, 6, 3, 2, 1, 1), (106, 81, 56, 32, 27, 21, 16, 13, 9, 9, 4, 4, 2, 2, 1, 1, 1), (121, 95, 85, 46, 26, 18, 18, 11, 11, 11, 9, 9, 7, 6), (34, 12, 10, 9, 7, 7, 6, 3), (26, 17, 16, 11, 10, 10, 7, 4, 3, 2, 2, 1, 1), (28, 14, 5, 4, 2, 1, 1, 1), (15, 8, 7, 7, 7, 3, 3, 2, 2, 1), (1,), (26, 21, 15, 8, 5, 5, 4, 3, 2, 1, 1, 1), (21, 11, 7, 6, 4, 4, 4, 3, 1, 1, 1, 1, 1, 1, 1), (10, 7, 7, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1), (12, 9, 8, 6, 6, 5, 5, 4, 4, 4, 3, 2, 1, 1), (4, 2, 2, 2, 1, 1, 1), (3, 2, 2, 2, 1, 1), (4, 2, 2, 2, 1)), ((M2_ab, M2_auf, m2_ab, P1, m3_ab, m2_auf, m3_auf, M3_ab, P4_auf, M3_auf, P5_ab, P5_auf, P4_ab, R, P8_ab), (m2_ab, M2_auf, R, P4_ab, m3_ab, P1, M3_auf, P8_ab, X, P5_ab, P5_auf, M3_ab, P4_auf, m3_auf), (M2_ab, m2_auf, R, P4_auf, m3_auf, M3_ab, P1, m6_auf, X, P5_ab, P8_ab, M2_auf), (m2_auf, M2_auf, M2_ab, P1, m3_auf, P5_ab, M3_ab, R, P4_auf, P4_ab, m3_ab, P5_auf, P8_ab, m6_auf, m2_ab, d4_auf, X), (M2_ab, M2_auf, m2_ab, R, P1, m3_ab, P4_auf, P5_auf, M3_auf, m3_auf, X, P5_ab, P4_ab, P8_auf), (m2_ab, P1, M2_ab, M2_auf, P4_ab, m3_ab, P5_ab, P4_auf), (M2_ab, M2_auf, m2_auf, P1, M3_ab, P4_auf, m3_auf, R, P5_auf, P5_ab, m6_auf, m3_ab, P4_ab), (M2_ab, m2_auf, P1, m3_auf, P4_ab, R, P5_ab, M3_ab), (M2_auf, M3_auf, m2_ab, P1, P4_auf, m3_ab, P4_ab, R, P5_auf, P8_auf), (M3_auf,), (m2_ab, M2_ab, P1, m3_ab, P5_ab, M2_auf, M3_ab, R, m3_auf, M3_auf, m2_auf, X), (M2_auf, P1, m2_auf, P5_auf, R, P4_auf, M2_ab, m3_auf, P5_ab, M3_auf, X, m3_ab, m6_auf, P4_ab, P8_auf), (P1, R, P5_ab, M2_ab, m3_ab, P4_ab, m2_ab, M2_auf, M3_ab, X, m3_auf, M3_auf, m2_auf), (M2_auf, R, P1, m2_ab, P5_auf, M3_auf, P4_auf, m3_auf, M2_ab, X, m3_ab, P8_auf, m2_auf, m6_auf), (m2_ab, P1, m3_ab, P5_ab, R, M2_ab, M2_auf), (P1, R, m3_ab, M2_ab, P4_ab, m2_ab), (M2_auf, R, P5_auf, P4_auf, m6_auf)))

PhrygianSetter = Setter(Phrygian, ((26, 24, 21, 11, 10, 7, 7, 6, 3, 2, 2, 2, 2, 2, 1, 1, 1), (37, 22, 20, 11, 9, 8, 4, 2, 2, 2, 1, 1), (69, 25, 19, 14, 8, 7, 7, 5, 3, 1, 1), (59, 53, 21, 17, 15, 11, 9, 6, 6, 5, 4, 2, 1, 1, 1), (59, 47, 35, 28, 16, 14, 9, 6, 5, 3, 2), (18, 11, 6, 4, 3, 3, 2, 1), (13, 12, 8, 5, 4, 3, 3, 2, 1), (3, 2, 1, 1, 1), (12, 7, 2, 1, 1), (1,), (18, 14, 11, 7, 3, 1, 1, 1, 1), (7, 4, 4, 3, 3, 3, 2, 2, 2, 1), (5, 2, 2, 2, 1, 1, 1), (6, 4, 3, 3, 1, 1, 1, 1, 1, 1), (3, 1, 1), (1, 1, 1), (2, 1, 1)), ((M2_ab, m2_ab, M2_auf, m3_auf, P1, P4_ab, m2_auf, P4_auf, X, P5_auf, m3_ab, R, M3_auf, P5_ab, P8_ab, M3_ab, m6_auf), (m2_ab, M2_auf, m3_ab, P4_ab, P1, R, M3_auf, M2_ab, P5_ab, P8_ab, P4_auf, m3_auf), (M2_ab, m2_auf, P1, R, P4_auf, M3_ab, X, m3_auf, m3_ab, d4_auf), (m2_auf, M2_auf, M2_ab, P1, m3_auf, M3_ab, P5_ab, R, m3_ab, P4_ab, P4_auf, X, P8_ab, P8_auf, P5_auf), (M2_ab, m2_ab, M2_auf, P1, R, m3_ab, P4_auf, P5_auf, m3_auf, P4_ab, M3_auf), (m2_ab, P1, M2_auf, M2_ab, m3_ab, P4_ab, R, P4_auf), (M2_auf, m2_auf, M2_ab, P1, m2_ab, P4_auf, P5_auf, P8_auf, m3_auf, P4_ab, m6_auf), (M2_ab, m2_auf, P4_ab, P1, P4_auf), (M2_auf, P4_auf, P1, R, m2_ab), (R,), (m2_ab, P1, M2_ab, M2_auf, P5_ab, R, m3_auf, m3_ab, M3_ab), (M2_auf, P4_auf, m3_auf, X, R, P1, M3_ab, M2_ab, m2_auf, m6_auf), (M2_auf, m2_auf, P1, m3_ab, M3_ab, P5_ab, R), (P4_auf, R, M2_auf, P1, m6_auf, P8_auf, m2_ab, M2_ab, m3_auf, P5_ab), (m2_ab, P1, m3_ab), (M2_ab, m2_ab, M2_auf), (M2_auf, P4_auf, P5_auf)))

LydianSetter = Setter(Lydian, ((6, 2, 2, 2, 1, 1, 1), (5, 2, 2, 2, 1, 1, 1, 1), (12, 4, 3, 1, 1), (7, 6, 4, 4, 3, 2, 1, 1, 1, 1, 1), (11, 9, 8, 5, 3, 2, 2, 2, 1, 1, 1, 1), (1, 1, 1, 1), (2, 1, 1), (3,), (1,), (3, 1, 1, 1), (2, 2, 2, 1, 1, 1, 1), (3, 3, 1, 1, 1), (1, 1, 1, 1, 1, 1, 1), (1,), (1,), (1,)), ((M2_ab, M2_auf, P5_ab, P4_auf, m2_auf, P1, m2_ab), (m2_ab, P4_ab, R, M2_auf, P1, P5_ab, P5_auf, X), (M2_ab, P1, m2_auf, P4_ab, M3_ab), (m2_auf, R, M2_ab, M2_auf, P5_auf, P1, m3_ab, P4_auf, P4_ab, m3_auf, X), (m2_ab, M2_auf, M2_ab, R, P5_auf, P5_ab, P1, m3_ab, M3_auf, P4_auf, P8_ab, m3_auf), (P4_ab, M3_auf, m2_ab, P1), (M2_auf, M2_ab, P1), (M2_ab,), (M2_auf,), (m2_ab, m3_ab, R, M2_ab), (P1, m3_auf, R, P4_ab, P5_ab, M2_auf, P8_auf), (R, M2_ab, P5_ab, M2_auf, P8_auf), (m6_auf, M2_ab, M2_auf, M3_auf, R, X, P4_auf), (M2_auf,), (M2_ab,), (M2_auf,)))

MixolydianSetter = Setter(Mixolydian, ((11, 8, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1, 1), (10, 9, 7, 3, 2, 2, 2, 2, 2, 1, 1, 1), (42, 11, 4, 2, 2, 2, 1, 1, 1), (19, 14, 6, 6, 6, 5, 5, 4, 2, 2, 2, 2, 1, 1, 1), (35, 27, 22, 9, 9, 4, 4, 2, 2, 2, 2, 1, 1, 1), (7, 5, 3, 3, 2), (7, 4, 3, 2, 1), (6, 6, 1, 1), (3, 1, 1), (1,), (5, 3, 2, 1, 1), (3, 3, 2, 1), (4, 2, 2, 2, 1, 1), (5, 3, 2, 2, 2, 1, 1, 1), (1,), (3, 2, 1), (1,), (2, 1)), ((M2_auf, M2_ab, M3_auf, m6_auf, m2_ab, m3_ab, P5_ab, P1, m2_auf, P4_ab, M3_ab, P8_ab, R), (M2_auf, m2_ab, R, P1, m3_ab, X, P4_auf, P4_ab, P5_auf, M3_auf, M2_ab, P5_ab), (M2_ab, m2_auf, P1, R, P5_ab, m3_auf, P4_ab, M2_auf, P4_auf), (m2_auf, M2_ab, P1, M2_auf, P5_ab, R, m3_auf, M3_ab, P4_ab, P4_auf, P8_ab, P5_auf, d4_auf, m6_auf, X), (m2_ab, M2_ab, M2_auf, R, P1, m3_ab, P5_auf, P4_auf, m3_auf, P5_ab, M3_auf, P4_ab, X, A4_auf), (m2_ab, M2_ab, P5_ab, M2_auf, P1), (m3_auf, M2_ab, M2_auf, P1, P4_auf), (m2_auf, M2_ab, P5_ab, P1), (M3_auf, P4_ab, m2_ab), (m3_ab,), (M2_ab, m2_ab, M2_auf, X, m3_ab), (M2_auf, m2_auf, m3_ab, P1), (P1, M2_auf, m2_ab, m3_auf, M2_ab, M3_auf), (R, M2_auf, P4_auf, m6_auf, P5_auf, M3_auf, P8_auf, X), (M2_ab,), (m2_ab, P1, M2_ab), (M2_ab,), (P5_auf, M2_auf)))

AeolianSetter = Setter(Aeolian, ((14, 13, 11, 7, 6, 6, 4, 4, 3, 3, 2, 2, 1, 1, 1), (18, 17, 6, 5, 5, 5, 4, 3, 2, 2, 1, 1), (49, 15, 9, 8, 5, 4, 3, 2, 1, 1), (35, 27, 12, 9, 7, 5, 3, 3, 3, 2, 2, 2, 1), (32, 29, 25, 14, 6, 6, 5, 4, 3, 3, 2, 2), (17, 6, 6, 4, 2, 1, 1, 1), (6, 6, 5, 5, 4, 3, 3, 2, 2), (2, 2, 1), (9, 4, 1, 1, 1), (6, 5, 3, 3, 1, 1, 1, 1, 1), (4, 4, 3, 1, 1, 1, 1, 1, 1, 1), (5, 3, 3, 3, 2, 1, 1, 1, 1), (7, 3, 3, 3, 1, 1, 1), (1,), (3, 2), (2, 1, 1)), ((P1, M2_auf, M2_ab, m3_auf, m2_ab, m3_ab, P4_auf, P5_auf, m2_auf, P5_ab, P8_auf, P4_ab, m6_auf, M3_ab, M3_auf), (m2_ab, M3_ab, R, P5_ab, P4_ab, M2_auf, P1, M3_auf, m3_auf, X, M3_ab, P5_auf), (M2_ab, m2_auf, R, P1, M3_ab, P4_auf, P5_ab, X, P8_auf, m3_auf), (m2_auf, M2_auf, M2_ab, P1, m3_auf, M3_ab, P5_ab, m2_ab, R, P5_auf, m3_ab, P8_ab, P4_ab), (M2_ab, M2_auf, m2_ab, R, m3_ab, m3_auf, P5_auf, P1, P4_auf, X, P5_ab, P4_ab), (m2_ab, P1, M2_auf, P4_ab, P4_auf, R, P8_ab, M3_auf), (P4_auf, M2_ab, M2_auf, m3_auf, m2_auf, P1, P5_auf, m2_ab, R), (M2_ab, P1, P5_ab), (m2_ab, M2_auf, P8_auf, P1, P4_ab), (M2_ab, m2_ab, m3_ab, P1, P5_ab, P4_ab, X, P5_auf, M3_ab), (M2_auf, P1, R, M2_ab, X, m2_auf, P5_auf, m2_ab, m3_auf, P8_auf), (M2_ab, R, m2_auf, M2_auf, m3_ab, P1, M3_ab, P8_ab, P5_ab), (P1, M2_auf, M2_ab, m3_auf, P5_auf, P4_auf, R), (P1,), (m2_ab, P1), (m2_auf, P5_auf, P1)))
	
Dorian.setSetter(DorianSetter)
Ionian.setSetter(IonianSetter)
Phrygian.setSetter(PhrygianSetter)
Lydian.setSetter(LydianSetter)
Mixolydian.setSetter(MixolydianSetter)
Aeolian.setSetter(AeolianSetter)

class generator:
	def __init__(self, mode):
		# to have a point of reference for the options inside of the generator
		# the intended starting note
		self.mode = mode
		self.options = self.mode.options
		self.mode.setScaleArguments()
		self.startMidiNoteNumber = (72 + self.mode.key)
		self.phrase = self.gen()
			

	def gen(self):
		result = [] # array of †uples => (midiNoteNumber, melodicInterval)
		generatePhrase = True
		i = 0
		while generatePhrase == True:
			if i == 0:
				result.append((self.startMidiNoteNumber, None))
			elif i == 1:
				baseInterval = random.choice(self.options)
				randomInterval = baseInterval.calculateNextInterval()[0]
				lastMidiNoteNumber = result[i-1][0] # access 0th element of tuple => midiNoteNumber
				newMidiNoteNumber = lastMidiNoteNumber + randomInterval.worth
				if newMidiNoteNumber in self.mode.scale:
					result.append((newMidiNoteNumber, randomInterval))
				else:
					continue
			else:
				baseInterval = result[i-1][1] # access 1st element of tuple => melodicInterval
				randomInterval = baseInterval.calculateNextInterval()[0]
				if randomInterval == m2_ab or randomInterval == M2_ab or randomInterval == X:
					if i >= 7:
						generatePhrase = False
				lastMidiNoteNumber = result[i-1][0] # access 0th element of tuple => midiNoteNumber
				newMidiNoteNumber = lastMidiNoteNumber + randomInterval.worth
				if newMidiNoteNumber in self.mode.scale:
					result.append((newMidiNoteNumber, randomInterval))
				else:
					continue
			i += 1
		return result
