pipeline {
	agent {
		dockerfile {
			additionalBuildArgs  '-t'
			args '-it -d -p 56733:80'
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