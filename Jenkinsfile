node('docker-host') {
	checkout scm
	docker.image({
		def dockerfile = "Dockerfile"
		def buildImage = docker.build("my-image-${env.GIT_COMMIT}", "-f $dockerfile .")
		buildImage.inside('-v /tmp:/tmp') {
			echo "inside docker"
		}
	}
}