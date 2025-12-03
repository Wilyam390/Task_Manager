# 🎯 DEMO PREPARATION CHECKLIST
**For: Leena Barq**  
**Demo Date: December 4, 2025 (TOMORROW!)**

---

## ⏰ Time Estimate: 2-3 Hours

---

## ✅ STEP-BY-STEP CHECKLIST

### **Phase 1: Test Everything Locally** (45 minutes)

#### ☐ **Step 1.1: Set Up Python Environment**
```bash
cd /Users/leenabarq/Documents/Task_manager

# Check Python version (need 3.11+)
python3 --version

# Create virtual environment (if not exists)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Expected Output:** All packages install successfully  
**If Issues:** Copy error and ask team for help

---

#### ☐ **Step 1.2: Initialize Database**
```bash
# Still in /Users/leenabarq/Documents/Task_manager
python init_db.py
```

**Expected Output:** `Database initialized successfully`  
**What This Does:** Creates `tasks.db` file with task table

---

#### ☐ **Step 1.3: Run the Application**
```bash
python app.py
```

**Expected Output:**
```
 * Running on http://0.0.0.0:8000
 * Running on http://127.0.0.1:8000
```

**Next:** Open browser to http://localhost:8000

---

#### ☐ **Step 1.4: Test All Features** (IMPORTANT!)
In your browser at http://localhost:8000:

1. **✅ Add a task:**
   - Type "Buy groceries" in the input box
   - Click "Add Task"
   - Should appear in the list

2. **✅ Mark task as complete:**
   - Click the toggle/checkbox next to "Buy groceries"
   - Task should show as completed (strikethrough or checkmark)

3. **✅ Add another task:**
   - Add "Study for exam"
   - Add "Call mom"
   - Should now have 3 tasks total

4. **✅ Delete a task:**
   - Click delete button on "Call mom"
   - Should disappear from list

5. **✅ Test health endpoint:**
   - Open new browser tab
   - Go to http://localhost:8000/health
   - Should see JSON response:
     ```json
     {
       "status": "healthy",
       "tasks_count": 2,
       "environment": "development",
       "database": "sqlite"
     }
     ```

6. **✅ Test metrics endpoint:**
   - Go to http://localhost:8000/metrics
   - Should see Prometheus-format metrics

**Take Screenshots of:**
- ☐ Main page with tasks
- ☐ Health endpoint response
- ☐ Metrics endpoint

---

#### ☐ **Step 1.5: Run Tests**
```bash
# In terminal (Ctrl+C to stop app first)
pytest tests/ -v

# With coverage report
pytest --cov=app --cov=config --cov=database --cov-report=term tests/ -v
```

**Expected Output:** All tests pass, ~70%+ coverage  
**Take Screenshot:** Of test results

---

### **Phase 2: Test Docker** (30 minutes)

#### ☐ **Step 2.1: Build Docker Image**
```bash
cd /Users/leenabarq/Documents/Task_manager
docker build -t task-manager:demo .
```

**Expected Output:** "Successfully built" message  
**This May Take:** 2-3 minutes

---

#### ☐ **Step 2.2: Run Docker Container**
```bash
docker run -d -p 8000:8000 \
  -e ENVIRONMENT=development \
  -e SECRET_KEY=demo-secret-key \
  --name task-manager-demo \
  task-manager:demo
```

**Expected Output:** Container ID printed

---

#### ☐ **Step 2.3: Test Dockerized App**
- ☐ Visit http://localhost:8000
- ☐ Add a task to verify it works
- ☐ Check http://localhost:8000/health

---

#### ☐ **Step 2.4: Stop Docker Container**
```bash
docker stop task-manager-demo
docker rm task-manager-demo
```

---

#### ☐ **Step 2.5: Test Full Stack with Docker Compose** (OPTIONAL but impressive!)
```bash
docker-compose up -d
```

**Then visit:**
- ☐ App: http://localhost:8000
- ☐ Prometheus: http://localhost:9090
- ☐ Grafana: http://localhost:3000 (login: admin/admin)

**Take Screenshots!**

**Stop when done:**
```bash
docker-compose down
```

---

### **Phase 3: Documentation Updates** (30 minutes)

#### ☐ **Step 3.1: Add Team Member Names to README**
```bash
# Open README.md in editor
# Find line 10: "**Team Members:** [Add your team members here]"
# Replace with actual names
```

**Example:**
```markdown
**Team Members:** John Smith, Jane Doe, Bob Johnson, Alice Williams, Leena Barq, Tom Brown
```

---

#### ☐ **Step 3.2: Create Individual Contribution Document**

Create file: `INDIVIDUAL_CONTRIBUTIONS.md`

```markdown
# Individual Contributions - [Your Name]

## Team Members and Contributions

1. **[Teammate A Name]** - 30%
   - Backend development (Flask app, routes, database)
   - Database integration (SQLite + Azure SQL)
   - Error handling and logging

2. **[Teammate B Name]** - 25%
   - CI/CD pipeline setup (GitHub Actions)
   - Azure deployment configuration
   - Docker containerization

3. **[Teammate C Name]** - 20%
   - Testing framework (pytest)
   - Integration tests
   - Code coverage setup

4. **[Teammate D Name]** - 15%
   - Frontend UI design
   - CSS styling
   - Template development

5. **Leena Barq (You)** - 10%
   - Documentation review and updates
   - Testing and quality assurance
   - Demo preparation and testing
   - Project status analysis

## Project Links

- **GitHub Repository:** https://github.com/Wilyam390/Task_manager
- **Live Demo:** [Insert Azure URL if deployed, or "Local demonstration"]
- **CI/CD Pipeline:** https://github.com/Wilyam390/Task_manager/actions

## AI Tools Used

- **GitHub Copilot:** Code completion and suggestions during development
- **ChatGPT/Claude:** Troubleshooting, documentation formatting, deployment questions
- **Specific Usage:** Understanding Flask error handling, Docker configuration help

## Retrospective Notes

### What Went Well
- Team collaboration and task distribution
- Clean, working MVP delivered on time
- Comprehensive testing and documentation

### Challenges Faced
- [Ask team: What were the main challenges?]
- Example: Azure SQL connection string configuration

### What I Learned
- Cloud deployment with Azure services
- CI/CD pipeline automation
- Docker containerization best practices
- Flask web application development

---

**Submitted by:** Leena Barq  
**Date:** December 4, 2025  
**Course:** BCSAI - SDDO - 2025
```

---

### **Phase 4: Prepare Demo Materials** (45 minutes)

#### ☐ **Step 4.1: Create Demo Script**

Create file: `DEMO_SCRIPT.md`

```markdown
# Task Manager Demo Script
**Duration: 10-12 minutes**

## 1. Introduction (1 min)
**Speaker:** [Assign]

"Good morning! We're presenting our Task Manager application - a cloud-native web app built using Azure services and modern DevOps practices."

**Team:**
- [Name] - [Role]
- [Name] - [Role]
- Leena - Testing & Documentation

## 2. Architecture Overview (1 min)
**Speaker:** [Assign]

**Show:** README.md architecture diagram

"Our application uses 5 Azure services:
- Azure App Service for hosting
- Azure SQL Database for data
- Application Insights for monitoring
- Azure Monitor for dashboards
- GitHub Actions for CI/CD"

## 3. Live Demo (4 min)
**Speaker:** Leena (You!)

**Screen:** http://localhost:8000 (or Azure URL)

**Actions:**
1. "Let me add a task for our final presentation"
   - Type: "Complete final project demo"
   - Click Add Task
   - *Point out*: "Task immediately appears with timestamp"

2. "Now I'll add a few more tasks"
   - Add: "Submit individual report"
   - Add: "Celebrate successful demo"

3. "Mark the first task as complete"
   - Click toggle
   - *Point out*: "Visual feedback shows completion"

4. "Delete a task"
   - Delete middle task
   - *Point out*: "Clean deletion with confirmation"

5. "Show health endpoint"
   - Navigate to /health
   - *Point out*: "Returns status, task count, environment"

6. "Show metrics endpoint"
   - Navigate to /metrics
   - *Point out*: "Prometheus-format metrics for monitoring"

## 4. DevOps Pipeline (2 min)
**Speaker:** [Assign]

**Screen:** GitHub Actions tab

"Our CI/CD pipeline automates:
1. Building the application
2. Running tests with 70%+ coverage requirement
3. Creating Docker images
4. Deploying to Azure
5. Running health checks"

*Click on latest workflow run*
*Show green checkmarks*

## 5. Testing & Quality (1 min)
**Speaker:** [Assign]

**Screen:** Test coverage report

"We have comprehensive test coverage:
- Unit tests for all routes
- Integration tests
- 74% code coverage
- Automated in CI/CD"

## 6. Monitoring (1 min)
**Speaker:** [Assign]

**Options:**
- Show Application Insights (if deployed)
- OR show Grafana dashboard (docker-compose)
- OR show Prometheus metrics

## 7. Documentation (1 min)
**Speaker:** Leena (You!)

**Screen:** README.md

"Complete documentation includes:
- Architecture diagrams
- Setup instructions
- Sprint history
- Docker deployment guide
- Testing procedures"

## 8. Q&A (1-2 min)
**All team members**

**Prepared Answers:**

Q: "Why did you choose this tech stack?"
A: "Flask is lightweight and perfect for MVPs. Azure provides enterprise-grade cloud services. Docker ensures consistency across environments."

Q: "What was the biggest challenge?"
A: "Configuring Azure SQL connection and Application Insights integration in production."

Q: "How would you scale this?"
A: "Add Redis caching, implement task queuing with Azure Service Bus, use Azure Front Door for CDN."

Q: "Why SQLite in development?"
A: "Faster local development, no connection strings needed, easy to reset."

---

**Backup Demos (if live demo fails):**
1. Pre-recorded video
2. Screenshots walkthrough
3. Docker demo
```

---

#### ☐ **Step 4.2: Take All Required Screenshots**

Create folder: `demo_screenshots/`

**Required Screenshots:**
1. ☐ Homepage with multiple tasks
2. ☐ Adding a new task
3. ☐ Completing a task
4. ☐ Health endpoint JSON response
5. ☐ Metrics endpoint
6. ☐ GitHub Actions pipeline (green checks)
7. ☐ Test results with coverage
8. ☐ Docker build success
9. ☐ Grafana dashboard (if using docker-compose)
10. ☐ README.md architecture diagram

**Save them as:**
- `01_homepage.png`
- `02_add_task.png`
- etc.

---

#### ☐ **Step 4.3: Create Presentation Slides** (OPTIONAL but helpful)

If your team wants slides, create a simple Google Slides/PowerPoint:

**Slide 1:** Title
- Task Manager - Cloud DevOps Project
- Team Names
- IE University BCSAI 2025

**Slide 2:** Project Overview
- What: Task management web application
- Why: Demonstrate cloud-native DevOps practices
- How: Flask + Azure + Docker + CI/CD

**Slide 3:** Architecture Diagram
- (Copy from README.md)

**Slide 4:** Technology Stack
- Backend: Python/Flask
- Database: Azure SQL
- Hosting: Azure App Service
- CI/CD: GitHub Actions
- Monitoring: Application Insights, Prometheus
- Containerization: Docker

**Slide 5:** Features
- CRUD operations for tasks
- Real-time task status updates
- Health monitoring
- Metrics tracking
- Error handling

**Slide 6:** DevOps Highlights
- Automated testing (70%+ coverage)
- CI/CD pipeline
- Docker containerization
- Infrastructure monitoring
- Comprehensive logging

**Slide 7:** Live Demo
- (This slide just says "Live Demo" - you show the actual app)

**Slide 8:** Challenges & Learnings
- Azure SQL configuration
- CI/CD setup
- Production-ready error handling
- Team collaboration

**Slide 9:** Thank You / Questions

---

### **Phase 5: Team Coordination** (15 minutes)

#### ☐ **Step 5.1: Questions to Ask Your Team (via message)**

Send this to your group chat:

```
Hey team! 👋 

I'm preparing for tomorrow's demo and need some info:

1. Is the app deployed to Azure? If yes, what's the URL?
2. Do we have access to Azure portal to show Application Insights?
3. Who's presenting which part? I can do the live demo + documentation walkthrough
4. Do we have GitHub secrets configured for CI/CD?
5. What were our biggest challenges? (for Q&A preparation)
6. Who should I credit for what in the individual contribution doc?

I've tested everything locally and it all works great! 🎉

- Leena
```

---

#### ☐ **Step 5.2: Divide Presentation Roles**

Suggested division (adjust based on your team):
- **Person 1:** Introduction + Architecture (2 min)
- **Person 2:** DevOps Pipeline + Testing (3 min)
- **Person 3:** Monitoring + Cloud Infrastructure (2 min)
- **You (Leena):** Live Demo + Documentation (4 min)
- **All:** Q&A (2 min)

---

### **Phase 6: Final Checks** (15 minutes)

#### ☐ **Step 6.1: Verify Everything Works One More Time**

```bash
# Start fresh
cd /Users/leenabarq/Documents/Task_manager
rm tasks.db  # Delete old database
python init_db.py  # Create fresh database
python app.py  # Run app

# Test in browser
# - Add 3 tasks
# - Mark 1 complete
# - Delete 1
# - Check /health
# - Check /metrics
```

---

#### ☐ **Step 6.2: Prepare Your Demo Environment**

**Before demo:**
- ☐ Close all unnecessary browser tabs
- ☐ Clear browser history (for clean demo)
- ☐ Have terminal ready with commands
- ☐ Have screenshots ready as backup
- ☐ Test screenshare quality
- ☐ Have README.md open in another window
- ☐ Have GitHub repo open in another tab

---

#### ☐ **Step 6.3: Practice Your Part**

**Practice out loud (seriously, do this!):**

"Now I'll demonstrate the live application. First, I'll add a task called 'Complete final demo'... [type]... and click Add Task. As you can see, it appears immediately in our task list. Next, I'll mark it as complete... [click]... and you can see the visual feedback. Finally, let me show our health endpoint which returns the application status in JSON format..."

**Time yourself:** Should take 3-4 minutes

---

## 📊 **SCORING CHECKLIST**

Verify you can demonstrate each requirement:

### Development & Functionality (25 pts)
- ☐ Working web application
- ☐ Backend API working
- ☐ Frontend UI functional
- ☐ CRUD operations
- ☐ Error handling

### Cloud Infrastructure (20 pts)
- ☐ Show 5 Azure services (docs/portal)
- ☐ Explain architecture
- ☐ Show resource group (if deployed)

### DevOps Pipeline (20 pts)
- ☐ Show GitHub Actions workflow
- ☐ Show automated stages
- ☐ Show successful deployments
- ☐ Explain version control

### Testing & Quality (15 pts)
- ☐ Run tests live
- ☐ Show coverage report
- ☐ Explain test strategy

### Monitoring & Logging (10 pts)
- ☐ Show health endpoint
- ☐ Show metrics endpoint
- ☐ Show logs (if possible)
- ☐ Explain monitoring strategy

### Documentation (10 pts)
- ☐ Show README
- ☐ Show architecture diagram
- ☐ Show setup instructions
- ☐ Show Sprint history

---

## 🚨 **TROUBLESHOOTING**

### Problem: "Can't install dependencies"
```bash
# Try upgrading pip first
pip install --upgrade pip
pip install -r requirements.txt
```

### Problem: "Database error when running app"
```bash
# Reinitialize database
rm tasks.db
python init_db.py
python app.py
```

### Problem: "Port 8000 already in use"
```bash
# Find and kill process using port 8000
lsof -ti:8000 | xargs kill -9
# Or use different port:
python app.py  # then change port in config
```

### Problem: "Tests failing"
```bash
# Make sure database exists
python init_db.py
# Run tests
pytest tests/ -v
```

### Problem: "Docker build fails"
```bash
# Check Docker is running
docker --version
docker info

# Clear Docker cache if needed
docker system prune -a
```

---

## ✅ **DAY-OF-DEMO CHECKLIST**

**Morning of December 4:**

- ☐ Get good sleep night before! 😴
- ☐ Eat breakfast
- ☐ Charge laptop fully 🔋
- ☐ Test WiFi/internet connection
- ☐ Run app one final time
- ☐ Have backup: screenshots + pre-recorded video
- ☐ Arrive 10 minutes early
- ☐ Deep breath - you've got this! 💪

---

## 🎉 **YOU'RE READY!**

Your team built an excellent project. You just need to:
1. Test it (45 min)
2. Understand it (read docs - 30 min)
3. Practice your demo part (15 min)
4. Show up confidently tomorrow

**Total time needed: ~3 hours**

Good luck! 🍀 You've got this! 🚀

---

**Questions?** Ask your team or refer to:
- `PROJECT_STATUS_SUMMARY.md` - Overall project status
- `README.md` - Technical documentation
- `DOCKER_GUIDE.md` - Docker deployment help

**Last Resort:** If everything fails during demo, you have:
- Screenshots of working app ✅
- GitHub Actions showing successful builds ✅
- Documentation proving it was built ✅
- Test results showing it works ✅
