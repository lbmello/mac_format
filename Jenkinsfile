pipeline {
    agent any

    stages {
        stage('Prepare Environment') {
            steps {
                sh 'python -m pip install unittest requests'
                sh 'python -m venv .venv'
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
