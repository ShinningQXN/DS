bfs126

# METHOD
####################################################### 
# bfs + path (一般这种情况path应该存在哪里呢？)

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


class Ladder:
	def find_shortest_path(self, wordlist, begin, end):
		if not begin or not end or not wordlist:
			return []
		if begin or end not in wordlist:
			return []

		q = [(begin, begin)]
		seen = {(begin, begin)}
		reached = False

		while q:
			nexts = []
			for cur, pre in q:
				if cur == end:
					reached = True
				for i in range(len(cur)):
					for c in range(26):
						nei = cur[:i] + char(ord('a') + c) + cur[i+1:]
						if nei != cur and nei in wordlist and (nei,cur) not in seen:
							seen.add((nei,cur))
							nexts.append((nei, cur))
			if reached:
				break

		pres = collections.defaultdict(list)
		for a, b in seen:
			pres[b].append(a)

		rst = []
		def dfs(cur, path):
			if cur == begin:
				rst.append(path)
			for pre in pres[cur]:
				dfs(pre, path + cur)

		dfs(end, [])
		rst = [a[::-1] for a in rst]
		return rst

# dog - god
# dog,fog,fot,hot,dot,doe

# dog - fog - fot - hot
# dog - dae - dat - hot

# q = [(dog,dog)], [fog,dog;dae,dog;doe,dog], [fotdog,hotdot,]
# seen = (dog,dog),dotdog,doedog,




	