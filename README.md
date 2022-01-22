# Filosaurus API

## introduction
Filmosaurus API is an api that can be used for free where you can get informations regarding about 80 000 movies. This is a standard API that waiting for an HTTP request and returning a json.

## Informations
The API is written wyth Python through the framework Django and Django Rest Framework.<br>
API url: https://filmosaurus-api.net/ <br>

## Tutorial

### Movies
Search a movie => https://filmosaurus-api.net/api/v1/search?query={{keyword}}&page=1 <br>
The request will return a list of movies related to the searched keyword.
<br>
<br>
Get movie detail => https://filmosaurus-api.net/api/v1/movie/{{movieID}} <br>
Will return information regarding the searched movie.
<br>
<br>
Get poster from a movie => https://fimosaurus-api.net/api/v1/image/get?movie={{title}}&year={{year}}`<br>
Return the url of the poster.
<br>
<br>
Load ratings of a movie => https://filmosaurus-api.net/api/v1/ratings/load?movie={{title}}&year={{year}} <br>
Return the ratings for the selected movie (actually rating are from Allociné and IMDB)
<br>
<br>

### Authentication
Registration => https://filmosaurus-api.net/api/v1/dj-rest-auth/registration/ <br>
Return a token if creation is successfull
<br>
<br>
Login => https://filmosaurus-api.net/api/v1/dj-rest-auth/login/ <br>
You need to add the username, email and password in the body of your request. Token will be provided if the login is successfull.
<br>
<br>

### Watchlist
Load the watchlist => https://filmosaurus-api.net/api/v1/accounts/watchlist/list <br>
Authentication is required, token need to be added in the header of the request. <br>
example: ('Authorization': `Token ${token}`)<br>
Return the list of movies saved in watchlist.
<br>
<br>
Add in Watchlist => https://filmosaurus-api.net/api/v1/accounts/watchlist/add <br>
Authentication is required, token need to be added in the header of the request. <br>
example: ('Authorization': `Token ${token}`)<br>
<br>
<br>
Tagged as viewed => https://filmosaurus-api.net/api/v1/accounts/watchlist/update/seen/ <br>
Authentication is required, token need to be added in the header of the request. <br>
example: ('Authorization': `Token ${token}`)<br>