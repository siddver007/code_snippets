# Program to find longest substring with max 2 unique characters and if multiple are present
# print all

def isPresent(_s, c):
	b = 0
	for ch in _s:
		if c == ch:
			b = 1
			break
	if b == 0:
		return False		
	else:
		return True	
		
def findMax2(_s):
	for ch in xrange(len(_s)):
		ss = []
		ss.append(_s[ch])
		count = 1
		for ch2 in xrange(ch + 1,len(_s)):
			if isPresent(ss, _s[ch2]):
				ss.append(_s[ch2])
			else:
				# This count < 2 decides max of 2 unique characters
				if count < 2:
					ss.append(_s[ch2])
					count += 1
				else:
					break	
		s_list.append(''.join(ss))					
			
if __name__ == '__main__':
	s = ('aaaabbbbcccczxcvfxcdvsdfgvdfhgdflkmkqwmslwqmqqqqqqqqqqqqqqqqqqqpqwkwddopewdpewpodpewdpqqqqqqqqqqqqqqqqqqjjjjjjjjjjeejjjjjjjjjjj' +
		'aaaabbbbcccczxcvfxcdvsdfgvdfhgdflkmkqwmslwqmqqqqqqqqqqqqqqqqqqqpqwkwddopewdpewpodpewdpqqqqqqqqqqqqqqqqqqjjjjjjjjjeejjjjjjjjjjjj' +
		'aaaabbbbcccczxcvfxcdvsdfgvdfhgdflkmkqwmslwqmqqqqqqqqqqqqqqqqqqqpqwkwddopewdpewpodpewdpqqqqqqqqqqqqqqqqqqjjjjjjjjjeejjjjjjjjjjjj' +
		'aaaabbbbcccczxcvfxcdvsdfgvdfhgdflkmkqwmslwqmqqqqqqqqqqqqqqqqqqqpqwkwddopewdpewpodpewdpqqqqqqqqqqqqqqqqqqjjjjjjjjjjjeejjjjjjjjjj')

	_s = list(s)
	s_list = []

	findMax2(s)							
	
	max_s = ''
	for x in  s_list:
		if len(x) > len(max_s):
			max_s = x

	aaa = []
	aaa.append(max_s)		
	for x in s_list:
		if len(max_s) == len(x)	and x != max_s:
			aaa.append(x)	

	print aaa								