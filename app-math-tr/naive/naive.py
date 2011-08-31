import re
import math

words = {}

# find all words in all files, creating a 
# global dictionary.
for file in ['a1.txt','a2.txt','a3.txt',
             'b1.txt','b2.txt','b3.txt']:
    f = open (file)
    s = f.read()
    tokens = re.split('\W+', s)
    for x in tokens: words[x] = 0.
    
hawking_alphas = words.copy()   
for file in ['a1.txt','a2.txt','a3.txt']:
    words_hawking = set()
    f = open (file)
    s = f.read()
    tokens = re.split('\W+', s)
    for x in tokens: 
        words_hawking.add(x)
    for x in words_hawking:
        hawking_alphas[x] += 1.
        
obama_alphas = words.copy()   
for file in ['b1.txt','b2.txt','b3.txt']:
    words_obama = set()
    f = open (file)
    s = f.read()
    tokens = re.split('\W+', s)
    for x in tokens: 
        words_obama.add(x)
    for x in words_obama:
        obama_alphas[x] += 1.

for x in hawking_alphas.keys():
    hawking_alphas[x] = hawking_alphas[x] / 3.        
for x in obama_alphas.keys():
    obama_alphas[x] = obama_alphas[x] / 3.        

def prob(xd, alpha):
    return math.log(alpha*xd + 1e-10) + \
        math.log((1.-alpha)*(1.-xd) + 1e-10)
        
def test(file):
    test_vector = words.copy()   
    words_test = set()
    f = open (file)
    s = f.read()
    tokens = re.split('\W+', s)
    for x in tokens: 
        words_test.add(x)
    for x in words_test:  
        test_vector[x] = 1.
    ob = 0.
    ha = 0.
    for x in test_vector.keys(): 
        if x in obama_alphas: 
            ob += prob(test_vector[x], obama_alphas[x])
        if x in hawking_alphas: 
            ha += prob(test_vector[x], hawking_alphas[x])
                
    print "obama", ob, "hawking", ha, \
    "obama", ob > ha, "hawking", ha > ob


print "hawking test"    
test('a4.txt')
print "hawking test"    
test('a5.txt')
print "obama test"    
test('b4.txt')
print "obama test"    
test('b5.txt')

