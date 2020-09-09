pipeline {
    environment {
        BACKEND_AUTH = credentials('backend_auth')
    }
    parameters {
        string(name: 'branch', defaultValue: 'master', description: 'Branch Name')
    }
    agent {
        docker {
            image 'flask-all:v2'
            args "-e BACKEND_AUTH_USR:${env.BACKEND_AUTH_USR}"
            args "-e BACKEND_AUTH_PSW:${env.BACKEND_AUTH_PSW}"
            args "-e branch:${params.branch}"
            args "-e ip:${params.ip}"
            args "-e port:${params.port}"
            // registryUrl 'https://myregistry.com/'
            // registryCredentialsId 'myPredefinedCredentialsInJenkins'
        }
    }
    stages {
        stage('test') {
            // when {
            //     branch 'master'
            // }
            steps {
                sh 'python fabfile.py'
            }
        }
    }
}