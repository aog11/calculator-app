pipeline {
    agent any

    stages {
        stage('Building') {
            steps {
                sh 'git@github.com:aog11/calculator-app-py.git'
            }
        }
        stage('Testing') {
            steps {
                sh '/usr/bin/python3 /var/lib/jenkins/calculator-app-py/calculator.py 1 2'
            }
        }
    }
}