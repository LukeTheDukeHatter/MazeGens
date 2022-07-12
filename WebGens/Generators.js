function HuntToKill(width, height){
	var grid = [];
	for (let y = 0; y<height; y++) {
		var t = [];
		for (let x = 0; x<width; x++) {
			t.push(new Cell());
		}
		grid.push(t);
	}

	for (let y = 0;y<height; y++) {
		for (let x = 0; x<height; x++) {
			let cx = x;
			let cy = y;

			var Stuck = false;
			while (!Stuck) {

				grid[cy][cx].Visit();

				ValidRoutes = [];

				if (cy > 0 && !grid[cy-1][cx].Down) {
					ValidRoutes.push('Up');
				}
				if (cy < height-1 && !grid[cy][cx].Down) {
					ValidRoutes.push('Down');
				}
				if (cx > 0 && !grid[cy][cx-1].Right) {
					ValidRoutes.push('Left');
				}
				if (cx < width-1 && !grid[cy][cx].Right) {
					ValidRoutes.push('Right');
				}

				while (true) {
					if (ValidRoutes.length == 0) {
						Stuck = true;
						break;
					}

					Route = ValidRoutes[Math.floor(Math.random()*ValidRoutes.length)];

					if (Route == 'Up' && !grid[cy-1][cx].Visited) {
						cy--;
						grid[cy][cx].Down = true;
						break;
					} else if (Route == 'Down' && !grid[cy+1][cx].Visited) {
						grid[cy][cx].Down = true;
						cy++;
						break;
					} else if (Route == 'Left' && !grid[cy][cx-1].Visited) {
						cx--;
						grid[cy][cx].Right = true;
						break;
					} else if (Route == 'Right' && !grid[cy][cx+1].Visited) {
						grid[cy][cx].Right = true;
						cx++;
						break;
					} else {
						ValidRoutes.splice(ValidRoutes.indexOf(Route), 1);
					}
				}
			}
		}
	}
	return new Maze(grid, width, height);
}