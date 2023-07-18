pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git clone 'https://github.com/lbmello/mac_format/'
            }
        }

        stage('Prepare Environment') {
            steps {
                sh pip3 install unittest requests
                sh python3 -m venv .venv
                sh source .venv/bin/activate
            }
        }

        stage('Tests') {
            steps {
                sh source .venv/bin/activate
                sh 'python -m unittest tests/test_mac_format.py'
            }
        }
    }
}
