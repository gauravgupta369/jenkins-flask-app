pipeline {
    environment {
        BACKEND_AUTH = credentials('backend_auth')
    }
    parameters {
        string(name: 'branch', defaultValue: 'master', description: 'Branch Name')
    }
    agent {
        docker {
            image 'flask-app'
            args "-e BACKEND_AUTH_USR:$BACKEND_AUTH_USR"
            args "-e BACKEND_AUTH_PSW:$BACKEND_AUTH"
            args "-e branch: ${params.branch}"
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