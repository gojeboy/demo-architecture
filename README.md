## Install docker and docker-compose

## clone the repo

git clone git@github.com:gojeboy/demo-architecture.git

## navigate to the project

cd demo-architecture

## build and downlaod docker images

docker-compose build

## run containers

docker-compose up -d

## check the running containers

docker ps

## Important to note. As it project is, it's not great with data migrations. it resets the database on every deployment
