pipeline {

    agent any

    stages {
        stage ('Checkout'){
            steps {
                    checkout scm
            }
        }
        stage ('Push'){
            steps {
                    script {
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

