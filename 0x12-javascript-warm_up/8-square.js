#!/usr/bin/node

const arg = parseInt(process.argv[2]);
if (Number.isNaN(arg)) console.log('Missing size');
else {
  let i = 0;
  while (i < arg) {
    console.log('X'.repeat(arg));
    i++;
  }
}
