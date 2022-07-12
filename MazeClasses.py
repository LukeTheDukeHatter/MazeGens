class Cell():
	def __init__(self):
		self.Visited = False
		self.Right = False
		self.Down = False

	def Visit(self):
		self.Visited = True

class Maze():
	def __init__(self,l,w,h):
		self.Data = l
		self.Width = w
		self.Height = h

	def Draw(self,Border=True,BChar = '#',log:str=False) -> None:
		# if log:
		# 	from FPrint import InitFPrint,print
		# 	InitFPrint(log)
		if Border: print(BChar*(self.Width*2+2))
		for y in self.Data:
			l1 = BChar if Border else ''
			l2 = BChar if Border else ''
			for x in y:
				l1 += '#' if x.Visited else ' '
				l1 += '#' if x.Right else ' '
				l2 += '#' if x.Down else ' '
				l2 += ' '
			l1 += BChar if Border else ''
			l2 += BChar if Border else ''
			print(l1)
			print(l2)
		if Border: print(BChar*(self.Width*2+2))