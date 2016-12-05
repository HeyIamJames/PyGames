#cheet sheet = https://www.debuggex.com/cheatsheet/regex/python

#return all ints of len 6

import re
re.findall(r"\D(\d{6})\D", s)

#include 6+
only len 6 = /([\W\w])\d{6}
#only 6
^\D*\d{15}\D*$

#how to replace char

re.sub('[d]', ' ', x)


>>> str = "h3110 23 cat 444.4 rabbit 11 2 dog"
>>> [int(s) for s in str.split() if s.isdigit()]
[23, 11, 2]

#invest result> 
re.findall("\W\w", {1}, s) 
s = "ds 4"
