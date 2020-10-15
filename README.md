# Banking System Template



## Getting Started

**Step 1:** Make sure git is installed on your os. I will be using macOS for the project.

On macOS, you can install the git using Homebrew using ```brew install git```

**Step 2:** Clone the project into your local machine using below command.

```https://github.com/Swapnay/banking.git```

### Prerequisites

**1. Docker**

Make sure you have Docker installed. Please follow the below link for official documentation from Docker to install latest version of docker on your os. For this project I am using Docker CE (18.09).

```https://docs.docker.com/docker-for-mac/install/```

### Installing

**Step 1:** Change to the directory where the project was cloned in previous step.

```
cd banking
```

**Step 2:** Make sure Docker is up and running. You can start the docker engine from desktop icon on Mac.

**Step 3:** Run

```
docker-compose up --build -d
docker exec -it banking /bin/bash
cd app
python bank.py
```
Use employee details from ```bnking/conf/docker-entrypoint-initdb.d/dbinit.sql``` to login to employee workflow.

**Step 4:** Verify DB is up and running and tables are created

Use any of the database clients like MySQL workbench or SQLDeveloper. In my case, I am using the Pycharm DB plugin. Make sure you have the driver installed for the MySQL db running on the client you are using.

Connect to MySQL database using the properties specified in ```docker-compose.yml``` file with host as ```mysql_test```.


## Deployment

## Built With

* [Docker](http://www.dropwizard.io/1.0.2/docs/) -  Deployment model
* [Python](https://rometools.github.io/rome/) - programming language
* [pip](https://rometools.github.io/rome/) - Package and dependency manager
* [MySQL](https://rometools.github.io/rome/) - Database
* [Sqlalchemy](https://www.sqlalchemy.org/download.html) Python ORM

## Contributing

## Versioning

## Authors

## License

## Acknowledgments
