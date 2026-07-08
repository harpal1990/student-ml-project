pipeline {

    agent any

    environment {
        IMAGE_NAME = "student-m1-api"
        IMAGE_TAG = "${BUILD_NUMBER}"
        K8S_NAMESPACE = "mlops-dev"
    }

    options {
        timestamps()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Environment') {
            steps {
                sh '''
                echo "===== Environment ====="
                whoami
                pwd
                docker --version
                kubectl version --client
                kind version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv

                . venv/bin/activate

                pip install --upgrade pip

                pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                . venv/bin/activate

                python src/train.py
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build \
                -t ${IMAGE_NAME}:${IMAGE_TAG} \
                .
                '''
            }
        }

        stage('Load Image into Kind') {
            steps {
                sh '''
                kind load docker-image \
                ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Update Deployment Image') {
            steps {
                sh '''
                kubectl set image deployment/student-ml-api \
                student-ml-api=${IMAGE_NAME}:${IMAGE_TAG} \
                -n ${K8S_NAMESPACE}
                '''
            }
        }

        stage('Verify Rollout') {
            steps {
                sh '''
                kubectl rollout status deployment/student-ml-api \
                -n ${K8S_NAMESPACE}
                '''
            }
        }

        stage('Smoke Test') {
            steps {
                sh '''
                kubectl get pods -n ${K8S_NAMESPACE}

                kubectl get svc -n ${K8S_NAMESPACE}
                '''
            }
        }

    }

    post {

        always {

            sh '''
            docker image prune -f
            '''

        }

        success {

            echo "=================================="
            echo "Deployment Successful"
            echo "=================================="

        }

        failure {

            echo "=================================="
            echo "Deployment Failed"
            echo "=================================="

        }

    }

}