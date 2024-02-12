#!/usr/bin/node
const request = require('request');
const argv = require(' process.argv')

if (argv.length == 3) {
	const id = argv[2]
}
const url = `https://swapi-api.alx-tools.com/api/films/${id}`

request(url, function(error, response, body) {
    if (error)
	// pass
    film = JSON.parse(body)
    characters = film['characters']
});

function get_req (url) {
    const res = new Promise(function(resolve, reject) {
	request(url, function(error, response, body) {
	    if (response === 200) {
		person = JSON.parse(body);
		resolve(person['name']);
	    } else {
		reject(respose)
	    }
	});
    });
    return res;
}

for (character of characters) {
    get_req(url).then((result) => (console.log(result)))
    .catch((error) => (console.log(error)))
}




