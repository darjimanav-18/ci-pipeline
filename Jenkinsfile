pipeline{
    agent any
    stages{
        stage("Requirements install"){
            echo "Installing Requiement "
            bat "python -m pip install -u requirements.txt"
        }
        stage("Running the ml_pipeline file"){
            echo "Runnig the python file"
            bat "python ml_pipeline.py"
        }
    }
    post{
        success{
            echo "Successfully run"
        }
        fail{
            echo "code Failure"
        }
    }
}