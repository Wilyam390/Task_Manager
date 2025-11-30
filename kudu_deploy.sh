#!/bin/bash

# Get publishing credentials
echo "Getting deployment credentials..."
CREDS=$(az webapp deployment list-publishing-credentials \
  --name task-manager-8b \
  --resource-group BCSAI2025-DEVOPS-STUDENT-8B \
  --query "{username:publishingUserName, password:publishingPassword}" -o json)

USERNAME=$(echo $CREDS | python3 -c "import sys, json; print(json.load(sys.stdin)['username'])")
PASSWORD=$(echo $CREDS | python3 -c "import sys, json; print(json.load(sys.stdin)['password'])")

echo "Deploying to Kudu API..."
curl -X POST \
  -u "$USERNAME:$PASSWORD" \
  --data-binary @deploy.zip \
  https://task-manager-8b.scm.azurewebsites.net/api/zipdeploy

echo ""
echo "Deployment complete! Check https://task-manager-8b.azurewebsites.net"
