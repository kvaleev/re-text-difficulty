---
project: shift-agents-store
repository: Rhynorater/shift-agents-store
license: Unknown
source_file: projectPRD.md
source_url: https://github.com/Rhynorater/shift-agents-store/blob/f0af9160dfe2f67e1f138d7932a820cc207812e0/projectPRD.md
downloaded_at: 2025-12-05T10:40:07.782144+00:00
consensus_grade_level: 10.3
headings_per_sentence: 0.08
lists_per_sentence: 0.14
smao_sentences_pct: 0.8
vague_words_per_sentence: 0.08
anaphora_per_sentence: 0.03
sentence_cv: 1.051
cpre_terms_per_sentence: 0.25
---
# **Product Requirements Document: Caido Shift Agent Prompt Store**

| Key Information | Value |
| :---- | :---- |
| **Product Name** | Caido Shift Agent Prompt Store |
| **Target Integration** | Caido HTTP Proxy (Shift Agents) |
| **Current Status** | Requirements Finalized |
| **Backend Technology** | Python Flask |
| **Database** | SQLite (Single File) |
| **Frontend Technology** | HTML, CSS (Tailwind), Vanilla JavaScript |
| **Deployment** | Docker |

## **1\. Introduction**

The Caido Shift Agent Prompt Store aims to provide a centralized, easy-to-use repository for sharing and discovering community-contributed prompt agents compatible with the Caido HTTP proxy's Shift Agents feature. The goal is to foster community engagement and accelerate the adoption and utility of micro-agent prompts within the security and development ecosystems. The platform will be deployed as a single, self-contained Docker container.

## **2\. Goals & Objectives**

1. **Centralize Discovery:** Create a single source of truth for Caido Shift Agent prompts.  
2. **Ease of Submission:** Implement a streamlined process for users to submit new prompts via GitHub Gists.  
3. **Real-time Synchronization:** Ensure prompt content is always up-to-date and automatically removed if the source Gist is deleted or made private.  
4. **Admin Control:** Provide a simple, token-authenticated administrative interface for content moderation.  
5. **Aesthetic Consistency:** Maintain a design aesthetic consistent with the official Caido branding, leveraging the provided Tailwind color palette.

## **3\. Design & Aesthetic Requirements (Caido-Inspired)**

The application’s styling must strictly adhere to the provided Tailwind configuration, aiming for a dark, professional, and minimalist aesthetic consistent with security tooling like Caido.

### **3.1. Color Palette**

The provided custom colors (Primary, Secondary, Surface) must be used for all UI elements, backgrounds, and interactive states. Specifically:

| Element | Suggested Color Palette |
| :---- | :---- |
| **Background/Surface** | surface-900 or surface-800 (Dark, deep gray/blue) |
| **Primary Accent/Buttons** | primary-500 to primary-700 (Red/Pink/Maroon tones) |
| **Secondary Accent/Highlights** | secondary-300 to secondary-500 (Orange/Amber tones) |
| **Text** | surface-0 or surface-200 (Off-white/light gray) |

### **3.2. General UI Principles**

* **Minimalism & Density:** Utilize clean lines, generous padding, and clear hierarchy, avoiding clutter.  
* **Rounded Corners:** All interactive elements, cards, and input fields must use rounded corners (rounded-lg or similar).  
* **Layout:** The main prompt viewing area should feel like a dense but readable data list or set of cards, similar to a file explorer or log viewer found in security applications.  
* **Font:** Default to a clean, highly readable sans-serif font (e.g., Inter, if available, or a system default).

## **4\. Functional Requirements: User Interface (Frontend)**

The public interface must be a single-page application (SPA) built with HTML, Tailwind CSS, and Vanilla JavaScript, communicating exclusively with the Flask JSON API.

### **4.1. SPA Routing (Query Parameters)**

The frontend will use query parameters for client-side navigation, ensuring shareable URLs.

* **Main Store View:** index.html?view=store  
* **Submission Form:** index.html?view=submit  
* **Admin Interface:** index.html?view=admin  
* **Specific Prompt View:** Prompts must be linked using the Gist identifier for shareability. The URL must contain the Gist's username and ID (e.g., index.html?view=prompt\&gist\_ref=username/id).

### **4.2. Prompt Submission**

Users must submit a form containing the following fields:

| Field | Requirement | Type | Notes |
| :---- | :---- | :---- | :---- |
| **Author Name** | Required | Text Input | Display name for the author. **Must match regex ^\[a-zA-Z\\s\\.\\-'\]{2,100}$ (2-100 characters).** |
| **GitHub Gist URL** | Required | URL Input | Must point to a public GitHub Gist URL. **The URL must parse to the canonical username/id format.** The author's GitHub username will be extracted by the backend from this URL and stored as a required social link. |
| **Tags** | Optional | Text Input | Comma-separated tags. **Max 5 tags.** Each tag must match regex \[a-zA-Z\\-\_\]{1,64}. |
| **X (Twitter) Handle** | Optional | Text Input | Author social link. **Must match regex ^@?\[a-zA-Z0-9\_\]{1,15}$ (Max 15 characters).** |
| **LinkedIn URL** | Optional | URL Input | Author social link. **Must match regex ^https?:\\/\\/(www\\.)?linkedin\\.com\\/.\*$ (Valid LinkedIn URL).** |
| **Discord Handle** | Optional | Text Input | Author social link. **Must match regex ^\[a-z0-9\\.\_\\-\]{2,32}$ (Modern Discord username, 2-32 lowercase characters).** |
| **Email** | Optional | Email Input | For communication (if needed). **Must match strict email regex and be between 5 and 128 characters.** |
| **Submit Button** | Action | Button | Submits data to the backend API (/api/submit). |

**Submission Flow:**

1. User fills out the form.  
2. Upon submission, the backend immediately attempts to fetch and parse the Gist. **The Gist must contain at least one Markdown file (.md). The system will always select the *first* .md file in the Gist to be the prompt content.** The frontend should validate the URL format and all input fields using the defined regexes.  
3. The submission status (pending approval, immediate approval, or requiring Captcha) is based on Admin settings. **The reCAPTCHA token must be included in the JSON payload sent to the backend for server-side verification.**

### **4.3. Prompt Viewing (Store Frontend)**

The main view must display all approved prompts in a sortable/searchable list.

| Feature | Requirement |
| :---- | :---- |
| **Search Function** | Single text input that searches across the Gist description (from GitHub) and the Markdown file name. |
| **Tag Filtering** | Display a list of all unique, approved tags with counts. Clicking a tag filters the main list to show only matching prompts. |
| **Author Filtering** | Display a list of all unique authors. Clicking an author filters the main list. |
| **Sorting** | The default sort order must be by **Gist Stars (Most Rated First)**. |
| **Copy Function** | A prominent "Copy Prompt" button (or icon) must be available for each prompt entry. This button copies the raw Markdown content (prompt\_body) to the user's clipboard for direct import into Caido. |
| **Prompt Card Details** | Each card must display: Gist Description, File Name, Author Name, Gist Star Count, associated Tags, and **GitHub Username**. |
| **Real-time Content Display** | When a user views a specific prompt (e.g., via the ?view=prompt\&gist\_ref=username/id URL), the client-side JavaScript **must perform a real-time fetch** using the GitHub Gist JSON API to embed the content, ensuring the absolute freshest version is displayed, regardless of the server-side cache status. |

## **5\. Functional Requirements: Admin Interface**

The Admin interface is a separate section of the site, accessible via a token.

### **5.1. Authentication**

* Access is granted by setting an Authorization header containing the generated ADMIN\_TOKEN.  
* A client-side login form will allow the token to be stored in the browser session (e.g., LocalStorage) for subsequent API calls.  
* The token is generated on Docker startup and stored in the SQLite database's admin table.

### **5.2. Admin Settings**

A dedicated settings panel to toggle core application behaviors:

| Setting | Type | Default | Notes |
| :---- | :---- | :---- | :---- |
| **Captcha Enabled** | Toggle (On/Off) | Off | If ON, new submissions require passing a Captcha before being processed. **Implementation uses Google reCAPTCHA (v2 or v3), requiring client-side integration and API keys provisioned via Docker environment variables.** |
| **Approval Required Mode** | Toggle (On/Off) | Off | If ON, all new prompt submissions enter a pending state and must be manually approved by an admin before appearing in the public store. |

### **5.3. Approval Table**

If Approval Required Mode is ON, this table lists all pending submissions.

| Field | Requirement |
| :---- | :---- |
| **Data Displayed** | All submitted fields: Author Name, Gist URL, Tags, Gist Description, File Name, and Gist Star count. |
| **Actions** | **Approve:** Sets is\_approved \= TRUE. **Reject:** Deletes the database entry. **View:** A mechanism to view the raw Gist content before approval. |

## **6\. Technical Requirements & Architecture**

### **6.1. Backend (Flask JSON API)**

* **Language:** Python 3 \+ Flask.  
* **Production WSGI Server:** The application must be served using **Gunicorn (Green Unicorn)** in the Docker container for production stability and performance.  
* **Data Source Interaction:** The backend must handle all interaction with the SQLite database and the GitHub Gist API.  
* **Gist URL Parsing:** The Gist URL validation and parsing **must strictly extract the canonical Gist reference (username/id) from the input URL** (e.g., https://gist.github.com/username/{id}), ignoring any other URL variations.  
* **Database Initialization:** The Flask application **must check on startup** for the existence of prompts.db and the required tables/settings/token. If missing, it must run the schema creation and initial ADMIN\_TOKEN generation logic and print the token to the container logs.  
* **GitHub API Check:** A background task must run every **hour (60 minutes)** to perform the following checks for every approved prompt:  
  1. Fetch the Gist details.  
  2. If the Gist is explicitly confirmed deleted or private, the prompt **must be deleted** from the store.  
  3. If the check fails due to a transient error (API limits, network issue, etc.), the consecutive\_sync\_failures counter must be incremented. The prompt is **only deleted after three consecutive failures**. A successful check resets the counter to zero. **No automated notification will be sent to the author upon removal.**  
  4. Update the gist\_stars count and the prompt\_body/gist\_description/file\_name to the latest version.  
* **Rate Limiting Mitigation:** Given the small expected scale, the 60-minute refresh interval is sufficient. To ensure stability and higher rate limits, the Docker container **must be configurable via an optional GH\_PAT (GitHub Personal Access Token) environment variable**. The backend should use this token for authenticated API calls if provided.  
* **Middleware:** Authorization middleware must be implemented to protect all /api/admin/\* endpoints using the ADMIN\_TOKEN.  
* **Gist File Selection:** The backend must parse the Gist file list and use the content of the **first file ending in .md** as the prompt body. No specific metadata or size limitation is imposed on the Shift Agent Markdown content.

### **6.2. Database (SQLite Schema)**

The database will be a single SQLite file (prompts.db) managed entirely within the Docker container.

| Table Name | Field Name | Data Type | Constraints/Notes |
| :---- | :---- | :---- | :---- |
| **prompts** | id | INTEGER | Primary Key, Auto-increment |
|  | gist\_url | TEXT | Unique Index. **Stores the canonical username/id string.** |
|  | author\_name | TEXT | Contributor's name. **Regex enforced: ^\[a-zA-Z\\s\\.\\-'\]{2,100}$** |
|  | **author\_github** | **TEXT** | **GitHub username, extracted from Gist URL (required for Gist fetching).** |
|  | author\_x | TEXT | Social handle/URL (optional). **Regex enforced: ^@?\[a-zA-Z0-9\_\]{1,15}$** |
|  | author\_linkedin | TEXT | Social handle/URL (optional). **Regex enforced: ^https?:\\/\\/(www\\.)?linkedin\\.com\\/.\*$** |
|  | author\_discord | TEXT | Social handle/URL (optional). **Regex enforced: ^\[a-z0-9\\.\_\\-\]{2,32}$** |
|  | author\_email | TEXT | Email (optional). **Regex enforced: ^\[a-zA-Z0-9\\.\_\\-+\]{1,64}@\[a-zA-Z0-9\\.\\-\]{1,64}\\.\[a-zA-Z\]{2,10}$** |
|  | tags | TEXT | Comma-separated string of tags. **Max 5 tags, each matching \[a-zA-Z\\-\_\]{1,64}.** |
|  | gist\_description | TEXT | Description pulled from GitHub |
|  | file\_name | TEXT | Name of the primary Markdown file in the Gist |
|  | prompt\_body | TEXT | Raw Markdown content of the Shift Agent |
|  | gist\_stars | INTEGER | Current star count from GitHub |
|  | is\_approved | BOOLEAN | 1 if approved, 0 if pending/rejected. |
|  | **consecutive\_sync\_failures** | **INTEGER** | **Counter for transient GitHub API failures (resets on success). Deletes on 3 failures.** |
|  | last\_checked | DATETIME | Timestamp of the last successful Gist sync. |
|  | created\_at | DATETIME | Timestamp of initial submission. |
| **settings** | key | TEXT | Primary Key (e.g., 'captcha\_enabled', 'approval\_required') |
|  | value | TEXT | Setting value (e.g., 'true', 'false') |
| **admin** | key | TEXT | Primary Key (Always 'ADMIN\_TOKEN') |
|  | token | TEXT | The current active Admin Token (SHA-256 or similar hash recommended) |
|  | created\_at | DATETIME | Timestamp of initial token creation |
|  | last\_refreshed | DATETIME | Timestamp of last token refresh |

### **6.3. Admin Token Management**

The ADMIN\_TOKEN is critical.

* **Generation:** A secure, random token must be generated upon the first run of the Docker container (or if the database is empty) and printed to the container logs.  
* **Refresh Mechanic:** An API endpoint (/api/admin/refresh\_token) will exist to refresh the token.  
  * **Authorization:** This endpoint **requires** the current ADMIN\_TOKEN in the Authorization header to execute.  
  * **Action:** It generates a new secure token, updates the admin table, and returns the new token.

## **7\. Finalized Requirements Summary**

The following decisions finalize the outstanding requirements:

| Requirement Area | Decision | Implementation Detail |
| :---- | :---- | :---- |
| **Gist URL Parsing** | Strictly enforce username/{id} format. | Backend must use regex/parsing to extract the **canonical username/id string** from the input URL. |
| **Gist File Selection** | Use the first .md file found in the Gist. | Client-side validation should check for the presence of an .md file, and the backend must strictly use the first one encountered. |
| **Tags Validation** | Max 5 tags, strict character set. | Tags must be separated by commas; each tag matches \[a-zA-Z\\-\_\]{1,64}. |
| **Email Validation** | Strict character set and length. | Email must be 5-128 characters, matching a strict email regex to enforce minimal character set. |
| **Social Handle Validation** | All social fields strictly validated. | **Author Name:** ^\[a-zA-Z\\s\\.\\-'\]{2,100}$. **X Handle:** ^@?\[a-zA-Z0-9\_\]{1,15}$. **Discord:** ^\[a-z0-9\\.\_\\-\]{2,32}$. **LinkedIn:** ^https?:\\/\\/(www\\.)?linkedin\\.com\\/.\*$ |
| **Synchronization Frequency** | Update check hourly (60 minutes). | The server-side background job will run every 60 minutes. |
| **Synchronization Failure** | Three consecutive failures threshold. | The new consecutive\_sync\_failures field tracks errors; prompt is deleted only after reaching 3\. |
| **SPA Routing** | Query parameter routing. | Frontend navigation will be based on query parameters (e.g., ?view=store). **Specific prompt views must use ?view=prompt\&gist\_ref=username/id.** |
| **Client-Side Loading** | **Real-time Gist embedding on view.** | When viewing a specific prompt, the client fetches the content via the GitHub Gist JSON API to ensure freshness. |
| **Database Init** | Flask handles setup on startup. | Flask must check for DB existence and run schema/token generation if required. |
| **GitHub Rate Limiting** | Use optional GitHub PAT. | The Docker container must accept an optional GH\_PAT environment variable to authenticate GitHub API calls and mitigate rate limits. |
| **Captcha Service** | Google reCAPTCHA (v2 or v3). | Require configuration variables for reCAPTCHA keys in the Docker environment for both client-side and server-side validation. Token transmitted via JSON payload (recaptcha\_token). |
| **Prompt Removal Notification** | No notification required. | When a prompt is automatically removed due to Gist deletion/privacy, the system will not attempt to contact the author. |
