pipeline {
    // environment {
    //     BACKEND_AUTH = credentials('backend_auth')
    // }
    parameters {
        string(name: 'branch', defaultValue: 'master', description: 'Branch Name')
    }
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
    options { timeout(time: 5, unit: 'MINUTES') }
    stages {
        stage ('Clone Source') {
            steps {
                script {
                    def branches = ['master', 'development', 'stage']
                    if (!(params.branch in branches)) {
                        throw new Exception("Invalid Branch")
                    }
                }
                git branch: "${params.branch}", url: "https://github.com/gauravgupta369/jenkins-flask-app.git/"
            }
        }
        stage('Unit Test') {
            options { timeout(time: 2, unit: 'MINUTES') }
            when {
                anyOf {
                    expression { params.branch == 'master' }
                    expression { params.branch == 'stage' }
                }
            }
            steps {
                sh 'python test.py'
            }
        }
        stage('Pospector Test') {
            options { timeout(time: 2, unit: 'MINUTES') }
            when {
                equals expected: 'master', actual: "${params.branch}"
            }
            steps{
                sh 'prospector'
            }
        }
    }
}