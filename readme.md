
## Book request

This is a library service. Wwe are adding a ​/request ​endpoint which allows a user to request a book by title so that they can later be emailed when it is available. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* If you don’t have them installed yet, install Docker and docker-compose.

### Installing

1. Clone the repository

```sh
$ git clone https://github.com/luciostocco/library.git
```

2. Go to project folder

```sh
$ cd xxxxx
```

3. In order to run the our dockerized app, we will execute the following command from the terminal:

```sh
$ docker-compose up
```

4. You can see the image being built, the packages installed according to the requirements.txt, etc. If everything went right, you will see the following line:

```sh
$ app_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

5. We can find out that everything is running as expected by typing this url in a browser or using curl the follows URLS:

```sh
Add Request Endpoint:
=============================
$ curl -v -H POST http://0.0.0.0:5000/request -H "Content-Type: application/json" -d "{ \"email\":  \"lucio@mail.com\", \"title\": \"Book 1\"}"

Retrieve Request(s) Endpoint
=============================
Get a specific Id
=================
$ curl -v -H GET http://0.0.0.0:5000/request/1 -H "Content-Type: application/json"

Get all Ids
=================
$ curl -v -H GET http://0.0.0.0:5000/request -H "Content-Type: application/json"

Delete Request Endpoint
=============================
curl -X DELETE http://0.0.0.0:5000/request/3 
```

5. The following books are available for requisition: (initial seed)
   POST request endpoint will only be accepted for these books titles

```sh
Book 1
Book 2
Book 3
Book 4
Book 5
```
