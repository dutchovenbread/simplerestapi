# CloudFormation Dynamic Templates

This directory contains CloudFormation templates that are deployed by the CI/CD pipeline.

## Templates

### application.yaml
Deploys the complete application infrastructure including:
- VPC with public subnet
- Internet Gateway
- EC2 instance with public IP
- Security groups (allowing HTTP, HTTPS, and port 8080)
- IAM role for the EC2 instance
- User data script to bootstrap the application

The application runs on port 8080 and is automatically started as a systemd service.

#### Parameters

- `InstanceType`: EC2 instance type (default: t3.micro)
- `LatestAmiId`: Amazon Linux 2023 AMI ID (automatically fetched from SSM)
- `KeyName`: Optional EC2 key pair for SSH access

#### Outputs

- `InstanceId`: The EC2 instance ID
- `PublicIP`: Public IP address of the instance
- `PublicDNS`: Public DNS name of the instance
- `ApiUrl`: Full URL to access the REST API
