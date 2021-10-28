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
        steps("Deploy to Kubernetes") {
            steps {
                sshagent(['k8s-jenkins']) {
                    sh 'scp -r -o StrictHostKeyChecking=no deployment.yaml root@94.26.239.26:/root'
                    script{
                        try{
                            sh 'ssh root@94.26.239.26 kubectl apply -f /root/deployment.yaml --kubeconfig=/root/.kube/config'
                        }
                        catch(error) {
                        }
                    }
                }
            }
        }
    }
}

