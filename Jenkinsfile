pipeline {
    options { timeout(time: 5, unit: 'MINUTES') }
    environment {
        BACKEND_AUTH = credentials('backend_auth')
    }
    parameters {
        string(name: 'branch', defaultValue: 'master', description: 'Branch Name')
        string(name: 'container_name', defaultValue: 'my-flask-app', description: 'Name of Container')
        string(name: 'ip', defaultValue: '', description: 'IP Address')
        string(name: 'port', defaultValue: '22', description: 'Port')
    }
    agent {
        docker {
            image "python-flask-app"
            args "-e ip:${params.ip}"
            args "-e port:${params.port}"
            args "-e BACKEND_AUTH_USR:${env.BACKEND_AUTH}"
            args "-e BACKEND_AUTH_PSW:${env.BACKEND_AUTH}"
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
                sh 'python fabfile.py'
            }
        }
    }
}