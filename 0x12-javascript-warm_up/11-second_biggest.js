#!/usr/bin/node
function findBig(args) {
	let nums = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));
	if (nums.length === 0 || nums.length === 1) {
		console.log(0);
	} else {
		let maxNum = Math.max(...nums);
		console.log(maxNum);
	}
}
let input = process.argv.slice(2);
findBig(input);