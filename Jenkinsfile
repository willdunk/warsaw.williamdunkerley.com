node {
	String restartNginx = "sudo /usr/sbin/service nginx restart"
	String testImage = null
	String testImageName = 'defaultTestImage'
	String testDockerfile = "test.Dockerfile"
	String remoteServer = "paris.williamdunkerley.com"
	String environmentName = null
	String appContainerPort = null
	if (env.BRANCH_NAME == "master") {
		environmentName = 'amsterdam';
		appContainerPort = '56733';
	}
	if (env.BRANCH_NAME == "release") {
		environmentName = 'santiago';
		appContainerPort = '56734';
	}
	if (env.BRANCH_NAME.contains("feature/")) {
		environmentName = 'prague';
		appContainerPort = '56735';
	}

	stage('Build Test Image') {
		checkout scm
		testImage = docker.build(testImageName, "-f ${testDockerfile} ./")
	}
	stage('Test') {
		testImage.inside {
			sh 'pytest'
		}
	}
	if (environmentName != null && appContainerPort != null) {
		stage('Deploy') {
			String appImageName = "${environmentName}.williamdunkerley.com"
			String startContainer = "cd ${environmentName}.williamdunkerley.com && sudo /bin/bash /var/www/${environmentName}.williamdunkerley.com/start.sh -n ${appImageName} -p ${appContainerPort}"
			sh "scp -r ./* ${remoteServer}:/home/jenkins/${environmentName}.williamdunkerley.com"
			sh "ssh ${remoteServer} \'${startContainer}\'"
			sh "ssh ${remoteServer} \'${restartNginx}\'"
		}	
	}
}