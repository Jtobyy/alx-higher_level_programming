#!/usr/bin/node

const arg = parseInt(process.argv[2]);
function factorial (n) {
  if (Number.isNaN(arg)) return 1;
  if (n === 1) return 1;
  else n *= factorial(n - 1);
  return n;
}

console.log(factorial(arg));
