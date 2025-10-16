# CloudFormation Static Templates

This directory contains CloudFormation templates for infrastructure that is not deployed by the CI/CD pipeline.

## Templates

### cicd-role.yaml
Creates the IAM role and OIDC provider needed for GitHub Actions to deploy to AWS.

#### Deployment

Deploy this template manually before setting up the CI/CD pipeline:

```bash
aws cloudformation deploy \
  --template-file cicd-role.yaml \
  --stack-name static-cicd-role \
  --capabilities CAPABILITY_NAMED_IAM \
  --profile <profile name>
  --region us-east-2

```

After deployment, get the role ARN:

```bash
aws cloudformation describe-stacks \
  --stack-name github-actions-cicd-role \
  --query 'Stacks[0].Outputs[?OutputKey==`RoleArn`].OutputValue' \
  --output text
```

Add this ARN as a secret named `AWS_ROLE_ARN` in your GitHub repository settings.
