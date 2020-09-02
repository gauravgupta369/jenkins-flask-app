pipeline {
    agent none
    stages {
        stage('test') {
            agent { dockerfile true }
            steps {
                sh 'python test.py'
            }
        }
    }
}