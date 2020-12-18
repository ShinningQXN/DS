# LC722: remove comments

# https://leetcode.com/problems/remove-comments/

# Get random

# https://www.1point3acres.com/bbs/thread-689845-1-1.html
import re
def f(source):
	return filter(None, re.sub('--.*\n', '\n', source))
s = "SELECT * FROM files --- This is an inline comment\nWHERE fullpath LIKE '/home/%';"
r = f(s)
print(r)
s = "SELECT * FROM files --- This is an inline comment\nWHERE fullpath LIKE 'xxx---xxx\\\'hi\'xx';"
r = f(s)
print(r)
s = "SELECT * FROM files --- This is an inline comment \nWHERE fullpath LIKE 'xxx---x\\xx\';"
r = f(s)
print(r)
# s = "SELECT * FROM files --- This is an inline comment\nWHERE fullpath LIKE '/home/%';"
# f(s)
