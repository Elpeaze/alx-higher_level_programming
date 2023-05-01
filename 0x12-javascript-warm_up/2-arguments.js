#!/usr/bin/node
const argsNum = process.argv.slice(2);

if (argsNum.length === 0) {
  console.log('No argument');
} else if (argsNum.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
