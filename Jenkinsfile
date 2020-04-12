node {
	def appname = "warsaw"
	def dockerfile = null
	def testImage = null
	stage('Build Test Image') {
		checkout scm
		dockerfile = "test.Dockerfile"
		testImage = docker.build(appname, "-f ${dockerfile} ./")
	}
	stage('Test') {
		testImage.inside {
			sh 'pytest'
		}
	}
}