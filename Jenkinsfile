pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                sh '''
                which python || true
                which python3 || true
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python -m pip install -r requirements.txt || python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                python -m pytest || python3 -m pytest
                '''
            }
        }
    }
}