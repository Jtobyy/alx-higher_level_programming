#!/usr/bin/node

const arg = parseInt(process.argv[2]);
if (Number.isNaN(arg)) console.log('Missing number of occurrences');
else {
  let i = 0;
  while (i < arg) {
    console.log('C is fun');
    i++;
  }
}
