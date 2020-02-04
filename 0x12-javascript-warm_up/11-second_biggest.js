#!/usr/bin/node

let biggest = 0;
let i;
const arrayNumbers = [];

for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    arrayNumbers[i - 2] = parseInt(process.argv[i]);
  }
}

if (arrayNumbers.length > 1) {
  biggest = Math.max.apply(null, arrayNumbers);
  i = arrayNumbers.indexOf(biggest);
  arrayNumbers[i] = -Infinity;
  biggest = Math.max.apply(null, arrayNumbers);
}

console.log(biggest);
