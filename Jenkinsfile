node {
    checkout scm

    docker.withRegistry('https://registry.example.com', 'my_docker') {

        def customImage = docker.build("besperspektivnyak/weather")

        /* Push the container to the custom Registry */
        customImage.push()
    }
}