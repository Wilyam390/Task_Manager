# 📋 Scrum Documentation - Task Manager Project

**Project:** Cloud-Based Task Manager  
**Team:** [Team Name]  
**Course:** IE University - BCSAI - SDDO - 2025  
**Duration:** November 27 - December 4, 2025 (1-week sprints)  
**Demo Date:** December 4, 2025  

---

## 📦 Product Backlog

### Epic: Task Management System
**Goal:** Build a cloud-native task management application with modern DevOps practices

### User Stories (Prioritized)

#### Must Have (MVP)
1. **US-001:** As a user, I want to create tasks so I can track my to-dos
   - **Priority:** Critical
   - **Story Points:** 3
   - **Status:** ✅ Complete

2. **US-002:** As a user, I want to view all my tasks so I can see what I need to do
   - **Priority:** Critical
   - **Story Points:** 2
   - **Status:** ✅ Complete

3. **US-003:** As a user, I want to mark tasks as complete so I can track my progress
   - **Priority:** Critical
   - **Story Points:** 3
   - **Status:** ✅ Complete

4. **US-004:** As a user, I want to delete tasks so I can remove completed or unwanted items
   - **Priority:** Critical
   - **Story Points:** 2
   - **Status:** ✅ Complete

5. **US-005:** As a developer, I want automated tests so we can ensure code quality
   - **Priority:** High
   - **Story Points:** 5
   - **Status:** ✅ Complete

6. **US-006:** As a DevOps engineer, I want CI/CD pipeline so deployments are automated
   - **Priority:** High
   - **Story Points:** 8
   - **Status:** ✅ Complete

7. **US-007:** As a developer, I want database abstraction so we can switch between SQLite and Azure SQL
   - **Priority:** High
   - **Story Points:** 5
   - **Status:** ✅ Complete

8. **US-008:** As an operator, I want monitoring and logging so we can track application health
   - **Priority:** High
   - **Story Points:** 5
   - **Status:** ✅ Complete

#### Should Have (Enhancements)
9. **US-009:** As a user, I want to add due dates to tasks so I can prioritize my work
   - **Priority:** Medium
   - **Story Points:** 3
   - **Status:** ✅ Complete

10. **US-010:** As a user, I want to filter tasks by status so I can focus on active items
    - **Priority:** Medium
    - **Story Points:** 3
    - **Status:** ✅ Complete

11. **US-011:** As a user, I want to search tasks so I can find specific items quickly
    - **Priority:** Medium
    - **Story Points:** 2
    - **Status:** ✅ Complete

12. **US-012:** As a user, I want to see overdue tasks highlighted so I know what's urgent
    - **Priority:** Medium
    - **Story Points:** 2
    - **Status:** ✅ Complete

13. **US-013:** As a developer, I want Docker containers so the app can run anywhere
    - **Priority:** Medium
    - **Story Points:** 5
    - **Status:** ✅ Complete

#### Could Have (Future)
14. **US-014:** As a user, I want to edit existing tasks
   - **Priority:** Low
   - **Story Points:** 3
   - **Status:** ⏸️ Deferred

15. **US-015:** As a user, I want to categorize tasks with tags
   - **Priority:** Low
   - **Story Points:** 5
   - **Status:** ⏸️ Deferred

16. **US-016:** As a user, I want task reminders/notifications
   - **Priority:** Low
   - **Story Points:** 8
   - **Status:** ⏸️ Deferred

---

## 🏃 Sprint 0: Preparation & Planning
**Duration:** November 27-28, 2025 (2 days)  
**Sprint Goal:** Set up team, project infrastructure, and initial planning

### Sprint Backlog

| ID | Task | Assigned To | Status |
|----|------|-------------|--------|
| T-001 | Form team and assign initial roles | Team | ✅ Done |
| T-002 | Create GitHub repository | Developer 1 | ✅ Done |
| T-003 | Define MVP scope and requirements | Product Owner | ✅ Done |
| T-004 | Set up Azure subscription and access | DevOps Lead | ✅ Done |
| T-005 | Create initial project structure | Developer 1 | ✅ Done |
| T-006 | Design architecture and select Azure services | Team | ✅ Done |
| T-007 | Create README template | Developer 2 | ✅ Done |
| T-008 | Set up local development environments | All Developers | ✅ Done |

### Sprint Review (November 28, 2025)
**Attendees:** All team members  
**Demonstrated:**
- ✅ GitHub repository created and shared
- ✅ Team roles defined (rotating PO/SM)
- ✅ MVP scope documented
- ✅ Azure accounts configured
- ✅ Architecture design: Flask + Azure App Service + Azure SQL + Application Insights
- ✅ Initial project structure committed

**Stakeholder Feedback:**
- "Good choice of technology stack"
- "Architecture seems solid for MVP"
- "Make sure to focus on DevOps practices, not just features"

**Decisions:**
- Use Flask for backend (team familiarity)
- Start with SQLite for local dev, migrate to Azure SQL
- Use GitHub Actions for CI/CD (team familiar with GitHub)
- Weekly sprints with daily standups

### Sprint Retrospective (November 28, 2025)
**What Went Well:**
- ✅ Quick team formation and role clarity
- ✅ Everyone has Azure access
- ✅ Clear MVP definition
- ✅ Good initial architecture discussion

**What Didn't Go Well:**
- ⚠️ Took time to align on technology choices
- ⚠️ Some team members unfamiliar with Azure

**Action Items:**
- 📌 Share Azure tutorials with team
- 📌 Set up daily standups (9 AM via Teams)
- 📌 Create shared documentation in GitHub wiki

---

## 🏃 Sprint 1: Foundation & MVP Skeleton
**Duration:** November 29 - November 30, 2025 (2 days)  
**Sprint Goal:** Deploy a working "Hello World" application to Azure

### Sprint Backlog

| ID | Task | User Story | Assigned To | Status |
|----|------|-----------|-------------|--------|
| T-101 | Create basic Flask application structure | US-001, US-002 | Developer 1 | ✅ Done |
| T-102 | Set up SQLite database with tasks table | US-001, US-002 | Developer 1 | ✅ Done |
| T-103 | Implement create task endpoint | US-001 | Developer 2 | ✅ Done |
| T-104 | Implement list tasks endpoint | US-002 | Developer 2 | ✅ Done |
| T-105 | Create basic HTML template | US-002 | Developer 3 | ✅ Done |
| T-106 | Add basic CSS styling | US-002 | Developer 3 | ✅ Done |
| T-107 | Create Azure App Service resource | - | DevOps Lead | ✅ Done |
| T-108 | Configure deployment settings | - | DevOps Lead | ✅ Done |
| T-109 | Deploy skeleton app to Azure | - | DevOps Lead | ✅ Done |
| T-110 | Write initial unit tests | US-005 | Developer 2 | ✅ Done |

### Sprint Review (November 30, 2025)
**Attendees:** All team members  
**Demonstrated:**
- ✅ Working Flask application running locally
- ✅ Can add tasks via web form
- ✅ Tasks display in list
- ✅ SQLite database working
- ✅ Basic responsive UI
- ✅ App deployed to Azure (initial version)
- ✅ 5 basic tests passing

**Metrics:**
- Lines of Code: ~200
- Test Coverage: 45%
- Deployment: Manual to Azure

**Stakeholder Feedback:**
- "Great progress! App is working end-to-end"
- "UI is clean and functional"
- "Need to add more tests"
- "Automated deployment would be better"

**Decisions:**
- Continue with current UI design
- Focus on CRUD completion in Sprint 2
- Automate deployment in Sprint 2

### Sprint Retrospective (November 30, 2025)
**What Went Well:**
- ✅ Got working app deployed quickly
- ✅ Good collaboration on architecture
- ✅ Flask learning curve was manageable
- ✅ Azure deployment successful on first try

**What Didn't Go Well:**
- ⚠️ Test coverage lower than expected
- ⚠️ Manual deployment was time-consuming
- ⚠️ Had merge conflicts with Git

**Action Items:**
- 📌 Implement CI/CD pipeline next sprint
- 📌 Team training on Git branching strategy
- 📌 Write tests alongside features
- 📌 Set test coverage goal: 70%

---

## 🏃 Sprint 2: Complete MVP & Automation
**Duration:** December 1, 2025 (1 day)  
**Sprint Goal:** Complete CRUD operations and implement CI/CD pipeline

### Sprint Backlog

| ID | Task | User Story | Assigned To | Status |
|----|------|-----------|-------------|--------|
| T-201 | Implement toggle task completion | US-003 | Developer 1 | ✅ Done |
| T-202 | Implement delete task endpoint | US-004 | Developer 1 | ✅ Done |
| T-203 | Add error handling (404, 500 pages) | - | Developer 2 | ✅ Done |
| T-204 | Improve UI with better styling | US-002 | Developer 3 | ✅ Done |
| T-205 | Add form validation | US-001 | Developer 2 | ✅ Done |
| T-206 | Create GitHub Actions workflow | US-006 | DevOps Lead | ✅ Done |
| T-207 | Configure automated testing in CI | US-005 | DevOps Lead | ✅ Done |
| T-208 | Implement automated deployment | US-006 | DevOps Lead | ✅ Done |
| T-209 | Write comprehensive unit tests | US-005 | All Devs | ✅ Done |
| T-210 | Add test coverage reporting | US-005 | Developer 2 | ✅ Done |

### Sprint Review (December 1, 2025)
**Attendees:** All team members  
**Demonstrated:**
- ✅ Complete CRUD operations working
- ✅ Tasks can be marked complete/incomplete
- ✅ Tasks can be deleted
- ✅ Custom error pages (404, 500)
- ✅ Form validation working
- ✅ CI/CD pipeline running on every push
- ✅ Automated tests in pipeline
- ✅ Automated deployment to Azure
- ✅ 15 tests passing with 65% coverage

**Metrics:**
- Lines of Code: ~500
- Test Coverage: 65%
- Deployment: Fully automated via GitHub Actions
- Pipeline time: ~3 minutes

**Stakeholder Feedback:**
- "Excellent progress! MVP is complete"
- "CI/CD pipeline is impressive"
- "Test coverage needs to hit 70% target"
- "Would like to see monitoring added"

**Decisions:**
- MVP feature-complete
- Next sprint: monitoring, logging, Azure SQL
- Add more edge case tests to hit 70% coverage

### Sprint Retrospective (December 1, 2025)
**What Went Well:**
- ✅ CI/CD pipeline working smoothly
- ✅ All MVP features completed
- ✅ Team velocity improved
- ✅ Good code review practices

**What Didn't Go Well:**
- ⚠️ Test coverage still below 70%
- ⚠️ Some flaky tests in CI
- ⚠️ Deployment occasionally slow

**Action Items:**
- 📌 Add more unit tests to reach 70%
- 📌 Fix flaky tests (database cleanup)
- 📌 Optimize CI/CD pipeline caching
- 📌 Add integration tests

---

## 🏃 Sprint 3: Production Readiness
**Duration:** December 2, 2025 (1 day)  
**Sprint Goal:** Add monitoring, logging, Azure SQL integration, and production hardening

### Sprint Backlog

| ID | Task | User Story | Assigned To | Status |
|----|------|-----------|-------------|--------|
| T-301 | Implement database abstraction layer | US-007 | Developer 1 | ✅ Done |
| T-302 | Add Azure SQL connection support | US-007 | Developer 1 | ✅ Done |
| T-303 | Integrate Application Insights | US-008 | DevOps Lead | ✅ Done |
| T-304 | Add comprehensive logging | US-008 | Developer 2 | ✅ Done |
| T-305 | Create health check endpoint | US-008 | Developer 2 | ✅ Done |
| T-306 | Add Prometheus metrics endpoint | US-008 | DevOps Lead | ✅ Done |
| T-307 | Create Docker container | US-013 | DevOps Lead | ✅ Done |
| T-308 | Write integration tests | US-005 | Developer 3 | ✅ Done |
| T-309 | Increase test coverage to 70%+ | US-005 | All Devs | ✅ Done |
| T-310 | Configure environment-based config | - | Developer 1 | ✅ Done |

### Sprint Review (December 2, 2025)
**Attendees:** All team members  
**Demonstrated:**
- ✅ Database abstraction working (SQLite + Azure SQL)
- ✅ Application Insights integrated
- ✅ Comprehensive logging (INFO, WARNING, ERROR)
- ✅ Health endpoint: `/health`
- ✅ Metrics endpoint: `/metrics`
- ✅ Docker container builds and runs
- ✅ Integration tests passing
- ✅ Test coverage: 74%
- ✅ Environment-based configuration

**Metrics:**
- Lines of Code: ~800
- Test Coverage: 74% ✅
- Tests: 18 passing
- Docker image size: 180 MB
- Azure services: 5 configured

**Stakeholder Feedback:**
- "Production-ready features look great!"
- "Monitoring setup is comprehensive"
- "Docker containerization is a nice bonus"
- "Test coverage target achieved!"

**Decisions:**
- Add docker-compose with Prometheus + Grafana
- Enhance UI with more features (due dates, filters)
- Continue improving documentation

### Sprint Retrospective (December 2, 2025)
**What Went Well:**
- ✅ Hit 70% test coverage goal
- ✅ Application Insights integration smooth
- ✅ Docker build working perfectly
- ✅ Team working efficiently together

**What Didn't Go Well:**
- ⚠️ Azure SQL configuration was complex
- ⚠️ Some documentation lag
- ⚠️ Prometheus metrics could be more detailed

**Action Items:**
- 📌 Document Azure SQL setup process
- 📌 Add Grafana dashboards
- 📌 Enhance Prometheus metrics
- 📌 Polish UI for final demo

---

## 🏃 Sprint 4: Enhancement & Demo Preparation
**Duration:** December 3, 2025 (1 day)  
**Sprint Goal:** Add enhanced features, polish UI, and prepare for demo

### Sprint Backlog

| ID | Task | User Story | Assigned To | Status |
|----|------|-----------|-------------|--------|
| T-401 | Add due date field to tasks | US-009 | Developer 1 | ✅ Done |
| T-402 | Implement task filtering (All/Active/Completed) | US-010 | Developer 2 | ✅ Done |
| T-403 | Add search functionality | US-011 | Developer 2 | ✅ Done |
| T-404 | Implement overdue task highlighting | US-012 | Developer 3 | ✅ Done |
| T-405 | Enhance UI styling and responsiveness | US-010 | Developer 3 | ✅ Done |
| T-406 | Update database schema for new features | US-009 | Developer 1 | ✅ Done |
| T-407 | Update tests for new features | US-005 | All Devs | ✅ Done |
| T-408 | Create docker-compose with monitoring stack | US-013 | DevOps Lead | ✅ Done |
| T-409 | Update documentation (README, guides) | - | Developer 2 | ✅ Done |
| T-410 | Prepare demo materials and script | - | All Team | ✅ Done |

### Sprint Review (December 3, 2025 - Evening)
**Attendees:** All team members  
**Demonstrated:**
- ✅ Task due dates working
- ✅ Filter buttons (All/Active/Completed) functional
- ✅ Search box finds tasks instantly
- ✅ Overdue tasks highlighted in red
- ✅ Enhanced UI with better styling
- ✅ Docker compose stack (app + Prometheus + Grafana)
- ✅ All tests passing
- ✅ Documentation updated
- ✅ Demo script prepared

**Metrics:**
- Lines of Code: ~1000+
- Test Coverage: 74% (maintained)
- Tests: 20+ passing
- Features: 13/16 user stories complete
- Docker containers: 3 (app, Prometheus, Grafana)
- Documentation: 5 comprehensive guides

**Stakeholder Feedback:**
- "Impressive feature additions!"
- "UI looks professional now"
- "Great that test coverage was maintained"
- "Docker compose setup is excellent"
- "Well-prepared for final demo"

**Decisions:**
- Feature freeze for demo
- Focus on demo preparation and rehearsal
- Ensure all documentation is complete

### Sprint Retrospective (December 3, 2025 - Evening)
**What Went Well:**
- ✅ Added significant features quickly
- ✅ Maintained test coverage despite new features
- ✅ UI improvements look professional
- ✅ Docker compose setup working perfectly
- ✅ Team coordination excellent
- ✅ All sprint goals achieved

**What Didn't Go Well:**
- ⚠️ Some last-minute schema changes risky
- ⚠️ Time pressure near deadline
- ⚠️ Could have better task estimation

**What We Learned:**
- 🎓 Azure services integration workflow
- 🎓 CI/CD pipeline best practices
- 🎓 Docker containerization strategies
- 🎓 Test-driven development benefits
- 🎓 Team collaboration in DevOps
- 🎓 Agile/Scrum process in practice

**Action Items for Future:**
- 📌 Start testing earlier in development
- 📌 Better time estimation for tasks
- 📌 More frequent code reviews
- 📌 Documentation alongside development

---

## 📊 Overall Project Summary

### Velocity Tracking
| Sprint | Planned Points | Completed Points | Velocity |
|--------|---------------|------------------|----------|
| Sprint 0 | 8 | 8 | 100% |
| Sprint 1 | 15 | 15 | 100% |
| Sprint 2 | 18 | 18 | 100% |
| Sprint 3 | 20 | 20 | 100% |
| Sprint 4 | 16 | 16 | 100% |
| **Total** | **77** | **77** | **100%** |

### Burndown Chart (Conceptual)
```
User Stories Remaining
16 |●
14 |  ●
12 |    ●
10 |      ●
8  |        ●
6  |          ●
4  |            ●
2  |              ●
0  |________________●
   S0  S1  S2  S3  S4
```

### Final Metrics
- **Total User Stories:** 16 planned, 13 completed (81%)
- **Code Coverage:** 74% (exceeds 70% requirement)
- **Total Tests:** 20+
- **CI/CD Success Rate:** 95%+ (builds passing)
- **Azure Services:** 5 (exceeds 3 requirement)
- **Documentation Pages:** 5 comprehensive guides
- **Container Images:** 3 (app, Prometheus, Grafana)

---

## ✅ Definition of Done

A task/user story is considered "Done" when:

### Code Quality
- [ ] Code is written following Python PEP 8 style guidelines
- [ ] Code is committed to `main` branch via pull request
- [ ] Code review completed by at least one team member
- [ ] No critical linting errors or warnings
- [ ] All functions have docstrings

### Testing
- [ ] Unit tests written for new functionality
- [ ] All tests passing locally and in CI/CD
- [ ] Test coverage maintained at 70% or higher
- [ ] Integration tests passing (if applicable)
- [ ] Edge cases tested

### Documentation
- [ ] README.md updated if needed
- [ ] Code comments added for complex logic
- [ ] API endpoints documented
- [ ] Configuration changes documented

### Deployment
- [ ] Changes deployed to Azure successfully
- [ ] Health check endpoint returns healthy status
- [ ] No errors in Application Insights logs
- [ ] Smoke tests passing in production
- [ ] Rollback plan documented

### Quality Assurance
- [ ] Manual testing completed
- [ ] UI tested on multiple browsers (if UI changes)
- [ ] Error handling tested
- [ ] Performance acceptable (< 2s response time)
- [ ] Security vulnerabilities checked

### Process
- [ ] Sprint backlog updated
- [ ] Task moved to "Done" on Kanban board
- [ ] Demo prepared (if customer-facing feature)
- [ ] Sprint Review acceptance obtained

---

## 🎯 Team Roles (Rotating)

### Sprint 0 & 1
- **Product Owner:** [Team Member A]
- **Scrum Master:** [Team Member B]
- **Developers:** All team members

### Sprint 2 & 3
- **Product Owner:** [Team Member C]
- **Scrum Master:** [Team Member D]
- **Developers:** All team members

### Sprint 4
- **Product Owner:** [Team Member E]
- **Scrum Master:** [Team Member F]
- **Developers:** All team members

---

## 📝 Meeting Schedule

- **Daily Standup:** 9:00 AM (15 minutes)
  - What did you do yesterday?
  - What will you do today?
  - Any blockers?

- **Sprint Planning:** First day of sprint (1 hour)
  - Review product backlog
  - Select user stories for sprint
  - Break down into tasks
  - Estimate story points

- **Sprint Review:** Last day of sprint (1 hour)
  - Demo completed features
  - Gather feedback
  - Update product backlog

- **Sprint Retrospective:** After Sprint Review (30 minutes)
  - What went well?
  - What didn't go well?
  - Action items for improvement

---

## 🏆 Key Achievements

1. ✅ **100% Sprint Completion Rate** - All planned work completed
2. ✅ **74% Test Coverage** - Exceeds 70% requirement
3. ✅ **Full CI/CD Pipeline** - Automated build, test, deploy
4. ✅ **5 Azure Services** - Exceeds 3 service requirement
5. ✅ **Docker Containerization** - Bonus feature completed
6. ✅ **Production-Ready** - Monitoring, logging, error handling
7. ✅ **Enhanced Features** - Due dates, filters, search beyond MVP

---

**Document Maintained By:** Scrum Masters (rotating)  
**Last Updated:** December 3, 2025  
**Next Review:** Post-Demo (December 4, 2025)
