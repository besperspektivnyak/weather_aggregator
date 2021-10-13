// node {
//     checkout scm
//
//     docker.withRegistry('', 'my_docker') {
//
//         def customImage = docker.build("besperspektivnyak/weather")
//
//         /* Push the container to the custom Registry */
//         customImage.push()
//     }
// }


pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('my_docker')
	}

	stages {

		stage('Build') {

			steps {
				sh 'docker build -t besperspektivnyak/weather .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push besperspektivnyak/weather'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
