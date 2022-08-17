import pprint
pp = pprint.PrettyPrinter(indent = 4)

test_rotor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rotor_i =    'EKMFLGDQVZNTOWYHXUSPAIBRCJ'

rotors = {
	'Test Rotor': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
	'Rotor I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
	'Rotor II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
	'Rotor III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
	'Reflector A': 'EJMZALYXVBWFCRQUONTSPIKHGD',
	'Reflector B': 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
}



def compute_rotor(rotor_string):
	rotor_map = {
		'NUMERIC':[],
		'OFFSET':[],
		'FORWARD':[0]*26,
		'BACKWARD':[0]*26
	}

	for i in range(0,len(rotor_string)):
		char = rotor_string[i]
		l = ord(char) - 65

		rotor_map['FORWARD'][i] = l

		rotor_map['NUMERIC'].append(l)
		rotor_map['OFFSET'].append(((l-i)+26)%26)

	for i in range(0,26):
		char = rotor_string[i]
		l = ord(char) - 65

		rotor_map['BACKWARD'][l] = i

	return rotor_map

for name,rotor in rotors.items():
	print('{}: '.format(name))
	data = compute_rotor(rotor)

	print('\tNumeric: ', end='')
	print(data['NUMERIC'])
	print('\tOffset: ', end='')
	print(data['OFFSET'])
	print('\tForward: ', end='')
	print(data['FORWARD'])
	print('\tBackward: ', end='')
	print(data['BACKWARD'])
	print()
