#!/usr/bin/env python3
"""
Simple deployment script using Azure SDK
"""
import os
import zipfile
import subprocess
import sys

def create_deployment_zip():
    """Create a clean deployment package"""
    print("📦 Creating deployment package...")
    
    # Files to exclude
    exclude_patterns = {
        '.git', '__pycache__', '*.pyc', '*.db', '*.log', 
        '.env', '.env.local', 'app.zip', 'venv', 'ENV'
    }
    
    zip_name = 'deploy.zip'
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('.'):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not any(pattern in d for pattern in exclude_patterns)]
            
            for file in files:
                if not any(pattern in file for pattern in exclude_patterns):
                    file_path = os.path.join(root, file)
                    arcname = file_path[2:]  # Remove './' prefix
                    print(f"  Adding: {arcname}")
                    zipf.write(file_path, arcname)
    
    print(f"✅ Created {zip_name}")
    return zip_name

def deploy_with_kudu(zip_file):
    """Deploy using Kudu REST API"""
    app_name = "task-manager-8b"
    resource_group = "BCSAI2025-DEVOPS-STUDENT-8B"
    
    print(f"\n🚀 Deploying to {app_name}...")
    
    # Get publishing credentials
    cmd = [
        'az', 'webapp', 'deployment', 'list-publishing-credentials',
        '--name', app_name,
        '--resource-group', resource_group,
        '--query', '{username:publishingUserName, password:publishingPassword}',
        '-o', 'json'
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Failed to get credentials: {result.stderr}")
        return False
    
    import json
    creds = json.loads(result.stdout)
    username = creds['username']
    password = creds['password']
    
    # Deploy using curl
    kudu_url = f"https://{app_name}.scm.azurewebsites.net/api/zipdeploy"
    
    print(f"  Uploading to: {kudu_url}")
    
    curl_cmd = [
        'curl', '-X', 'POST',
        '-u', f"{username}:{password}",
        '--data-binary', f"@{zip_file}",
        '-H', 'Content-Type: application/zip',
        kudu_url
    ]
    
    result = subprocess.run(curl_cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Deployment successful!")
        print(f"\n🌐 Visit: https://{app_name}.azurewebsites.net")
        return True
    else:
        print(f"❌ Deployment failed: {result.stderr}")
        return False

if __name__ == "__main__":
    try:
        zip_file = create_deployment_zip()
        success = deploy_with_kudu(zip_file)
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
