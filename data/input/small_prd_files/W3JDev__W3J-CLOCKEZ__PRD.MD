---
project: W3J-CLOCKEZ
repository: W3JDev/W3J-CLOCKEZ
license: MIT License
source_file: PRD.MD
source_url: https://github.com/W3JDev/W3J-CLOCKEZ/blob/c4432926b17c67a5d2cd6afe72715c15657a1f48/PRD.MD
downloaded_at: 2025-12-05T10:29:40.163613+00:00
---

## **Product Requirements Document: Staff Attendance Application**

**1\. Introduction & Purpose**

This document defines the requirements for the Staff Attendance Application, a system designed to streamline and modernize employee time tracking. The application will consist of two main interfaces: a staff-facing Kiosk for clock-in/out and an Admin Dashboard for management and reporting. The primary purpose is to provide an accurate, efficient, and user-friendly solution for tracking employee attendance, calculating work hours, and generating relevant reports, initially targeted towards businesses like F\&B establishments in Malaysia (e.g., Table & Apron).

**2\. Goals & Objectives**

* **Goal 1:** Improve accuracy of attendance tracking and reduce manual errors.  
  * *Objective 1.1:* Implement reliable clock-in/out methods (PIN, Face Scan).  
  * *Objective 1.2:* Automate calculation of work hours, including handling potential complexities like overnight shifts.  
* **Goal 2:** Enhance operational efficiency for staff and management.  
  * *Objective 2.1:* Provide a fast and intuitive Kiosk interface for staff.  
  * *Objective 2.2:* Offer a centralized Admin Dashboard for easy access to data and management tasks.  
  * *Objective 2.3:* Streamline the process for handling missed punches or corrections.  
* **Goal 3:** Provide actionable insights for management.  
  * *Objective 3.1:* Generate clear reports on attendance patterns (lateness, absences).  
  * *Objective 3.2:* Provide data summaries for payroll processing.  
  * *Objective 3.3:* Offer a real-time view of currently clocked-in staff.  
* **Goal 4:** Deliver a modern and professional user experience.  
  * *Objective 4.1:* Implement a sleek, clean, iOS-inspired UI for both Kiosk and Dashboard.  
  * *Objective 4.2:* Ensure the application is responsive and performs well.

**3\. Target Audience**

* **Staff Members:** Employees who need to record their work start and end times. May have varying levels of technical proficiency. (e.g., FOH staff, BOH staff).  
* **Administrators / Managers:** Personnel responsible for managing employees, overseeing attendance, processing payroll, and configuring the system (e.g., Restaurant Manager, HR personnel).

**4\. Scope**

**4.1. In Scope:**

* **Kiosk Application:**  
  * User Authentication (4-digit PIN, Face Scan \- requires external library/service integration).  
  * Clock-In / Clock-Out functionality.  
  * Display of current time.  
  * Interface for submitting manual entry requests (for missed punches).  
  * Link/Button for Admin Access (triggers separate login/redirect).  
* **Admin Dashboard Application (Web):**  
  * Secure Admin Login.  
  * Dashboard Overview: Real-time status (who's in), key stats (late count, hours today), pending approvals summary, weekly hours chart.  
  * Timesheet Management: View detailed attendance records, filter by date/employee/status, pagination. Admin ability to add/edit records (with audit trail).  
  * Employee Management: Add, view, edit, activate/deactivate employee profiles. Store basic info, PIN, associate Face Scan data reference. Face Scan registration flow UI.  
  * Reporting: Generate reports (Payroll Hours Summary, Late Arrivals, Absences). View reports within the dashboard. Export reports (CSV, PDF \- generation handled by backend).  
  * Manual Entry Approval Workflow: View submitted requests, approve/reject them.  
  * Settings: Configure company profile, attendance rules (grace period, OT threshold), Kiosk options (enable/disable face scan), basic appearance settings.  
* **General:**  
  * Calculation logic for total hours, overtime, and status (Late, On Time, etc.).  
  * Basic light/dark mode support based on system preference.  
  * Responsive design for the Admin Dashboard (usable on desktop/tablet).

**4.2. Out of Scope (for initial version):**

* Advanced Role-Based Access Control (beyond basic Admin/Staff).  
* Leave Management (Requesting/Approving PTO, Sick Leave, etc.).  
* Shift Scheduling and Assignment.  
* Automated break time deductions (unless explicitly clocked).  
* Direct integration with specific payroll systems (reports will provide data *for* payroll).  
* Generating legally compliant, localized payslips directly (template structure provided for guidance only).  
* Offline Kiosk functionality.  
* Native mobile applications (focus is on web dashboard and potentially web-based kiosk).  
* Advanced analytics and predictive reporting.

**5\. Functional Requirements**

**5.1. Kiosk Module**

* REQ-K-001: The Kiosk MUST display the current time accurately based on the configured timezone.  
* REQ-K-002: The Kiosk MUST allow staff to authenticate using a unique 4-digit PIN.  
* REQ-K-003: The Kiosk MUST provide visual feedback during PIN entry (e.g., filled dots).  
* REQ-K-004: The Kiosk SHOULD allow staff to authenticate using Face Scan (requires integration).  
* REQ-K-005: The Kiosk MUST display clear instructions and feedback during the Face Scan process (simulation or real).  
* REQ-K-006: Upon successful authentication, the Kiosk MUST identify the employee and determine if they are currently clocked in or out.  
* REQ-K-007: The Kiosk MUST present the correct action ("Clock In" or "Clock Out") based on the employee's current status.  
* REQ-K-008: The Kiosk MUST record the timestamp accurately upon successful Clock In or Clock Out action.  
* REQ-K-009: The Kiosk MUST provide clear success confirmation after Clock In/Out.  
* REQ-K-010: The Kiosk MUST handle authentication failures (Invalid PIN, Face Not Recognized) gracefully with appropriate user feedback.  
* REQ-K-011: The Kiosk MUST provide an interface for authenticated staff to submit requests for manual entry (Date, Time, Type, Reason).  
* REQ-K-012: The Kiosk MUST provide a button/link to access the Admin Dashboard (triggering login/redirect).

**5.2. Dashboard Module \- General**

* REQ-D-001: The Dashboard MUST require secure login for Admin/Manager users.  
* REQ-D-002: The Dashboard MUST provide clear navigation (Sidebar) to all main sections.  
* REQ-D-003: The Dashboard UI MUST be responsive and usable on standard desktop and tablet screen sizes.

**5.3. Dashboard Module \- Overview**

* REQ-D-101: The Overview page MUST display the count of currently clocked-in staff.  
* REQ-D-102: The Overview page MUST display key stats for the current day (e.g., number of late arrivals, total hours logged).  
* REQ-D-103: The Overview page MUST display a summary/count of pending manual entry requests requiring approval.  
* REQ-D-104: The Overview page MUST display a visual chart summarizing recent activity (e.g., hours logged per day for the past week).  
* REQ-D-105: The Overview page SHOULD display a list of recent exceptions or key activities (e.g., late arrivals today, missing punches).

**5.4. Dashboard Module \- Timesheets**

* REQ-D-201: The Timesheets page MUST display a detailed list/table of attendance records.  
* REQ-D-202: The Timesheets page MUST allow filtering records by Date Range.  
* REQ-D-203: The Timesheets page MUST allow filtering records by Employee.  
* REQ-D-204: The Timesheets page SHOULD allow filtering records by Status (Late, Missing Punch, Pending, etc.).  
* REQ-D-205: The Timesheets table MUST display Date, Employee Name, Clock In Time, Clock Out Time, Calculated Total Hours, and Status/Notes for each record.  
* REQ-D-206: The Timesheets page MUST support pagination for large datasets.  
* REQ-D-207: Admins MUST be able to add a manual attendance entry from the Timesheets page.  
* REQ-D-208: Admins MUST be able to edit existing attendance records (e.g., correct times, add notes). All edits MUST be logged for audit purposes (backend requirement).  
* REQ-D-209: Admins MUST be able to approve or reject pending manual entry requests viewed via the Timesheets page or linked from the Overview.

**5.5. Dashboard Module \- Employees**

* REQ-D-301: The Employees page MUST display a list/table of all registered employees.  
* REQ-D-302: The Employees table MUST display Employee Name, Employee ID, Role, Contact Info (optional), and Status (Active/Inactive).  
* REQ-D-303: Admins MUST be able to add a new employee profile, including Name, ID, Role, Contact, Kiosk PIN.  
* REQ-D-304: The system MUST provide a UI flow for registering an employee's face scan data, associated with their profile.  
* REQ-D-305: Admins MUST be able to edit existing employee profiles.  
* REQ-D-306: Admins MUST be able to Activate or Deactivate employee profiles. Deactivated employees should not be able to log in via Kiosk but their historical data MUST be retained.  
* REQ-D-307: The Employees page MUST provide search functionality (by Name or ID).  
* REQ-D-308: The Employees page SHOULD allow filtering by Status (Active/Inactive).  
* REQ-D-309: The Employees page MUST support pagination.

**5.6. Dashboard Module \- Reports**

* REQ-D-401: The Reports page MUST allow selection of different report types (Payroll Summary, Late Arrivals, Absences minimum).  
* REQ-D-402: The Reports page MUST allow specifying a Date Range for report generation.  
* REQ-D-403: The Reports page MAY require additional filters (e.g., Employee) depending on the selected report type.  
* REQ-D-404: The system MUST generate the selected report based on the provided filters and display it within the dashboard.  
* REQ-D-405: The system MUST provide functionality to export generated reports in CSV format.  
* REQ-D-406: The system SHOULD provide functionality to export generated reports in PDF format.

**5.7. Dashboard Module \- Settings**

* REQ-D-501: The Settings page MUST allow configuration of basic Company Profile information (Name, Address).  
* REQ-D-502: The Settings page MUST allow configuration of attendance rules: Late Arrival Grace Period (minutes), Weekly Overtime Threshold (hours).  
* REQ-D-503: The Settings page MUST allow configuration of the system's Timezone.  
* REQ-D-504: The Settings page MUST allow enabling/disabling the Face Scan login option on the Kiosk.  
* REQ-D-505: The Settings page SHOULD provide an option to manage Appearance settings (e.g., manual Light/Dark mode override toggle).

**5.8. General Functional Requirements**

* REQ-G-001: The system MUST accurately calculate total work hours based on clock-in/out times, considering potential overnight shifts.  
* REQ-G-002: The system MUST accurately calculate overtime hours based on configured thresholds.  
* REQ-G-003: The system MUST correctly determine attendance status (On Time, Late, Absent, Missing Punch) based on configured rules and shift schedules (if implemented).

**6\. Non-Functional Requirements**

* **Performance:**  
  * Kiosk login/logout actions should complete within 2 seconds (excluding network latency for verification).  
  * Dashboard pages (list views) should load within 3 seconds with typical data volume.  
  * Report generation time should be reasonable (e.g., \< 10-15 seconds for standard reports).  
* **Security:**  
  * Admin passwords and staff PINs MUST be securely hashed and stored.  
  * Face scan data (embeddings/templates) MUST be stored securely.  
  * Communication between Kiosk/Dashboard and Backend MUST use HTTPS.  
  * Implement protection against common web vulnerabilities (e.g., XSS, CSRF, SQL Injection).  
* **Usability:**  
  * Kiosk interface MUST be simple, intuitive, and require minimal training for staff.  
  * Dashboard interface MUST be clean, organized, and easy for admins to navigate and find information.  
  * Error messages MUST be clear and helpful.  
  * Follow design guidelines consistently.  
* **Reliability:**  
  * The system should have high availability, especially the Kiosk for clock-in/out.  
  * Data backups should be performed regularly (backend requirement).  
* **Maintainability:**  
  * Code should be well-structured, commented, and follow chosen framework (React) best practices.  
  * Configuration settings should be easily manageable.

**7\. Design Guidelines**

* Adhere to the **"3D dynamic, high-end Apple iOS inspired, clean, modern, sleek, attractive view"** aesthetic defined previously.  
* Key elements: Translucency/blur, rounded corners, clean typography (e.g., Inter or system fonts), minimalist icons, subtle shadows for depth, smooth transitions, clear visual hierarchy, light/dark mode support.  
* Ensure consistency across Kiosk and Dashboard interfaces.

**8\. Success Metrics**

* Reduction in payroll processing time/errors reported by admin.  
* Reduction in time taken for staff to clock in/out.  
* High adoption rate and positive feedback from staff and admin users.  
* Reduction in reported instances of missed punches requiring manual correction.  
* System uptime and performance meeting NFR targets.

**9\. Future Considerations**

* Leave Management module.  
* Advanced Shift Scheduling.  
* Mobile App for Staff/Admin.  
* Direct Payroll System Integration.  
* Geofencing for clock-in/out.  
* More detailed analytics and dashboards.  
* Multi-language support.

Staff Attendance App

an efficient, user-friendly Staff Attendance Application (Kiosk \+ Admin Dashboard) for businesses like F\&B (e.g., Table & Apron).  
 Target Audience:  
     Staff: Quick PIN/Face Scan clock-in/out, submit corrections.  
     Admin/Managers: Manage staff, view real-time data, generate reports (payroll/analysis), manage shifts (opt.), approve corrections, configure settings.  
 Goals: Accurate time tracking, simplified clocking, reduced payroll errors, attendance insights, modern UX.

2\. Core Features  
 Kiosk: PIN/Face Scan Login, Clock-In/Out, Manual Entry Submission.  
 Dashboard: Overview (stats, pending requests, charts, activity), Timesheet Management (view, filter, edit), Employee Management (add/edit/deactivate \+ Face Scan reg), Reporting, Settings, Manual Entry Approval.

3\. Key User Flows  
 Staff Clock-In/Out (PIN/Face Scan): Staff approaches Kiosk, selects method (PIN/Face). Authenticates (enters 4-digit PIN or positions face for scan). System verifies. Displays staff name & status (In/Out), prompts relevant action (Clock In/Clock Out). Staff taps action. Success confirmation shown, timestamp recorded. Kiosk resets. Handles errors (Invalid PIN, Face Not Recognized, Camera issues).  
 Staff Manual Entry (Kiosk): Staff authenticates, accesses form. Enters missing punch details (Date, Time, Type, Reason). Submits request for Admin approval. Confirmation shown. Kiosk resets.  
 Admin Add Employee (+ Face Scan Reg): Admin uses Dashboard form (Name, ID, Role, Contact, PIN). Optionally initiates Face Registration (requires employee present): UI prompts face positioning via camera feed, captures data, processes embedding (via library/service), confirms success/failure. Admin saves employee record (details, PIN hash, face embedding/ref stored securely). List updates.  
 Admin Dashboard View: Logs in, sees overview: Stat cards (Staff In, Late, etc.), pending approvals list, hours chart, recent activity/exceptions table.  
 Admin Timesheet Mgt: Navigates to Timesheets. Filters data (Date Range, Employee, Status). Views filtered records in table. Can edit/view details of specific entries. Uses pagination.  
 Admin Approve Manual Entry: Accesses pending request (via Dashboard/Timesheets). Reviews details (Employee, Date, Time, Type, Reason). Clicks Approve/Reject. System updates record/status.  
 Admin Generate Report: Navigates to Reports. Selects type (e.g., Payroll Summary), date range. Clicks Generate. Views report data (table format). Optionally exports (CSV/PDF).

4\. Wireframes (Conceptual Layout)  
 Kiosk: Centered layout. Initial screen (Clock, PIN/Face buttons, Manual Entry/Admin links). PIN entry (Dots, Keypad). Face Scan (Camera view placeholder/frame, instructions). Manual Entry (Modal form).  
 Dashboard: Two-column: Fixed Sidebar (Nav: Dashboard, Timesheets, Employees, Reports, Settings), Fluid Main Content Area (Page Header \+ dynamic content). Specific pages use grids/cards for stats, charts, tables (Timesheets, Employees, Reports), forms (Settings, Add Employee Modal).

5\. Design Language  
 Style: Clean, modern, sleek, high-end iOS-inspired. Dynamic 3D feel.  
 Elements: Clean grids, whitespace. Translucency/blur (sidebar/modals), subtle shadows (depth). Rounded corners. Clear typography hierarchy (system fonts/web alternatives). Neutral backgrounds \+ vibrant accent color. Minimalist line icons.  
 Dynamics: Smooth, subtle transitions/animations (hover, modals, charts). Interactive feedback (button press scale).

6\. Calculation Logic  
 Status: On Time (In \<= Start \+ Grace), Late (In \> Start \+ Grace), Absent (No Clock In for scheduled shift), Missing Punch (In/Out missing), Complete (In & Out exist).  
 Total Hours: Duration(Clock Out \- Clock In) \- Breaks. Handles overnight shifts.  
 Overtime: Based on rules (e.g., \> Threshold hours/week, configurable). Weekly OT \= MAX(0, Total Weekly Hours \- Threshold).  
 Absences: Flagged if scheduled shift has no corresponding Clock In (and no approved leave).

7\. Reporting  
 Types: Individual Report Card (Emp Name, Period Stats: Total/OT Hrs, Days, Late/Absence Counts, Avg Times, Daily Log), Payroll Summary (Emp Name/ID, Regular/OT/Total Hrs), Late Arrival Report (Date, Emp, Scheduled/Actual In, Duration), Absence Report (Date, Emp, Shift, Notes).  
 Filters: Date Range, Employee (optional). Export options (CSV/PDF).

8\. Payslip Format (Malaysia)  
 Structure: Requires Company/Employee Info, Pay Period, Earnings (Basic, OT, Allowances), Deductions (EPF, SOCSO, EIS, PCB, Loans), Net Pay, Employer Contributions per Employment Act 1955\. Recommend localized payroll software for compliance.

9\. Face Scan Registration (Admin Flow Detail)  
 Triggered from Add/Edit Employee form. Requires employee presence. UI shows camera feed, guides positioning. Library captures frames/video, processes to create facial embedding (numerical representation, not image). Frontend receives embedding/ref. On save, backend stores employee data \+ secure embedding/ref. Handles camera permissions, detection quality, success/failure feedback  