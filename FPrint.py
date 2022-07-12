openfile = None

def InitFPrint(fn:str) -> None:
	global openfile
	openfile = open(f"{fn}.txt",'a')

def print(txt:any,end:str='\n') -> None:
	global openfile
	openfile.write((str(txt) if (type(txt) != str) else txt) + end)

def fprint(txt:any,filename:str,end:str='\n') -> None:
	with open(f"{filename}.txt",'a') as of:
		of.write((str(txt) if (type(txt) != str) else txt) + end)