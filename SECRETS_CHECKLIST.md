# GitHub Secrets Checklist

## Step-by-Step: Adding Secrets to GitHub

Go to: **https://github.com/Wilyam390/Task_Manager/settings/secrets/actions**

---

### ✅ Secret 1: AZURE_CREDENTIALS
- [ ] Click **New repository secret**
- [ ] Name: `AZURE_CREDENTIALS`
- [ ] Value: Your full JSON object with clientId, clientSecret, subscriptionId, tenantId
- [ ] Click **Add secret**

**Your JSON should look like:**
```json
{
  "clientId": "YOUR-CLIENT-ID",
  "clientSecret": "YOUR-CLIENT-SECRET",
  "subscriptionId": "e0b9cada-61bc-4b5a-bd7a-52c606726b3b",
  "tenantId": "YOUR-TENANT-ID",
  "activeDirectoryEndpointUrl": "https://login.microsoftonline.com",
  "resourceManagerEndpointUrl": "https://management.azure.com/",
  "sqlManagementEndpointUrl": "https://management.core.windows.net:8443/",
  "galleryEndpointUrl": "https://gallery.azure.com/",
  "managementEndpointUrl": "https://management.core.windows.net/"
}
```

---

### ✅ Secret 2: AZURE_WEBAPP_NAME
- [ ] Click **New repository secret**
- [ ] Name: `AZURE_WEBAPP_NAME`
- [ ] Value: `task-manager-8b`
- [ ] Click **Add secret**

---

### ✅ Secret 3: AZURE_RESOURCE_GROUP
- [ ] Click **New repository secret**
- [ ] Name: `AZURE_RESOURCE_GROUP`
- [ ] Value: `BCSAI2025-DEVOPS-STUDENT-8B`
- [ ] Click **Add secret**

---

### ✅ Secret 4: AZURE_WEBAPP_PUBLISH_PROFILE
- [ ] Open `task-manager-8b.PublishSettings` file in VS Code
- [ ] Select ALL content (Cmd+A)
- [ ] Copy (Cmd+C)
- [ ] Click **New repository secret**
- [ ] Name: `AZURE_WEBAPP_PUBLISH_PROFILE`
- [ ] Value: Paste the entire XML
- [ ] Click **Add secret**

---

### ✅ Secret 5: AZURE_SQL_CONNECTION_STRING
- [ ] Click **New repository secret**
- [ ] Name: `AZURE_SQL_CONNECTION_STRING`
- [ ] Value: 
```
Driver={ODBC Driver 18 for SQL Server};Server=tcp:task-manager-sql-8b.database.windows.net,1433;Database=taskmanagerdb;Uid=sqladmin;Pwd=TaskManager2025!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
```
- [ ] Click **Add secret**

---

### ✅ Secret 6: APPINSIGHTS_INSTRUMENTATIONKEY
- [ ] Click **New repository secret**
- [ ] Name: `APPINSIGHTS_INSTRUMENTATIONKEY`
- [ ] Value: `acb28819-3fc4-4d3d-b21a-722f007126ab`
- [ ] Click **Add secret**

---

## Verification

After adding all 6 secrets, your GitHub Actions secrets page should show:

1. ✅ AZURE_CREDENTIALS
2. ✅ AZURE_WEBAPP_NAME
3. ✅ AZURE_RESOURCE_GROUP
4. ✅ AZURE_WEBAPP_PUBLISH_PROFILE
5. ✅ AZURE_SQL_CONNECTION_STRING
6. ✅ APPINSIGHTS_INSTRUMENTATIONKEY

**When done, let me know and I'll create the GitHub Actions workflow!**
