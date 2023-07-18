pipeline {
    agent any

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
                sh 'python -m unittest tests/test_mac_format.py'
            }
        }
    }
}
