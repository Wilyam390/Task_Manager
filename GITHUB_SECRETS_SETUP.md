# GitHub Secrets Setup Guide

## Required Secrets for GitHub Actions CI/CD

Go to your GitHub repository: **https://github.com/Wilyam390/Task_Manager**

### Steps:
1. Click **Settings** tab
2. In the left sidebar, click **Secrets and variables** → **Actions**
3. Click **New repository secret** for each of these:

---

## Secrets to Add:

### 1. AZURE_CREDENTIALS
**Name:** `AZURE_CREDENTIALS`  
**Value:** (The entire JSON object you have)
```json
{
  "clientId": "your-client-id",
  "clientSecret": "your-client-secret",
  "subscriptionId": "e0b9cada-61bc-4b5a-bd7a-52c606726b3b",
  "tenantId": "your-tenant-id",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}
```

### 2. AZURE_WEBAPP_NAME
**Name:** `AZURE_WEBAPP_NAME`  
**Value:** `task-manager-8b`

### 3. AZURE_RESOURCE_GROUP
**Name:** `AZURE_RESOURCE_GROUP`  
**Value:** `BCSAI2025-DEVOPS-STUDENT-8B`

### 4. AZURE_WEBAPP_PUBLISH_PROFILE
**Name:** `AZURE_WEBAPP_PUBLISH_PROFILE`  
**Value:** (We'll get this from Azure Portal - see Step 2 below)

### 5. AZURE_SQL_CONNECTION_STRING
**Name:** `AZURE_SQL_CONNECTION_STRING`  
**Value:** 
```
Driver={ODBC Driver 18 for SQL Server};Server=tcp:task-manager-sql-8b.database.windows.net,1433;Database=taskmanagerdb;Uid=sqladmin;Pwd=TaskManager2025!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
```

### 6. APPINSIGHTS_INSTRUMENTATIONKEY
**Name:** `APPINSIGHTS_INSTRUMENTATIONKEY`  
**Value:** `acb28819-3fc4-4d3d-b21a-722f007126ab`

---

## Step 2: Get Publish Profile (Using Azure CLI)

Since basic authentication is disabled in the portal, use this method:

1. **The publish profile is already downloaded!** Check your project folder for `task-manager-8b.PublishSettings`
2. Open `task-manager-8b.PublishSettings` in a text editor (VS Code)
3. Copy the **ENTIRE contents** of the file (it's XML format)
4. Go to GitHub: https://github.com/Wilyam390/Task_Manager
5. Click **Settings** tab
6. Click **Secrets and variables** → **Actions**
7. Click **New repository secret**
8. Name: `AZURE_WEBAPP_PUBLISH_PROFILE`
9. Value: Paste the entire XML contents
10. Click **Add secret**

**Alternative:** If you need to regenerate it:
```bash
az webapp deployment list-publishing-profiles \
  --name task-manager-8b \
  --resource-group BCSAI2025-DEVOPS-STUDENT-8B \
  --xml > task-manager-8b.PublishSettings
```

---

## Step 3: Verify Service Principal (Optional but Recommended)

The Service Principal credentials you have:
- **appId**: This is the same as `clientId` in AZURE_CREDENTIALS
- **password**: This is the same as `clientSecret` in AZURE_CREDENTIALS  
- **tenant**: This is the same as `tenantId` in AZURE_CREDENTIALS

You can verify your service principal has the right permissions:

```bash
# Login with service principal
az login --service-principal \
  -u <appId> \
  -p <password> \
  --tenant <tenant>

# Verify access to resource group
az group show --name BCSAI2025-DEVOPS-STUDENT-8B
```

---

## Summary of All Secrets:

| Secret Name | Purpose |
|-------------|---------|
| `AZURE_CREDENTIALS` | Service principal for Azure login |
| `AZURE_WEBAPP_NAME` | Target web app name |
| `AZURE_RESOURCE_GROUP` | Resource group name |
| `AZURE_WEBAPP_PUBLISH_PROFILE` | Deployment credentials |
| `AZURE_SQL_CONNECTION_STRING` | Database connection |
| `APPINSIGHTS_INSTRUMENTATIONKEY` | Application monitoring |

Once you've added all these secrets, we can:
1. Create a GitHub Actions workflow
2. Test automated deployment
3. Set up the CI/CD pipeline

**Let me know when you've added the secrets and I'll create the GitHub Actions workflow file!**
