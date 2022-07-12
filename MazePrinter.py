
def EDraw(g:list,Border:bool=True,data:str=False,BChar:str='#',log:str=False):
	if log:
		from FPrint import InitFPrint,print
		InitFPrint(log)

	if data:
		print(f"\n\n{data}\n")

	if Border: print(BChar*(len(g[0])*2+2))
	for y in g:
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
	if Border: print(BChar*(len(g[0])*2+2))

	print('\n\n\n')