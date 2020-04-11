node {
	def testImage = null
	stage('Build Image') {
		checkout scm
		sh 'pwd'
		def dockerfile = "test.Dockerfile"
		testImage = docker.build("test-image", "-f ${dockerfile}")
	}
	stage('Test') {
		testImage.inside {
			sh 'pwd'
		}
	}
}