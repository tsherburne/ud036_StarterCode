<a href="https://github.com/tsherburne/udacity-fsdev-movie-trailer-project">
    <img src="http://inderecami.com/wp-content/uploads/2017/12/tomato-clip-art-fresh-14-free-clipart-panda-images.png" title="Fresh Tomatoes" align="right" height="60"/>
</a>
## Fresh Tomatoes Movie Trailers
This respository is for project #1 (Movie Trailers Website) 
for the [Udacity Fullstack Developers Nano Degree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
### Table of Contents

* [Installation](#installation)
* [Setup](#setup)
* [Running](#running)

### Installation
Clone the respository:

```
git clone https://github.com/tsherburne/udacity-fsdev-movie-trailer-project.git
cd udacity-fsdev-movie-trailer-project
```

### Setup
Define movies in `movies.txt`.  One row for each movie as:

```
<movie title>,<poster image url>,<movie youtube trailer url>
```

By default the Web Server listens on port 8080.  If desired, the port can be updated in `web_server.py`
### Running
Upon starting the Web Server, a static web page (`fresh_tomatoes.html`) will be created based on the movies defined in the `movies.txt`.

Start the Web Server:
```
python web_server.py
```

Open a browser and browse the movie trailers! Clicking on a movie will show the trailer!
```
https://<host>:8080
```