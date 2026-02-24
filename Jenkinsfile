pipeline{
    agent any
    stages{
        steps
        {
            echo "Installing Requiement "
            bat "python -m pip install -u requirements.txt"
        }
        steps
        {
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