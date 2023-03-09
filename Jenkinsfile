pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/lbmello/mac_format/'
                sh python3 -m venv .venv
                sh source .venv/bin/activate
                sh pip3 install unittest requests
                python3 -m unittest tests/test_mac_format.py
            }
        }
    }
}