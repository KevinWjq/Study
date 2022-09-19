pipeline {
    agent {
      label 'web2'
    }

    tools {
      allure 'allure'
      git 'Default'
    }

    stages {
        stage('Clean'){
            steps{
                sh 'rm -rf allure junit.xml'
            }
        }
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git 'https://github.com/KevinWjq/Study.git'

            }
        }
        stage('Tests'){
            parallel {
                stage('Test2'){
                    steps {
                        sh "echo test2"
                    }
                }
                stage('Test3'){
                    steps {
                        sh "echo test3"
                    }
                }
                stage('Test1'){
                    steps {
                        sh "pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/"
                        sh "pytest --alluredir=allure --junitxml=junit.xml geektime/service/petclinic/"
                    }
                    post {
                        // If Maven was able to run the tests, even if some of the test
                        // failed, record the test results and archive the jar file.
                        success {
                            junit 'junit.xml'
                            archiveArtifacts 'junit.xml'
                            allure includeProperties: false,jdk: '',results:[[path:'allure']
						}
					}
				}
			}
		}
	}
}