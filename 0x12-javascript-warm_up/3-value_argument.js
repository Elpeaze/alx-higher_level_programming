#!/usr/bin/node
const [argsNum1] = process.argv.slice(2);

if (!argsNum1) {
  console.log('No argument');
} else {
  console.log(argsNum1);
}
