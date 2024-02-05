#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, 'utf-8', (err, res, data) => {
  if (err) {
    console.log(err);
	return;
  }
  fs.writeFile(filePath, data, (err) => {
    if (err) {
	  console.log(err);
	}
  });
});
