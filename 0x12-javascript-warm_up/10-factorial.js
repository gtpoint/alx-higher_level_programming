#!/usr/bin/node
function factorial (n) {
  let result = n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
  return result;
}

console.log(factorial(Number(process.argv[2])));
