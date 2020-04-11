pipeline {
	agent {
		dockerfile {
			additionalBuildArgs  '-t docker.test'
			args '-it -d -p 56733:80 --name=docker.test -v $PWD:/app docker.test'
		}
	}
	stages {
		stage('Test') {
			steps {
				sh 'pwd'
			}
		}
	}
}