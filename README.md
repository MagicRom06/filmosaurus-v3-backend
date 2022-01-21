# Filosaurus API

## introduction
Filmosaurus API is an api that can be used for free where you can get informations regarding about 80 000 movies. This is a standard API that waiting for a HTTP request and returning a json.

## Informations
The API is written wyth Python through the framework Django and Django Rest Framework.<br>
API url: https://filmosaurus-api.net/ <br>

## Tutorial

### Movies
Search a movies => https://filmosaurus-api.net/api/v1/search?query={{keyword}}&page=1 <br>
The request will return a list of movies related to the searched keyword.
<br>
<br>
Get movie detail => https://filmosaurus-api.net/api/v1/movie/{{movieID}} <br>
Will return information regarding the searched movie.
<br>
<br>
Get poster from a movie => https://fimosaurus-api.net/api/v1/image/get?movie={{title}}&year={{year}}`<br>
Return the url of the poster.
