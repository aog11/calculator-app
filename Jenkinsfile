pipeline {
    agent any

    stages {
        stage('Testing') {
            steps {
                sh '/usr/bin/python3 /var/lib/jenkins/calculator-app-py/calculator.py 1 2'
            }
        }
    }
}