pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                apt-get update || true
                apt-get install -y python3 python3-pip || true
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest'
            }
        }
    }
}