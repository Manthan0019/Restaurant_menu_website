pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Manthan0019/Restaurant_menu_website.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'docker build -t restaurant-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop restaurant-container || true
                docker rm restaurant-container || true
                docker run -d -p 5000:5000 --name restaurant-container restaurant-app
                '''
            }
        }
    }
}