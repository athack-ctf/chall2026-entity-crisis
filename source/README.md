# Running The Challenge

Navigate to source/main:
> cd ./source./main

Build the docker image
> docker build -t entity-crisis .


Run the challenge:
> docker run --rm -p 8000:8000 entity-crisis