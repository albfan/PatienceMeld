from bzrlib.patiencediff import unified_diff
from bzrlib.patiencediff import PatienceSequenceMatcher
from difflib import Differ
import sys

__author__ = 'nenopera'

text1 = '''  1. Beautiful is better than ugly.
  2. Explicit is better than implicit.
  3. Simple is better than complex.
  4. Complex is better than complicated.
  
  function bye {
    if (true) {
        print "goodbye"
    }
  }

  function eco {
    if (true) {
        yyy = 98
    } else {
        cant = 45 + 3
    }
  }
'''.splitlines(1)

text2 = '''  1. Beautiful is better than ugly.
  3.   Simple is better than complex.
  4. Complicated is better than complex.
  5. Flat is better than nested.

  function hi {
    if (true) {
        print "Hello"
    }
  }

  function bye {
    while (true) {
        switch a:
            case
            print "aaaa"*4
            break
    }
  }

  function eco {
    if (true) {
        yyy = 98
    } else {
        cant = 45 + 3
    }
  }
'''.splitlines(1)

d = Differ()

def print_line(message):
    print
    print message + " " + "-" * 20
    print

print_line("text1")

sys.stdout.writelines(text1)

print_line("text2")

sys.stdout.writelines(text2)

print_line("normal compare normal text1 a text2")

sys.stdout.writelines(list(d.compare(text1, text2)))

print_line("normal compare text2 a text1")

sys.stdout.writelines(list(d.compare(text2, text1)))

matcher = PatienceSequenceMatcher

print_line("compare PATTIENCE text1 a text2")

sys.stdout.writelines(list(unified_diff(text1, text2,
                        fromfile="text1", tofile="text2",
                        sequencematcher=matcher)))

print_line("compare PATTIENCE text2 a text1")

sys.stdout.writelines(list(unified_diff(text2, text1,
                        fromfile="text2", tofile="text1",
                        sequencematcher=matcher)))
