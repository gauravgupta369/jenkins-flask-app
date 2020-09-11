pipeline {
    // environment {
    //     BACKEND_AUTH = credentials('backend_auth')
    // }
    agent none
    parameters {
        string(name: 'branch', defaultValue: 'master', description: 'Branch Name')
    }
    stages {
        stage('unit test') {
             agent {
                docker {
                    image "flask-app"
                    // args "-e BACKEND_AUTH_USR:${env.BACKEND_AUTH_USR}"
                    // args "-e BACKEND_AUTH_PSW:${env.BACKEND_AUTH_PSW}"
                    args "-e branch:${params.branch}"
                    args "-e ip:${params.ip}"
                    args "-e port:${params.port}"
                    // registryUrl 'https://myregistry.com/'
                    // registryCredentialsId 'myPredefinedCredentialsInJenkins'
                }
            }
            steps {
                sh 'python test.py'
            }
        }
    }
}