var maze = --HERE--;

const grid = document.getElementById('TheGrid');

maze.forEach(element => {
    for (let i of element) {
        let x = document.createElement('div');
        x.classList.add(i == '#' ? 'taken' : 'empty');
        grid.appendChild(x);
    }
});