node {
	def testImage = null  
	stage('Build Image') {
		checkout scm
		sh 'pwd'
		testImage = docker.build("test-image", "test.Dockerfile")
	}
	stage('Test') {
		testImage.inside {
			sh 'pwd'
		}
	}
}