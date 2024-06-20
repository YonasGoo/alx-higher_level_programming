#!/usr/bin/node
function printMsg(times) {
	let num = parseInt(times);
	if (isNaN(num)) {
		console.log('Missing number of occurrences');
	} else {
		for (let i = 0; i < num; i++) {
			console.log('C is fun');
		}
	}
}
let input = process.argv[2];
printMsg(input);