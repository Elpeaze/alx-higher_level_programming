#!/usr/bin/node
const [argsNum1] = process.argv.slice(2);

if (isNaN(argsNum1)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argsNum1));
}
