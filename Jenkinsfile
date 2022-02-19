pipeline {
    agent any

    stages {
        stage('Building') {
            steps {
                sh 'rm -rf ${env.WORKSPACE}/calculator-app-py/'
                sh 'git clone git@github.com:aog11/calculator-app-py.git'
            }
        }
        stage('Testing') {
            steps {
                sh '/usr/bin/python3 ${env.WORKSPACE}/calculator-app-py/calculator.py 1 2'
            }
        }
    }
}