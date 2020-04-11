pipeline {
	stages {
		stage('Test') {
			agent {
				dockerfile {
					filename 'test.Dockerfile'
				}
			}
			steps {
				sh 'pwd'
			}
		}
	}
}