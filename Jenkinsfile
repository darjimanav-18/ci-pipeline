pipeline{
    agent any
    stages("CI workFlow"){
        
        stage(""){
            echo "Installing Requiement "
            bat "pip install requirements.txt"
            echo "Runnig the python file"
            bat "python ml_pipeline.py"
        }
    }
    post{
        success{
            echo "Successfully run"
        }
        Failure{
            echo "code Failure"
        }
    }
}