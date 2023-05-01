#!/usr/bin/node
const [argsNum1] = process.argv.slice(2);

if (isNaN(argsNum1)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(argsNum1); i++) {
    console.log('C is fun');
  }
}
