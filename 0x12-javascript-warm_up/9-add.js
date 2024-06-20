#!/usr/bin/node
function add(a, b) {
	let num1 = parseInt(a);
	let num2 = parseInt(b);
	if (isNaN(num1) || isNaN(num2)) {
		console.log(NaN);
	} else {
	let sum = num1 + num2;
	console.log(sum);
}
}
let input1 = process.argv[2];
let input2 = process.argv[3];
add(input1,input2);