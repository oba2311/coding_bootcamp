

### kill / stop all running containers:
`docker stop $(docker ps -q)`

<!-- consider adding the -a flag -->


### Delete all 'untagged/dangling' (<none>) images
`docker rmi $(docker images -q -f dangling=true)`


### Push existing image to DockerHub:
docker login
docker tag IMAGE_NAME oba2311/IMAGE_NAME
docker push oba2311/IMAGE_NAME
