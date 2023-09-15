pipeline{
    agent any
    
    stages {
        stage('pull code'){
            steps{
               git credentialsId: 'github user password', url: 'https://github.com/mokcoo/rpa.git'
            }
        }
        stage("build project"){
            steps{
                sh '''echo "start"
                    echo "complete"'''
            }
        }
        stage("deploy project"){
            steps{
                sshPublisher(publishers: [sshPublisherDesc(configName: '192.168.74.137', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'echo "success"', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: 'py_test/', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '*.py')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
            }
        }
    }
}
