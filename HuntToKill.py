from random import choice
from MazeClasses import Cell,Maze

def HuntToKill(width:int,height:int,grid:list=False,log:bool=False) -> Maze:
	if not grid: 
		grid = [[Cell() for x in range(width)] for y in range(height)]

	for y in range(height):
		for x in range(width):
			cx,cy = x,y
			
			Stuck = False
			while not Stuck:
				
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

				while True:
					if len(ValidRoutes) == 0:
						Stuck = True
						break

					Route = choice(ValidRoutes)
					
					if (Route == 'Up') and (not grid[cy-1][cx].Visited):
						cy -= 1
						grid[cy][cx].Down = True
						break
					elif (Route == 'Down') and (not grid[cy+1][cx].Visited):
						grid[cy][cx].Down = True
						cy += 1
						break
					elif (Route == 'Left') and (not grid[cy][cx-1].Visited):
						cx -= 1
						grid[cy][cx].Right = True
						break
					elif (Route == 'Right') and (not grid[cy][cx+1].Visited):
						grid[cy][cx].Right = True
						cx += 1
						break
					else:
						ValidRoutes.remove(Route)

	return Maze(grid,width,height)