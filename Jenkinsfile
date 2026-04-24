pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build') {
            steps {
                echo 'No build required for HTML'
            }
        }

        stage('Test') {
            steps {
                echo 'Checking index.html'
                sh 'if [ -f index.html ]; then echo "File exists"; else exit 1; fi'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to XAMPP htdocs'
                sh 'cp -r * /Applications/XAMPP/htdocs/'
            }
        }
    }
}