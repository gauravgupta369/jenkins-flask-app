pipeline {
    agent { dockerfile true }
    stage('test') {
        steps {
            sh 'python test.py'
        }
    }
}