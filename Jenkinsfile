pipeline{
    agent any
    stages{
        steps("Requirements install"){
            echo "Installing Requiement "
            bat "python -m pip install -u requirements.txt"
        }
        steps("Running the ml_pipeline file"){
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