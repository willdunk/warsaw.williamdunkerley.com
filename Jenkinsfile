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
	stage('Deploy') {
		sh 'scp -r ./* paris.williamdunkerley.com:/home/jenkins/amsterdam.williamdunkerley.com'
		sh 'ssh paris.williamdunkerley.com \'cd amsterdam.williamdunkerley.com && sudo /bin/bash /var/www/amsterdam.williamdunkerley.com/start.sh -n amsterdam.williamdunkerley.com -p 56733\''
		sh 'ssh paris.williamdunkerley.com \'sudo /usr/sbin/service nginx restart\''
	}
}