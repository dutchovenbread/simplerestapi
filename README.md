# Simple REST API Deployment on AWS

This project deploys a simple REST API application on AWS using CloudFormation.  
It now uses Nginx as the web server and includes an S3 bucket for application data.

## Features

- **EC2 Instance**: Deployed in a public subnet, with Nginx installed and configured.
- **Nginx**: Serves static content from `/usr/share/nginx/html` and `/usr/share/nginx/html/secondary` via custom config (`webservice.conf`).
- **S3 Bucket**: Encrypted with AWS KMS and bucket key, deployed via a separate CloudFormation stack.
- **IAM Roles & Policies**: EC2 instance profile with permissions to access the S3 bucket.
- **Security Groups**: Allow HTTP (80), HTTPS (443), and application traffic (8080).
- **GitHub Actions OIDC**: IAM role for CI/CD deployments from GitHub Actions.

## Directory Structure

```
cloudformation_dynamic/
  application.yaml      # VPC, subnet, security group, IAM roles/policies
  bucket.yaml           # S3 bucket resource

cloudformation_static/
  cicd-role.yaml        # GitHub Actions OIDC provider and deployment role

application/
  configuration/
    webservice.conf     # Nginx config for custom routing
```

## Nginx Custom Routing

- Requests to `/other/filename.html` are served from `/usr/share/nginx/html/secondary/filename.html`.
- Requests to `/sws/` are proxied to `localhost:8080`.

## Deployment

1. **S3 Bucket Stack**  
   Deploy with:
   ```
   aws cloudformation deploy \
     --template-file cloudformation_dynamic/bucket.yaml \
     --stack-name simplerestapi-bucket \
     --capabilities CAPABILITY_NAMED_IAM \
     --parameter-overrides BucketName=simplerestapi-bucket-20251016
   ```

2. **Application Stack**  
   Deploy with:
   ```
   aws cloudformation deploy \
     --template-file cloudformation_dynamic/application.yaml \
     --stack-name simplerestapi-app \
     --capabilities CAPABILITY_NAMED_IAM
   ```

3. **CI/CD Role Stack**  
   Deploy with:
   ```
   aws cloudformation deploy \
     --template-file cloudformation_static/cicd-role.yaml \
     --stack-name simplerestapi-cicd-role \
     --capabilities CAPABILITY_NAMED_IAM
   ```

4. **Testing**
    Visit "http://<ipaddress>/sws/ to make sure the web service responds.

## Notes

- Update `webservice.conf` as needed for custom Nginx routing.
- Ensure your EC2 instance has access to the S3 bucket via IAM policy.
- Check security group rules for required ports.

---

For questions or further customization, see the CloudFormation templates or contact the repository maintainer.