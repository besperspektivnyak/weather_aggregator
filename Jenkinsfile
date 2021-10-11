pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('my_docker')
    }
    stages {

        stage('Build') {

			steps {
				bat 'docker build -t besperspektivnyak/weather .'
			}
		}

		stage('Login') {

			steps {
				bat 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				bat 'docker push besperspektivnyak/weather'
			}
		}
}