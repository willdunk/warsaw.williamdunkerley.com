node {
	def testImage = null  
	stage('Build Image') {
		checkout scm
		testImage = docker.build("test-image", "test.Dockerfile")
	}
	stage('Test') {
		testImage.inside {
			sh 'pwd'
		}
	}
}