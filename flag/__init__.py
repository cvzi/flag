# -*- coding: utf-8 -*-
# Converts flag emoji to ascii and back
# https://github.com/cvzi/flag
# Based on http://schinckel.net/2015/10/29/unicode-flags-in-python/

import sys
import re

__all__ = ["flagize", "dflagize"]

OFFSET = 127397 # = ord("🇦") - ord("A")

PY2 = sys.version_info.major is 2

def flagize(text):
    def flag(code):
        if not code:
            return u""
        points = list(map(lambda x: ord(x) + OFFSET, code.upper()))
        
        if PY2:
            return ("\\U%08x\\U%08x" % tuple(points)).decode("unicode-escape")
        else:
            return chr(points[0]) + chr(points[1])
    
    def flag_repl(matchobj):
        return flag(matchobj.group(1))
    
    text = re.sub(":([a-zA-Z]{2}):", flag_repl, text)
    
    return text

def dflagize(text):
    if PY2:
        return dflagize_py2(text)
    else:
        return dflagize_py3(text)

def dflagize_py3(text):
    def dflag(i):
        points = tuple(map(lambda x: ord(x) - OFFSET, i))
        return ":%c%c:" %  points
    
    def dflag_repl(matchobj):
        return dflag(matchobj.group(0))
    
    regex = re.compile(u"([\U0001F1E6-\U0001F1FF]{2})", flags=re.UNICODE)
    
    text = regex.sub(dflag_repl, text)
    
    return text

def dflagize_py2(text):
    def dflag_repl(matchobj):
        a = int(matchobj.group(1), 16)
        b = int(matchobj.group(2), 16)
        if a >= 127462 and a <= 127487 and b >= 127462 and b <= 127487:
            return ":%c%c:" % (a - OFFSET, b - OFFSET)
        return matchobj.group(0)
    
    regex = re.compile(r"\\U([0-9a-fA-F]{8})\\U([0-9a-fA-F]{8})")
    
    text = regex.sub(dflag_repl, text.encode("unicode-escape"))
    
    return text.decode("unicode-escape")
