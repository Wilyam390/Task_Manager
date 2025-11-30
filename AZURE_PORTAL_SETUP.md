# Azure Portal Configuration Guide

Your app has been deployed to: **https://task-manager-8b.azurewebsites.net**

## Step 1: Configure Environment Variables in Azure Portal

1. Go to Azure Portal: https://portal.azure.com
2. Navigate to your Resource Group: **BCSAI2025-DEVOPS-STUDENT-8B**
3. Click on **task-manager-8b** (App Service)
4. In the left menu, go to **Configuration** → **Application settings**
5. Click **+ New application setting** for each of these:

### Application Settings to Add:

| Name | Value |
|------|-------|
| `FLASK_ENV` | `production` |
| `DB_TYPE` | `azure_sql` |
| `AZURE_SQL_CONNECTION_STRING` | `Driver={ODBC Driver 18 for SQL Server};Server=tcp:task-manager-sql-8b.database.windows.net,1433;Database=taskmanagerdb;Uid=sqladmin;Pwd=TaskManager2025!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;` |
| `APPINSIGHTS_INSTRUMENTATIONKEY` | `acb28819-3fc4-4d3d-b21a-722f007126ab` |
| `SCM_DO_BUILD_DURING_DEPLOYMENT` | `true` |

6. Click **Save** at the top
7. Click **Continue** when prompted about restarting the app

## Step 2: Configure Startup Command

1. In the same **Configuration** page
2. Go to **General settings** tab
3. Under **Startup Command**, enter:
   ```
   gunicorn --bind=0.0.0.0 --timeout 600 app:app
   ```
4. Click **Save**

## Step 3: Initialize the Database

Once the app is running, you need to create the database table. You have two options:

### Option A: Use Azure Cloud Shell
1. In Azure Portal, click the Cloud Shell icon (>_) at the top
2. Run these commands:
   ```bash
   # Install pyodbc if needed
   pip install pyodbc --user
   
   # Create init script
   cat > init_db.py << 'EOF'
   import pyodbc
   
   conn_str = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:task-manager-sql-8b.database.windows.net,1433;Database=taskmanagerdb;Uid=sqladmin;Pwd=TaskManager2025!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
   
   conn = pyodbc.connect(conn_str)
   cursor = conn.cursor()
   
   # Create table
   cursor.execute("""
   CREATE TABLE tasks (
       id INT IDENTITY(1,1) PRIMARY KEY,
       title NVARCHAR(200) NOT NULL,
       completed BIT DEFAULT 0,
       created_at DATETIME DEFAULT GETDATE()
   )
   """)
   
   # Add sample data
   cursor.execute("INSERT INTO tasks (title, completed) VALUES (?, ?)", ("Deploy to Azure successfully!", 1))
   cursor.execute("INSERT INTO tasks (title, completed) VALUES (?, ?)", ("Configure CI/CD pipeline", 0))
   
   conn.commit()
   cursor.close()
   conn.close()
   
   print("✅ Database initialized!")
   EOF
   
   python3 init_db.py
   ```

### Option B: Use SQL Query Editor in Portal
1. In Azure Portal, go to **taskmanagerdb** (SQL Database)
2. Click **Query editor** in the left menu
3. Login with:
   - Login: `sqladmin`
   - Password: `TaskManager2025!`
4. Run this SQL:
   ```sql
   CREATE TABLE tasks (
       id INT IDENTITY(1,1) PRIMARY KEY,
       title NVARCHAR(200) NOT NULL,
       completed BIT DEFAULT 0,
       created_at DATETIME DEFAULT GETDATE()
   );
   
   INSERT INTO tasks (title, completed) VALUES 
       ('Deploy to Azure successfully!', 1),
       ('Configure CI/CD pipeline', 0),
       ('Prepare for demo presentation', 0);
   ```
5. Click **Run**

## Step 4: Test Your Application

1. Visit: https://task-manager-8b.azurewebsites.net
2. You should see your Task Manager application!
3. Test the health endpoint: https://task-manager-8b.azurewebsites.net/health

## Resources Created

✅ **App Service Plan**: task-manager-plan-8b (B1 Basic)
✅ **Web App**: task-manager-8b  
✅ **SQL Server**: task-manager-sql-8b  
✅ **SQL Database**: taskmanagerdb  
✅ **Application Insights**: task-manager-insights-8b

## Troubleshooting

If the app shows errors:
1. Check **Log stream** in the App Service
2. Go to **Diagnose and solve problems** 
3. View **Application Insights** for detailed telemetry

## Next Steps

- Set up Azure DevOps Pipeline for automated deployments
- Configure custom domain (optional)
- Enable HTTPS only
- Set up deployment slots for staging/production
