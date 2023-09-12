#!/usr/bin/node
let arg_1 = !process.argv[2] ? "undefined" : process.argv[2];
let arg_2 = !process.argv[3] ? "undefined" : process.argv[3];
console.log(`${arg_1} is ${arg_2}`);
