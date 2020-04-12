node {
	def testImage = null
	stage('Build Test Image') {
		checkout scm
		def dockerfile = "test.Dockerfile"
		testImage = docker.build("test-image", "-f ${dockerfile} ./")
	}
	stage('Test') {
		testImage.inside {
			sh 'cd /var/www'
			sh 'ls -la'
			sh 'ls -la /var/www'
			sh 'pytest'
		}
	}
}