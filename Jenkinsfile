pipeline {
    agent {
        docker { image 'python:3.12.0b4-alpine3.18' }
    }

    stages {
        stage('Prepare Environment') {
            steps {
                sh 'pip3 install unittest requests'
                sh 'python3 -m venv .venv'
                sh 'source .venv/bin/activate'
            }
        }

        stage('Tests') {
            steps {
                sh 'source .venv/bin/activate'
                sh 'python3 -m unittest tests/test_mac_format.py'
            }
        }
    }
}
