pipeline {
    stages {
        stage ('Checkout'){
            steps {
                node ('Checkout') {
                    checkout scm
                }
            }
        }
        stage ('Push'){
            steps {
                node ('Push') {

                    docker.withRegistry('', 'my_docker') {

                    def customImage = docker.build("besperspektivnyak/weather")

                    /* Push the container to the custom Registry */
                    customImage.push()
                    }
                }
            }
        }
    }
}

