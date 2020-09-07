pipeline {
    environment {
        BACKEND_AUTH = credentials('backend_auth')
    }
    agent {
        docker {
            image 'flask-app'
            args "-e BACKEND_AUTH_USR:$BACKEND_AUTH"
            args "-e BACKEND_AUTH_PSW:$BACKEND_AUTH"
            // registryUrl 'https://myregistry.com/'
            // registryCredentialsId 'myPredefinedCredentialsInJenkins'
        }
    }
    stages {
        stage('test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}