pipeline{
    agent any
    stages{
        stage("setup"){
            step{
                bat "pip install requirements.txt"
            }
        }
        stage("run"){
            step{
                bat "python ml_pipeline.py"
            }
        }
    }
}