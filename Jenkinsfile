node {
	stage('Preparation') {
		// Get some code from a GitHub repository
		git 'https://github.com/zaneswafford/weather_checker.git'
		echo 'hello'
		sh "pip3.5 install -r requirements.txt"
	}
	stage('Test') {
		catchError {
			if (isUnix()) {
				sh "python3.5 -m nose2 --plugin nose2.plugins.junitxml --junit-xml --with-coverage test"
				sh "python3.5 -m coverage xml"
			}
		}
		step([$class: 'Mailer', notifyEveryUnstableBuild: true, recipients: 'zane@otters.io', sendToIndividuals: true])
	}
	stage('Results') {
		junit 'nose2-junit.xml'
	}
}