#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

#----------Test strings----------
s = u'aaaaaadgfdhgfbbbbgggee)ehje ekekkkkkeefh ehfeff88888éééééh\"hr ekkKKKKK\njhxjhjhhhhh\nthe the\n\"eeeeeeeeaaaabcaaaaadexxxdddzdzzzz\"\n\"eeeeeeeeaaaabcaaaaadexxxdddzdzzzz\"\n\"eeeeeeeeaaaabcaaaaadexxxdddzdzzzz\"\n\"aaaeeeeeeeeaaaadzxzzzzffffrrrr\"\n\"aaa\"'

p = re.compile(ur'(\w)\1\1\1+')

def compress_match(matchobj):
    s = matchobj.group(0)
    if len(s) >= 4 : return (str(len(s)) + "x" + s[0])
    return ("")

new_string, n = re.subn(ur'(\w)\1\1\1+', compress_match, s)
print ("number_of_subs_made : %s, new_string : %s" % (n, new_string))
