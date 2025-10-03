# Simple REST API

A simple REST API deployed through a DevOps pipeline to AWS using GitHub Actions and CloudFormation.

## Project Structure

```
.
├── application/              # Python REST API application
│   ├── app.py               # Main application code
│   ├── requirements.txt     # Python dependencies
│   └── README.md            # Application documentation
├── cloudformation_static/   # CloudFormation for manual deployment
│   ├── cicd-role.yaml      # CI/CD IAM role template
│   └── README.md           # Static templates documentation
├── cloudformation_dynamic/  # CloudFormation for automated deployment
│   ├── application.yaml    # Application infrastructure template
│   └── README.md           # Dynamic templates documentation
└── .github/workflows/      # GitHub Actions workflows
    └── deploy.yaml         # CI/CD deployment workflow
```

## Architecture

The application is deployed on a single EC2 instance with:
- Public IP address for direct access
- VPC with public subnet and Internet Gateway
- Security groups allowing HTTP/HTTPS and custom port 8080
- Systemd service for automatic application startup
- IAM role with CloudWatch and SSM permissions

## Setup

### 1. Deploy CI/CD Role (One-time Setup)

First, manually deploy the CloudFormation stack that creates the GitHub Actions role:

```bash
cd cloudformation_static
aws cloudformation deploy \
  --template-file cicd-role.yaml \
  --stack-name github-actions-cicd-role \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    GitHubOrg=dutchovenbread \
    GitHubRepo=simplerestapi
```

Get the role ARN:

```bash
aws cloudformation describe-stacks \
  --stack-name github-actions-cicd-role \
  --query 'Stacks[0].Outputs[?OutputKey==`RoleArn`].OutputValue' \
  --output text
```

### 2. Configure GitHub Secrets

Add the following secret to your GitHub repository:
- `AWS_ROLE_ARN`: The ARN from the previous step

### 3. Deploy Application

Push code to the `main` branch or manually trigger the workflow to deploy the application.

## API Endpoints

Once deployed, the API provides:

- `GET /` - API status and available endpoints
- `GET /health` - Health check endpoint

## Local Development

To run the application locally:

```bash
cd application
python3 app.py
```

Access the API at `http://localhost:8080`

## CI/CD Pipeline

The GitHub Actions workflow automatically:
1. Validates the CloudFormation template
2. Deploys/updates the infrastructure stack
3. Updates the application code on the EC2 instance
4. Verifies the deployment

## License

Apache License 2.0 - See LICENSE file for details
