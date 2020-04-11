pipeline {
	agent {
		dockerfile {
			args '-it -p 56733:80'
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