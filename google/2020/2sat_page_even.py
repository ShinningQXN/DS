# PROBLEM
#######################################################
# 这轮跪了。假设有一本书，要实现一个machine， 每次给一个input (startPage, endPage, words count is even or odd from startPage to endPage)，基于之前的输入，判断当前输入是否有效。
# e.g. 1st input (0, 10, Even) -> valid; 2nd input (11, 15, Even) -> valid; 3rd input (0, 15, Odd) -> False, 因为0-15只能是even

# METHOD
####################################################### 
Let P(i) means page 0 - i
so input(11,15,even) -> P(15) - P(11) is even, which means they are in the same party
so which mean this problem is to see if the graph could be a bipartite
#  so now use prefix sums in Z_2, so P[5] = P[1], P[15] = P[5], P[15]  != P[1]
# now its 2sat
# or just like bipartite coloring, or whatever you want
# very easy after this bijection to prefix sum in Z_2
# "by prefix sums in Z_2" i mean:
# Let A be the number of words on page i, we only care about this mod 2, so say its mod 2.
# Let P[i+1] = A[0] + ... + A   mod 2
# so now note any binary sequence A corresponds to a binary sequence P, and vice versa, so its a bijection.  So if a P exists, so does an A
# now look at the condition like (1, 5, even), it means P[5] - P[1] = 0 mod 2, or equivalently P[5] = P[1] mod 2
# ok so now its just like can you 2-color this graph basically.  the algorithm is, you start at any uncolored node and try to color the connected component greedily based on the edges (equal, or different) you have

# CORNER CASE
####################################################### 
# begin == end
# begin or end not in wordlist
# uppercase?
# abce - adce

# 注意点
####################################################### 
# 对于bfs，一定不能走回头路
# 对于有重复路过的点，我们只要每个node可以有多个parent就可以啦
# 我的写法真的一点都不好

class Page:
	def __init__():
		self.color = {-1:0}
		self.uncolored = defaultdict(list)

	def check(start:int, end:int, even_odd:int)->bool:
		start -= 1
		def add_color(x):
			stack = [x]
			while stack:
				cur = stack.pop()
				for nei, v in self.uncolored[cur]:
					
		if start in self.color and end in self.color:
			return self.color[start] == self.color[end] ^ even_odd
		elif start in self.color:




