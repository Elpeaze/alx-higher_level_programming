#!/usr/bin/node
const [argsNum1] = process.argv.slice(2);

if (isNaN(argsNum1)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argsNum1); i++) {
    let symbol = '';
    for (let j = 0; j < parseInt(argsNum1); j++) {
      symbol += 'x';
    }
    console.log(symbol);
  }
}
