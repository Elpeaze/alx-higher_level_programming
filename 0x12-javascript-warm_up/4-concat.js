#!/usr/bin/node
const [argsNum1, argsNum2] = process.argv.slice(2);

if (argsNum1 && argsNum2) {
  console.log(argsNum1 + ' is ' + argsNum2);
} else if (argsNum1) {
  console.log(argsNum1 + ' is undefined');
} else {
  console.log('undefined is undefined');
}
