pipeline{
    agent any
    stages{
        stage("setup"){
            steps{
                bat "pip install -r  requirements.txt"
            }
        }
        stage("run"){
            steps{
                bat "python ml_pipeline.py"
            }
        }
        
    }
    post{
            success{
                echo "Success"
            }
            failure{
                echo  "Fail"
            }
        }
}