#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const characterLen = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, data) => {
  if (error) {
    console.log(error);
  } else {
    const films = JSON.parse(data).results;
    const match = films.filter((film) => film.characters.includes(characterLen)).length;
    console.log(match);
  }
});
