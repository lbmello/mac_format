pipeline {
    agent none

    stages {
        agent { label 'general-usage && docker-proxy1' }
        stage('Prepare Environment') {
            steps {
                sh 'pip3 install unittest requests'
                sh 'python3 -m venv .venv'
                sh 'source .venv/bin/activate'
            }
        }

        stage('Tests') {
            agent { label 'general-usage && docker-proxy1' }
            steps {
                sh 'source .venv/bin/activate'
                sh 'python3 -m unittest tests/test_mac_format.py'
            }
        }
    }
}
