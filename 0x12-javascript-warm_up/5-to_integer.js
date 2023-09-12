#!/usr/bin/node
const num = Math.trunc(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
