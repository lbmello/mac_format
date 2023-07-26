pipeline {
    agent {
        docker { 
            image 'python'
        }
    }

    stages {
        stage('Prepare Environment') {
            steps {
                sh 'python3 -m venv .venv'
                sh 'source .venv/bin/activate'
                sh 'pip3 install requests'
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
