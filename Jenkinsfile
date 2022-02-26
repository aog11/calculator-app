pipeline {
    agent any
    environment {
        BRANCH='upgrades'
    }

    stages {
        stage('Building') {
            steps {
                sh """
                    rm -rf ${env.WORKSPACE}/calculator-app-py/
                    git clone -b $BRANCH git@github.com:aog11/calculator-app-py.git
                """
            }
        }
        stage('Testing') {
            steps {
                sh "/usr/bin/python3 ${env.WORKSPACE}/calculator-app-py/calculator.py"
            }
        }
        stage('Cleaning') {
            steps{
                sh """
                    rm -rf ${env.WORKSPACE}/calculator-app-py/
                """
            }
        }
    }
}