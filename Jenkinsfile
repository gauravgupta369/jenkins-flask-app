pipeline {
    options { timeout(time: 5, unit: 'MINUTES') }
    environment {
        BACKEND_AUTH = credentials('my-creds-file')
    }
    parameters {
        string(name: 'branch', defaultValue: 'master', description: 'Branch Name')
        string(name: 'container_name', defaultValue: 'my-flask-app', description: 'Name of Container')
    }
    agent {
        docker {
            image "flask-app"
            args "-e BACKEND_AUTH_USR:${env.BACKEND_AUTH}"
        }
    }
    // agent {
    //     dockerfile {
    //         filename 'Dockerfile'
    //         args "--name ${params.container_name}"
    //         // registryUrl 'https://myregistry.com/'
    //         // registryCredentialsId 'myPredefinedCredentialsInJenkins'
    //     }
    // }

    stages {
        stage ('Clone Source') {
            steps {
                script {
                    def branches = ['master', 'development']
                    if (!(params.branch in branches)) {
                        throw new Exception("Invalid Branch")
                    }
                }
                git branch: "${params.branch}", url: "https://github.com/gauravgupta369/jenkins-flask-app.git/"
            }
        }
        // stage('Unit Test') {
        //     options { timeout(time: 2, unit: 'MINUTES') }
        //     when {
        //         anyOf {
        //             expression { params.branch == 'master' || params.branch == 'stage' }
        //             expression { params.branch == 'development' }
        //         }
        //     }
        //     steps {
        //         sh 'python test.py'
        //     }
        // }
        // stage('Pospector Test') {
        //     options { timeout(time: 2, unit: 'MINUTES') }
        //     when {
        //         equals expected: 'master', actual: "${params.branch}"
        //     }
        //     steps{
        //         sh 'prospector'
        //     }
        // }
        stage('Deploy') {
            steps {
                sh "echo ${creds.py}"
                sh 'python fabfile1.py'
            }
        }
    }
}