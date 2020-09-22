
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", mobilephone="", workphone="", homephone="")] + [
    Contact(firstname=random_string('firstname_', 10), lastname=random_string('lastname_', 10),
                  mobilephone=random_string('mobilephone_', 5), workphone=random_string('workphone_', 5),
                    homephone=random_string('homephone_', 5)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)
with open(file, 'w') as ff:
    jsonpickle.set_encoder_options('json', indent=2)
    ff.write(jsonpickle.encode(testdata))