#!/usr/bin/node

const [args1, args2] = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

if (isNaN(args1) || isNaN(args2)) {
  console.log('NaN');
} else {
  const a = parseInt(args1);
  const b = parseInt(args2);

  console.log(add(a, b));
}
