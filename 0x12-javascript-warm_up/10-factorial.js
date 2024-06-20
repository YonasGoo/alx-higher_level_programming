#!/usr/bin/node
function factorial(n) {
	let num = parseInt(n);
	if (isNaN(num)) {
		console.log(1);
		return;
	}
	if (num === 0) {
		return 1;
	} else {
		return num * factorial(num -1);
		console.log(num);
	}
}
let input = process.argv[2];
let result = factorial(input);
if (result !== undefined) {
	console.log(result);
}