pipeline{
    agent any
    stages("CI workFlow"){
        
        stage(""){
            step{
                bat "pip install requirements.txt"
                bat "python ml_pipeline.py"

            }

        }
    }
    post{
        success{
            echo "Successfully run"
        }
        failure{
            echo "code Failure"
        }
    }
}