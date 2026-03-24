---
project: Jobili_main_dev
repository: Surjeet9700/Jobili_main_dev
license: MIT License
source_file: payment-testing-prd.md
source_url: https://github.com/Surjeet9700/Jobili_main_dev/blob/027e72ba63d925b633ec70de9aaca7d50ef5a9b7/payment-testing-prd.md
downloaded_at: 2025-12-05T10:46:37.525948+00:00
consensus_grade_level: 20.8
headings_per_sentence: 0.54
lists_per_sentence: 4.29
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.37
anaphora_per_sentence: 0.0
sentence_cv: 1.7
cpre_terms_per_sentence: 1.68
---
# Backend Services Testing Requirements

## Product Overview
Comprehensive job portal application with AI-powered job matching, automated applications, and subscription-based services.

## Core Backend Services to Test

### 1. User Registration & Authentication
- **Endpoints**: 
  - `POST /api/v1/auth/register`
  - `POST /api/v1/auth/login`
  - `GET /api/v1/auth/me`
- **Purpose**: User account creation and authentication
- **Expected Behavior**:
  - Create user with proper validation
  - Generate JWT tokens
  - Create related records (UserProfile, UserSettings, UserSecurity, UserSubscription, UsageQuota)
  - Handle duplicate email validation
  - Proper password hashing
  - Session management

### 2. Resume Upload & Management
- **Endpoints**:
  - `POST /api/v1/resume/upload`
  - `GET /api/v1/resume/files`
  - `DELETE /api/v1/resume/files/:fileId`
  - `GET /api/v1/resume/files/:fileId/download`
- **Purpose**: Resume file handling with ImageKit integration
- **Expected Behavior**:
  - Upload PDF files (max 5MB)
  - Store in ImageKit cloud or local storage
  - One resume per user enforcement
  - File validation and virus scanning
  - Proper transaction handling
  - Audit logging for deletions

### 3. AI Role Suggestions & Approval
- **Endpoints**:
  - `POST /api/v1/resume/analyze` - Analyze resume content
  - `POST /api/v1/resume/analyze-roles` - Generate role suggestions
  - `POST /api/v1/resume/approve-roles` - Approve/reject suggested roles
  - `GET /api/v1/resume/check-setup-complete` - Check if setup is complete
- **Purpose**: AI-powered role analysis and user approval
- **Expected Behavior**:
  - Analyze resume content and extract skills/experience
  - Generate role suggestions with match scores
  - Allow user to approve/reject roles
  - Store approved roles in ResumeAnalysis model
  - Update job preferences based on approved roles

### 4. Job Preferences Management
- **Endpoints**:
  - `POST /api/v1/resume/save-preferences` - Save job preferences
  - `GET /api/v1/resume/check-setup-complete` - Check setup status
- **Purpose**: Manage user job search preferences
- **Expected Behavior**:
  - Set preferred roles, locations, job types
  - Handle remote work preferences
  - Update UserProfile model with preferences
  - Validate location data against India states/cities
  - Auto-generate tasks when setup is complete

### 5. Platform Credentials Management
- **Endpoints**:
  - `GET /api/v1/settings/credentials/:platform` - Get platform credentials status
  - `POST /api/v1/settings/credentials/:platform` - Save platform credentials
  - `DELETE /api/v1/settings/credentials/:platform` - Remove platform credentials
  - `GET /api/v1/settings/naukri-credentials-status` - Get Naukri status
  - `GET /api/v1/settings/internshala-credentials-status` - Get Internshala status
- **Purpose**: Manage platform-specific credentials (Naukri, LinkedIn, Foundit, Wellfound, Internshala)
- **Expected Behavior**:
  - Encrypt and store credentials using AES encryption
  - Support 5 platforms: naukri, linkedin, foundit, wellfound, internshala
  - Validate credential formats and platform names
  - Handle credential updates and deletions
  - Auto-generate tasks when setup is complete
  - Provide application statistics per platform

### 6. Payment & Subscription System
- **Endpoints**:
  - `GET /api/v1/payment/plans` - Get available payment plans
  - `POST /api/v1/payment/create-order` - Create Razorpay payment order
  - `POST /api/v1/payment/verify` - Verify payment and update subscription
  - `GET /api/v1/payment/config` - Get Razorpay configuration
  - `POST /api/v1/payment/cancel` - Cancel subscription
  - `GET /api/v1/payment/subscription` - Get subscription status
  - `POST /api/v1/payment/webhook` - Razorpay webhook handler
- **Purpose**: Handle subscription payments and upgrades
- **Expected Behavior**:
  - Create Razorpay payment orders
  - Verify Razorpay payments with signature validation
  - Update UserSubscription, User, and UsageQuota models
  - Handle plan upgrades/downgrades
  - Manage billing cycles (monthly/yearly)
  - Update usage quotas based on plan
  - Proper transaction handling with rollback on failures

### 7. Profile Management
- **Endpoints**:
  - `GET /api/v1/profile` - Get complete user profile
  - `PUT /api/v1/profile` - Update user profile
  - `PUT /api/v1/profile/notifications` - Update notification settings
  - `GET /api/v1/profile/stats` - Get user statistics
  - `GET /api/v1/profile/analytics` - Get profile analytics
  - `DELETE /api/v1/profile` - Delete user account
- **Purpose**: Manage user profile information
- **Expected Behavior**:
  - Retrieve complete user profile with all related data
  - Update profile fields with validation
  - Handle notification preferences
  - Manage skills, experience, education
  - Update profile completion status
  - Provide user statistics and analytics

### 8. Settings Management
- **Endpoints**:
  - `GET /api/v1/settings/notifications` - Get notification settings
  - `PUT /api/v1/settings/notifications` - Update notification settings
  - `GET /api/v1/settings/auto-apply` - Get auto-apply settings
  - `PUT /api/v1/settings/auto-apply` - Update auto-apply settings
  - `GET /api/v1/settings/auto-apply/status` - Get auto-apply status
- **Purpose**: Manage user settings and preferences
- **Expected Behavior**:
  - Handle notification preferences (email frequency, weekly digest)
  - Manage auto-apply settings (enabled, max applications per day, min match score)
  - Validate settings data
  - Update user settings in database

### 9. Job Queue & Task Management
- **Endpoints**:
  - `POST /api/v1/job-queue/auto-generate` - Auto-generate tasks based on resume analysis
  - `GET /api/v1/job-queue/eligibility` - Check user eligibility for task generation
  - `POST /api/v1/job-queue/verify-and-generate` - Smart task verification and generation
  - `GET /api/v1/job-queue/dashboard` - Get comprehensive dashboard data
  - `GET /api/v1/job-queue/tasks` - Get user tasks with pagination
  - `POST /api/v1/job-queue/add` - Add manual job to queue
  - `POST /api/v1/job-queue/batch` - Batch add jobs
  - `PUT /api/v1/job-queue/tasks/:taskId` - Update task
  - `DELETE /api/v1/job-queue/tasks/:taskId` - Delete task
  - `POST /api/v1/job-queue/bulk-action` - Bulk actions on tasks
- **Purpose**: Manage job application tasks and automation
- **Expected Behavior**:
  - Auto-generate tasks based on user profile and preferences
  - Handle manual job additions
  - Manage task status (pending, processing, completed, failed)
  - Provide comprehensive dashboard with statistics
  - Handle bulk operations on tasks
  - Track application success rates and performance

### 10. Scheduler Management
- **Endpoints**:
  - `POST /api/v1/scheduler/create` - Create application schedule
  - `POST /api/v1/scheduler/bootstrap` - Bootstrap scheduler with user data
  - `GET /api/v1/scheduler/status` - Get current schedule status
  - `PUT /api/v1/scheduler/update` - Update schedule configuration
  - `POST /api/v1/scheduler/pause` - Pause schedule
  - `POST /api/v1/scheduler/resume` - Resume schedule
  - `GET /api/v1/scheduler/limits` - Get subscription limits for scheduling
  - `GET /api/v1/scheduler/availability/next` - Get next available time slots
  - `GET /api/v1/scheduler/statistics` - Get execution statistics
- **Purpose**: Manage automated job application scheduling
- **Expected Behavior**:
  - Create and manage application schedules
  - Handle time slot management
  - Respect subscription limits
  - Provide scheduling statistics
  - Handle schedule pause/resume operations

## Technical Requirements

### Database Operations
- **Transaction Handling**: All multi-document operations must be atomic
- **Session Management**: Proper handling in development vs production
- **Data Validation**: Zod schema validation for all inputs
- **Error Handling**: Comprehensive error handling and logging

### Security
- **Authentication**: JWT token validation
- **Authorization**: Role-based access control
- **Data Encryption**: Sensitive data encryption
- **Input Sanitization**: Prevent injection attacks

### Performance
- **Response Times**: API responses under 2 seconds
- **Concurrent Users**: Handle multiple simultaneous requests
- **Database Queries**: Optimized queries with proper indexing
- **File Uploads**: Efficient file handling and storage

## Test Scenarios

### Happy Path Testing
1. User registration → Login 
2. Resume upload → AI analysis → Role approval
3. Job preferences setup → Platform credentials
4. Payment upgrade → Subscription activation
5. Email notifications → Profile updates

### Error Handling Testing
1. Invalid input validation
2. Authentication failures
3. File upload errors
4. Payment verification failures
5. Database transaction failures
6. External service failures (ImageKit, Razorpay, Email)

### Edge Cases
1. Duplicate user registration
2. Large file uploads
3. Network timeouts
4. Concurrent operations
5. Session expiration
6. Invalid payment data

## Success Criteria
- All endpoints respond correctly
- Database transactions are atomic
- Error handling is comprehensive
- Security measures are in place
- Performance meets requirements
- Logging and monitoring work properly
