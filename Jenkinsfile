node {
	String restartNginx = "sudo /usr/sbin/service nginx restart"
	def testImage = null
	String testImageName = 'defaulttestimage'
	String testDockerfile = "test.Dockerfile"
	String remoteServer = "paris.williamdunkerley.com"
	String environmentName = null
	String environmentDockerfile = null
	String appContainerPort = null
	if (env.BRANCH_NAME == "master") {
		environmentName = 'amsterdam';
		appContainerPort = '56733';
		environmentOption = 'prod.';
	}
	if (env.BRANCH_NAME == "release") {
		environmentName = 'santiago';
		appContainerPort = '56734';
		environmentOption = 'qa.';
	}
	if (env.BRANCH_NAME.contains("feature/")) {
		environmentName = 'prague';
		appContainerPort = '56735';
		environmentOption = 'dev.';
	}

	stage('Build Test Image') {
		checkout scm
		testImage = docker.build("${testImageName}", ". -f ./Dockerfiles/${testDockerfile}")
	}
	// stage('Test') {
	// 	testImage.inside {
	// 		sh 'pytest'
	// 	}
	// }
	if (environmentName != null && appContainerPort != null) {
		stage('Deploy') {
			String appImageName = "${environmentName}.williamdunkerley.com"
			String startContainer = "cd ${environmentName}.williamdunkerley.com && sudo /bin/bash /var/www/${environmentName}.williamdunkerley.com/start.sh -n ${appImageName} -p ${appContainerPort} -e ${environmentOption}"
			sh "scp -r ./* ${remoteServer}:/home/jenkins/${environmentName}.williamdunkerley.com"
			sh "ssh ${remoteServer} \'${startContainer}\'"
			sh "ssh ${remoteServer} \'${restartNginx}\'"
		}	
	}
}