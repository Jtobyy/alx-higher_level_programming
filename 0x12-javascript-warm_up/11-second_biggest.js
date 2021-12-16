#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) console.log(0);
else {
  const arr = process.argv;
  for (let i = 2; i < process.argv.length; i++) {
    process.argv[i] = parseInt(process.argv[i]);
  }
  let b = arr[2];
  for (let i = 3; i < arr.length; i++) {
    if (arr[i] >= b) b = arr[i];
  }
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] === b) {
      delete arr[i];
    }
  }
  let j = 2;
  b = arr[j];
  while (arr[j] == null && j < arr.length) {
    b = arr[j + 1];
    j++;
  }
  for (let i = 2; i < arr.length; i++) {
    if (arr[i] == null) continue;
    if (arr[i] >= b) b = arr[i];
  }
  console.log(b);
}
