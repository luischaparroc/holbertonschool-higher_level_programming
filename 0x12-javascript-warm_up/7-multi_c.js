#!/usr/bin/node
let i = parseInt(process.argv[2]);
if (Number.isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  while (i > 0) {
    console.log('C is fun');
    i--;
  }
}
