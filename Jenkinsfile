pipeline {
    agent any
    
    stages {
    
        stage('CI') {
            steps {
                
                    dir('Crowdfunding') {
                        sh '''
                        docker build -t mohamedsalahacc/crowd-appjenkins .
                        docker-compose up
                        '''
                    }
            }
        }   
    }
}
