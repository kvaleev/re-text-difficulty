---
project: move-metrics-backend
repository: coeus-solutions/move-metrics-backend
license: Unknown
source_file: MoveMetricsPRD.md
source_url: https://github.com/coeus-solutions/move-metrics-backend/blob/03f1ed7d1584fcb46abdbf59567935fb8f4d9be2/MoveMetricsPRD.md
downloaded_at: 2025-12-05T10:54:30.337567+00:00
consensus_grade_level: 12.5
headings_per_sentence: 0.24
lists_per_sentence: 0.83
smao_sentences_pct: 0.8
vague_words_per_sentence: 0.15
anaphora_per_sentence: 0.03
sentence_cv: 0.975
cpre_terms_per_sentence: 0.46
---
**Product Requirements Document (PRD)**

# **MoveMetrics**

---

## **Objective**
Create a system that allows users to research and compare the cost of living in cities. Users can specify their current city, a list of potential cities to move to, and their family size. The system will analyze relevant parameters using an agent and provide recommendations based on the cost of living and other factors.

---

## **Target Audience**
- Individuals or families planning to relocate.
- Businesses assisting employees with relocation.
- Expats and immigrants researching affordable living options.

---

## **Core Features**

### **1. User Authentication**
- **Feature:** JWT bearer-based authentication.
- **Details:**
  - Users must sign up and log in to use the system.
  - Secure authentication for accessing and storing user-specific data.

### **2. City Comparison Engine**
- **Feature:** Allow users to compare cost-of-living data between cities.
- **Input Parameters:**
  - Current city (e.g., Berlin).
  - Potential cities to move to (e.g., Austin, Bay Area, Seattle).
  - Family size.
- **Output:**
  - Comparison of key parameters such as housing costs, groceries, utilities, transportation, healthcare, and education.
  - Overall cost index and ranking of cities.

### **3. Recommendations Engine**
- **Feature:** Provide tailored recommendations based on user input.
- **Details:**
  - Recommend cities based on cost efficiency and user preferences.
  - Highlight pros and cons for each city.

### **4. Agent Integration**
- **Feature:** Microsoft Autogen for intelligent analysis.
- **Details:**
  - Agent to fetch and process real-time data from APIs or trusted sources.
  - Perform contextual analysis to generate meaningful insights.

### **5. Dashboard**
- **Feature:** Interactive dashboard for comparison and insights.
- **Details:**
  - Visualize cost-of-living data with charts and tables.
  - Enable users to filter and sort data by categories such as housing, groceries, transportation, etc.
  - Allow comparisons side-by-side for multiple cities.
  - Provide users the ability to save comparisons and export results as CSV or PDF.
  - Include drill-down capabilities for each cost category to provide detailed subcategory data.
  - Integrate an interactive map showing city locations and additional geographic insights.
  - Implement trend analysis to show historical cost-of-living changes in cities.

### **6. Data Storage**
- **Feature:** Store user preferences and comparison history.
- **Details:**
  - Use Supabase as the database backend.
  - Persist user data securely for future reference.
  - Enable secure deletion of user data upon request.

### **7. Parameterized Analysis**
- **Feature:** Advanced filtering and parameter adjustments.
- **Details:**
  - Allow users to adjust weightage of parameters (e.g., prioritize housing or transportation costs).
  - Provide dynamic recalculations based on user-modified criteria.

---

## **Non-Core Features (Future Enhancements)**
- Multi-language support.
- AI-driven insights on quality of life.
- User reviews and feedback on cities.
- Integration with job market data.

---

## **Technical Requirements**

### **Frontend:**
- **Technology:** React.js
- **Features:**
  - User-friendly interface for inputting city and family size details.
  - Dynamic dashboard for displaying recommendations.
  - Responsive design for mobile and desktop users.

### **Backend:**
- **Technology:** Python FastAPI
- **Features:**
  - Handle user authentication and API requests.
  - Communicate with the agent for fetching and analyzing data.
  - Provide APIs for the frontend to access user-specific insights.

### **Database:**
- **Technology:** Supabase
- **Features:**
  - Store user information, input data, and comparison results.
  - Secure data with authentication and authorization.

### **Agent:**
- **Technology:** Microsoft Autogen (https://microsoft.github.io/autogen/0.2/)
- **Features:**
  - Automate data gathering and contextual analysis.
  - Integrate with external APIs for up-to-date cost-of-living data.

### **Authentication:**
- **Mechanism:** JWT bearer-based authentication.
- **Features:**
  - Secure token issuance and validation.
  - Role-based access control if required.

---

## **Workflow**

1. **User Login/Signup:**
   - Users sign up or log in using JWT-based authentication.

2. **Input Collection:**
   - User provides current city, potential cities, and family size.

3. **Data Fetching and Analysis:**
   - The backend triggers the agent to gather relevant data for the cities provided.
   - Agent processes and returns insights.

4. **Comparison and Visualization:**
   - Backend sends analyzed data to the frontend.
   - Frontend displays the comparison results in an interactive dashboard.

5. **Recommendations:**
   - Backend computes tailored recommendations and sends them to the frontend.

6. **User Actions:**
   - User saves preferences or revisits comparison history.
   - User exports comparison data for offline use.

---

## **API Endpoints**

### **Authentication**
- `POST /auth/signup`: Register a new user.
- `POST /auth/login`: Authenticate user and issue JWT.
- `GET /auth/logout`: Invalidate the current session.

### **User Management**
- `GET /user/profile`: Retrieve user profile information.
- `PUT /user/profile`: Update user profile.

### **City Comparison**
- `POST /compare`: Submit cities and family size for comparison.
- `GET /compare/history`: Retrieve saved comparison history.
- `DELETE /compare/history/{id}`: Delete a specific comparison entry.

### **Recommendations**
- `GET /recommendations`: Fetch tailored recommendations for the user.

---

## **Database Design**

### **Users Table**
| Column       | Type        | Constraints         |
|--------------|-------------|---------------------|
| id           | UUID        | Primary Key         |
| email        | String      | Unique, Not Null    |
| password     | String      | Hashed, Not Null    |
| created_at   | Timestamp   | Default Now         |
| updated_at   | Timestamp   |                     |

### **Comparisons Table**
| Column       | Type        | Constraints         |
|--------------|-------------|---------------------|
| id           | UUID        | Primary Key         |
| user_id      | UUID        | Foreign Key (Users) |
| current_city | String      | Not Null            |
| potential_cities | JSONB   | Not Null            |
| family_size  | Integer     | Not Null            |
| results      | JSONB       |                     |
| created_at   | Timestamp   | Default Now         |

---

## **Acceptance Criteria**
- Users can sign up and log in using JWT-based authentication.
- Users can input cities and family size for comparison.
- System fetches and displays cost-of-living data with recommendations.
- Dashboard is interactive and visually intuitive.
- Data is stored securely in Supabase.
- Agent performs accurate data analysis and returns meaningful insights.
- Users can adjust parameters dynamically and receive updated results.

---

## **KPIs**
- Number of user sign-ups and active sessions.
- Average time spent on the platform.
- User satisfaction with recommendations (via feedback form).
- System response time and data accuracy.

---

## **Risks and Mitigations**

1. **Risk:** Lack of real-time data accuracy.
   - **Mitigation:** Use multiple trusted APIs and cross-verify data.

2. **Risk:** Slow system performance with agent integration.
   - **Mitigation:** Optimize backend processes and agent queries.

3. **Risk:** Security vulnerabilities with JWT and database.
   - **Mitigation:** Implement robust security practices (e.g., token expiration, encryption).

---

## **Conclusion**
MoveMetrics will provide users with a robust and user-friendly platform to analyze and compare cities based on cost-of-living parameters. With an advanced functionality set, the system ensures a comprehensive and personalized experience for users planning relocations.


