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
                        customImage.push("${env.BUILD_NUMBER}")
                        customImage.push("latest")
                    }
                }
            }
        }
        stage("Deploy to Kubernetes") {
            steps {
                script {
                    withKubeConfig([credentialsId: 'kube_config', serverUrl: 'https://192.168.0.2:6443']) {
                        sh 'kubectl apply -f deployment.yaml'
                    }
                }
            }

        }
    }
}

