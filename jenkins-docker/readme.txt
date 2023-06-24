docker build -t jenkins-docker .


docker run -d -p 8081:8080 -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker
