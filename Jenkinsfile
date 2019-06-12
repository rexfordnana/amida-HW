pipeline{
    agent { dockerfile true}

    stages{
        stage('Build'){
            steps{
                sh 'pwd'
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
