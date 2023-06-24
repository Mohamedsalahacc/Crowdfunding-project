pipeline {
    agent any
    
    stages {
    
        stage('CI') {
            steps {
                
                    dir('Crowdfunding') {
                        sh '''
                        chmod 777 manage.py
                        docker-compose up &
                        '''
                    }
            }
        }   
    }
}
