# End-to-End Machine Learning Project with MLflow

Excited to share my latest project - an End-to-end Machine Learning MLOPS Project focused on predictive maintenance to predict machine failure! 🛠️ Leveraging CI/CD pipelines, I streamlined the development process. Utilizing modernized code with OOP concepts, I ensured efficiency and scalability. In data validation, I employed MLflow to fine-tune model hyperparameters, achieving impressive results:

## Parameters:
- l1_ratio: 0.0
- max_iter: 135
- penalty: l2
- solver: lbfgs

## Metrics:
- R2: 0.9869
- RMSE: 0.02
- MAE: 0.0004

By integrating Data Version Control (DVC.ai) for data management and GitHub Actions for CI/CD workflows, the process was automated seamlessly. With each new commit, the workflow automatically detects changes, creates a new Docker image, and pushes it to Amazon Web Services (AWS) Elastic Container Registry (ECR). Subsequently, the Docker image is pulled by the EC2 instance to run the UI developed with Streamlit. This automated process ensures that the latest changes are reflected in the deployed application, maintaining efficiency and consistency throughout the development cycle.

Check out the deployed UI here: [http://3.110.195.10:8501/](http://3.110.195.10:8501/) 🌐

## Workflows:
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

## How to run?

### STEPS:

1. Clone the repository
```bash
https://github.com/Smith-S-S/End-to-End-Data-Science-Project-Using-MLOPS.git
```

2. Create a conda environment after opening the repository
```bash
conda create -n mlproj python=3.8 -y
conda activate mlproj
```

3. Install the requirements
```bash
pip install -r requirements.txt
```

4. Run the following command
```bash
python app.py
```

5. Open your local host and port

## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


## DagsHub

[DagsHub](https://dagshub.com/)



Run this to export as env variables:

## AWS CICD Deployment with GitHub Actions

1. Login to AWS console.
2. Create IAM user for deployment with specific access:
   - EC2 access: Virtual machine
   - ECR: Elastic Container Registry to save your Docker image in AWS
3. Create ECR repo to store/save Docker image
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install Docker in EC2 Machine
6. Configure EC2 as self-hosted runner
7. Setup GitHub secrets:
   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_REGION
   - AWS_ECR_LOGIN_URI
   - ECR_REPOSITORY_NAME

## Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu
