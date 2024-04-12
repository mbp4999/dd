pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code repository
                git 'github.com:mbp4999/demo.git'
            }
        }

        stage('Code Scanning') {
    steps {
        // Install Bandit
        sh 'pip install bandit'

        // Run Bandit and save the HTML report
        sh 'bandit -r . --exclude "*/pip/*" -f html -o bandit_report.html'
    }
}
        
        stage('Run Unit Tests') {
            steps {
                // Install dependencies if needed
                sh 'pip install -r requirements.txt'
                
                // Run unit tests
                sh 'python -m unittest discover -s tests -p "test_*.py"'
            }
            
            post {
                always {
                    // Archive test results
                    junit 'path/to/test/reports/**/*.xml'
                }
            }
        }
    }
    
    post {
        always {
            // Archive HTML report
            archiveArtifacts 'report.html'
        }
    }
    
    // Add more stages, post-build actions, notifications, etc. as needed
}

