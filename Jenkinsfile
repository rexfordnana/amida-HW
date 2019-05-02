pipeline{
    agent any

    stages{
        stage('Build'){
            steps{
                echo 'Building'
            }
        }
        stage('Run unit test'){
            steps{
                echo 'Testing'
            }
        }
        stage('Deploy to dev'){
            steps{
                echo 'Deploying'
            }
        }
        stage('Trigger automation test'){
            steps{
                echo 'Running integration tests'
            }
        }
        stage('Deploy to qa'){
            steps{
                echo 'Deploying to qa'
            }
        }
    }

}