class Cell {
	constructor() {
		this.Visited = false;
		this.Right = false;
		this.Down = false;
	}

	Visit() {
		this.Visited = true;
	}
}

class Maze {
	constructor(l,w,h) {
		this.Data = l;
		this.Width = w;
		this.Height = h;
	}

	Draw(border=true, Border = true, BChar='#', log=false) {

		var cmaze = [];

		console.log(this.Data);

		if (Border) { cmaze.push(BChar.repeat(this.Width*2+2)); }
		for (let y of this.Data) {
			var l1 = (Border ? BChar : '');
			var l2 = (Border ? BChar : '');
			for (let x of y) {
				l1 += (x.Visited ? '#' : ' ');
				l1 += (x.Right ? '#' : ' ');
				l2 += (x.Down ? '#' : ' ');
				l2 += ' ';
			}
			l1 += Border ? BChar : '';
			l2 += Border ? BChar : '';
			cmaze.push(l1);
			cmaze.push(l2);
		}
		if (Border) { cmaze.push(BChar.repeat(this.Width*2+2)); }

		if (log == true) { console.log(cmaze.join('\n')); }

		const DaGrid = document.getElementById('TheGrid');
		
		DaGrid.innerHTML = '';
		DaGrid.style.gridTemplateColumns = `repeat(${this.Width}, 1fr) !important`;
		DaGrid.style.gridTemplateRows = `repeat(${this.Height}, 1fr) !important`;

		for (let y of cmaze) {
			for (let x of y) {
				const cell = document.createElement('div');
				cell.classList.add(x == '#' ? 'taken' : 'empty');
				DaGrid.appendChild(cell);
			}
		}
	}
}
