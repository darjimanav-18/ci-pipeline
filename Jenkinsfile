pipeline{
    agent any
    stages{
        void setUp( "Installing Requiement ") {
            bat "pip install requirements.txt"
            
        }
        // {
        //     echo "Installing Requiement "
        //     echo "Runnig the python file"
        //     bat "python ml_pipeline.py"
        // }
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