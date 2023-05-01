#!/usr/bin/node
const [argsNum1, argsNum2] = process.argv.slice(2);

if (argsNum1 === 'c' && argsNum2 === 'cool') {
  console.log('c is cool');
} else if (argsNum1 === 'c') {
  console.log('c is undefined');
} else {
  console.log('undefined is undefined');
}
