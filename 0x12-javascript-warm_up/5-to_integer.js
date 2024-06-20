#!/usr/bin/node
function convertNum(value) {
	let num = parseInt(value);
	if (isNaN(num)) {
		console.log('Not a Number');
	} else {
		console.log('My number:', num);
	}
}
let input = process.argv[2];
convertNum(input);