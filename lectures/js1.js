const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const evenSquares = numbers
	.filter(n => n % 2 === 0);
numbers
	.map(n => n * n);

console.log(evenSquares);
