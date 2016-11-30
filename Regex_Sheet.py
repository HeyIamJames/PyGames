#cheet sheet = https://www.debuggex.com/cheatsheet/regex/python

#return all ints of len 6

import re
re.findall(r"\D(\d{6})\D", s)
