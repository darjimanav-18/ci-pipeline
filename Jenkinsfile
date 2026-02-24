pipeline{
    agent any
    stages{
        
            stage{
                bat "pip install requirements.txt"
                bat "python ml_pipeline.py"

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