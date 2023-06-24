pipeline {
    agent any
    
    stages {
    
        stage('CI') {
            steps {
                
                    dir('Crowdfunding') {
                        sh '''

                        docker-compose up &
                        '''
                    }
            }
        }   
    }
}
