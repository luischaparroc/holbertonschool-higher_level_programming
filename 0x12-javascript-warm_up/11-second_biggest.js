#!/usr/bin/node
let secondbiggest = 0;
let biggest = 0;

for (let i = 2; i < process.argv.length; i++) {
  if (process.argv[i] >= biggest) {
    secondbiggest = biggest;
    biggest = process.argv[i];
  }
  if ((process.argv[i] < biggest) && (process.argv[i] > secondbiggest)) {
    secondbiggest = process.argv[i];
  }
}

console.log(secondbiggest);
