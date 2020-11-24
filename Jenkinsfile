Pipeline{
  agent any
  stages{
    stage('Build'){
      steps{
        echo 'Building Docker Images'
        sh 'docker build -t myflaskapp2'
      }
    }
    stage('Test'){
      steps{
        echo 'Running flask application'
        sh 'docker run -p 5000:5000 --name myflaskapp2
      }
    } 
  }
}
