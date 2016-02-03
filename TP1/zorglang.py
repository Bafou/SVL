"""
Zorglang
"""

class TradZorglang:

	def __init__(self):
		pass

	def zorglang(self, chaine):
		res = ''
		resInter = ''
		for c in chaine:
			if (c.isalpha()):
				resInter = c + resInter
			else:
				res += resInter + c
				resInter = ''
		res += resInter
		return res

