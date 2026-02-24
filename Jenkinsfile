pipeline{
    agent any
    stages{
        step("install and run"){
            stage{
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