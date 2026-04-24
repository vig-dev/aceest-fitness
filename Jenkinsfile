pipeline {
    agent any

    environment {
        IMAGE = "vighneshdevane/aceest-fitness"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE:latest .'
            }
        }

        stage('Run Tests in Container') {
            steps {
                sh 'docker run $IMAGE:latest pytest -v'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'TOKEN')]) {
                    sh '''
                    echo $TOKEN | docker login -u $USER --password-stdin
                    docker push $IMAGE:latest
                    '''
                }
            }
        }
    }
}