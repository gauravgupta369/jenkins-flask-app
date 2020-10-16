pipeline {
    options { timeout(time: 5, unit: 'MINUTES') }
    environment {
        // BACKEND_AUTH = credentials('backend_auth')
        BACKEND_PEM = credentials('backend-pem')
    }
    parameters {
        string(name: 'branch', defaultValue: 'master', description: 'Branch Name')
        // string(name: 'ip', defaultValue: '', description: 'IP Address')
        // string(name: 'port', defaultValue: '22', description: 'Port')
    }
    agent {
        docker {
            image "python-flask-app"
            // args "-e ip:${params.ip}"
            // args "-e port:${params.port}"
            // args "-e BACKEND_AUTH_USR:${env.BACKEND_AUTH}"
            // args "-e BACKEND_AUTH_PSW:${env.BACKEND_AUTH}"
        }
    }
    stages {
        stage ('Clone Repository') {
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
        stage('Dev Deploy') {
            when {
                expression { params.branch == 'development' || params.branch == 'master' }
            }
            steps {
                sh "cat ${BACKEND_PEM} > backend.pem"
                sh 'python fabfile_dev.py'
            }
        }
    }
    post {
        always {
            sh "rm backend.pem"
        }
    }
}