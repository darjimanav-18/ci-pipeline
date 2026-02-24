pipeline{
    agent any
    stages{
        stage("setup"){
            steps{
                bat "pip install requirements.txt"
            }
        }
        stage("run"){
            steps{
                bat "python ml_pipeline.py"
            }
        }
    }
}