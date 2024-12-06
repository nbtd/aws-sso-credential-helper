# AWS SSO Credential Helper
![PyPI Downloads](https://static.pepy.tech/badge/aws-sso-credential-helper) 

Many organizations use AWS SSO (IAM Identity Center) to integrate AWS authentication with their own user directories.  
Additionally, after SSO authentication, it is often necessary to switch roles to dedicated roles for each product or project.

The AWS SSO Credential Helper assists with authentication through AWS SSO and obtaining temporary credentials for switch roles afterward.

During execution, you may be prompted to confirm authentication in your browser, so please allow it.  
The AWS SSO authentication token is cached in a file and reused within its validity period.  
The cache is saved as a file in the home directory and can be shared and used by multiple programs using the Credential Helper.

## Pypi
https://pypi.org/project/aws-sso-credential-helper/

## Usage

### 1. Create Instance
```python
from aws_sso_credential_helper import CredentialHelper

credential_helper = CredentialHelper(
    start_url="d-xxxxxxxxxx.awsapps.com/start",
    region_name="ap-northeast-1"
    )
```
 - start_url: URL of the AWS access portal
 - region_name: Region of the IAM Identity Center

### 2. Get Credentials
```python
credentials = credential_helper.get_swrole_credentials(
    sso_account_id="123456789",
    sso_role_name="ssoRoleName",
    sw_role_arn="arn:aws:iam::123456789012:role/sw-role-name"
    )
```
 - sso_account_id: AWS account ID with the access portal
 - sso_role_name: Role to log in with SSO
 - sw_role_arn: ARN of the role to switch to after logging in with SSO

### 3. Create boto3 client with credentials
```python
lambda_client = boto3.client(
    "lambda",
    region_name="ap-northeast-1",
    aws_access_key_id=credentials["AccessKeyId"],
    aws_secret_access_key=credentials["SecretAccessKey"],
    aws_session_token=credentials["SessionToken"],
    )
```
### Credentials
```python
{
    'AccessKeyId': 'XXXXXXXXXXXXX',
    'SecretAccessKey': 'YYYYYYYYY',
    'SessionToken': 'ZZZZZZZZZZ',
    'Expiration': expiration time,
}
```

## How to install

Install from PyPI
```python
pip install aws-sso-credential-helper
```

Let me know if there's anything else you need help with! 😊
