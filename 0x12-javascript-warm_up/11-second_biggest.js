#!/usr/bin/node
function findBig(args) {
	let nums = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));
	if (nums.length < 2) {
		console.log(0);
		return;
	}
	nums.sort((a, b) => b - a);
	let bigNum = nums[1];
	console.log(bigNum);
}
let input = process.argv.slice(2);
findBig(input);