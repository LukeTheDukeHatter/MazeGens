from random import shuffle
from MazeClasses import Cell,Maze

def RecursiveMazeGen(width:int,height:int,log:bool=False) -> Maze:
	return Maze(_Recurse(width,height),width,height)

def _Recurse(width:int,height:int,cx:int=0,cy:int=0,grid:list=False,log:bool=False) -> list:
	if not grid: 
		grid = [[Cell() for x in range(width)] for y in range(height)]
	grid[cy][cx].Visit()

	ValidRoutes=[]
	
	if (cy > 0) and (not grid[cy-1][cx].Down):
		ValidRoutes.append('Up')
	if (cy < height-1) and (not grid[cy][cx].Down):
		ValidRoutes.append('Down')
	if (cx > 0) and (not grid[cy][cx-1].Right):
		ValidRoutes.append('Left')
	if (cx < width-1) and (not grid[cy][cx].Right):
		ValidRoutes.append('Right')

	if len(ValidRoutes) == 0:
		return grid

	shuffle(ValidRoutes)

	for id in range(len(ValidRoutes)):
		tcx = cx
		tcy = cy

		Route = ValidRoutes[id]

		Altered = False

		if (Route == 'Up') and (not grid[tcy-1][tcx].Visited):
			tcy -= 1
			grid[tcy][tcx].Down = True
			Altered = True
		elif (Route == 'Down') and (not grid[tcy+1][tcx].Visited):
			grid[tcy][tcx].Down = True
			tcy += 1
			Altered = True
		elif (Route == 'Left') and (not grid[tcy][tcx-1].Visited):
			tcx -= 1
			grid[tcy][tcx].Right = True
			Altered = True
		elif (Route == 'Right') and (not grid[tcy][tcx+1].Visited):
			grid[tcy][tcx].Right = True
			tcx += 1
			Altered = True
		
		if log:
			from MazePrinter import EDraw
			EDraw(grid,data=f"\ncx: {cx},cy: {cy},tcx: {tcx},tcy: {tcy}\nRoute: {Route}\nRoutes: {str(ValidRoutes)}\n")

		if Altered:
			grid = _Recurse(width,height,cx=tcx,cy=tcy,grid=grid)

	return grid