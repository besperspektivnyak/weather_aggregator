pipeline {
    agent any
    environment {
        DOCKER = credentials('my_docker')
    }
    stages {
        stage('Docker push') {
            steps {
                docker build -t besperspektivnyak/weather .
                docker login -u DOCKER_USR -p DOCKER_PSW
                docker image push besperspektivnyak/weather
            }
        }
    }
}