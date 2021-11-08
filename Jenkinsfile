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
                    withKubeConfig([credentialsId: 'kube_config', serverUrl: 'https://94.26.239.26:6443']) {
                        bat 'kubectl apply -f deployment.yaml'
                    }
                }
            }

        }
    }
//     post {
//         always {
//             bat 'docker logout'
//             CleanWs()
//         }
//     }
}

