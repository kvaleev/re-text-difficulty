---
project: elli-po-buddy
repository: tkhongsap/elli-po-buddy
license: Unknown
source_file: full-prd.md
source_url: https://github.com/tkhongsap/elli-po-buddy/blob/39917d2273c1e799d768557db891a4419770d21f/full-prd.md
downloaded_at: 2025-12-05T10:46:14.313278+00:00
consensus_grade_level: 9.4
headings_per_sentence: 0.04
lists_per_sentence: 0.36
smao_sentences_pct: 0.0
vague_words_per_sentence: 0.08
anaphora_per_sentence: 0.04
sentence_cv: 1.062
cpre_terms_per_sentence: 0.17
---
# Personal Website (Blog + Portfolio) — Product Requirements Document

Version: 1.0  
Author: Product / Owner  
Target MVP delivery: 2–4 weeks

---

## 1. Introduction / Overview

This project delivers a personal website that functions as a professional personal brand and résumé aimed at attracting employers and clients. It combines a content-first blog and a portfolio section with a built‑in admin CMS for easy content management. The website will be mobile‑first and minimalist, optimized for fast load times and clear presentation of skills, experience, and case studies.

Goal: Ship an MVP within 2–4 weeks that enables the owner to publish and update pages, blog posts, and portfolio projects, and to receive contact inquiries from prospective employers or clients.

---

## 2. Goals (Specific, Measurable)

Primary goals
1. Present a clear professional résumé and portfolio that converts visitors to contacts:
   - Target: generate at least 2 qualified contact inquiries per month within 3 months of launch.
2. Fast, mobile-first user experience:
   - Target: mobile Lighthouse performance score ≥ 90; First Contentful Paint (FCP) < 1.5s on 3G emulation.
3. Quick content management for the owner:
   - Target: owner can create, preview and publish a new blog post in ≤ 10 minutes using the admin UI.

Secondary goals
4. Good SEO and discoverability:
   - Target: achieve organic search traffic growth of 10–20% month-over-month for the first three months.
5. Low maintenance and scalable hosting:
   - Target: site deploys via CI and has automated backups of content/media.

---

## 3. User Stories

Primary user types:
- Site Owner (Admin / Content editor)
- Visitor (Employer / Client / Recruiter / General reader)

User stories

1. As the Site Owner, I want to log into an admin UI so I can create, edit, publish and delete content without using code.
2. As the Site Owner, I want to upload and manage media (images, PDF resume) so I can include visuals and a downloadable resume in projects and pages.
3. As the Site Owner, I want to preview content (posts/pages/projects) on mobile and desktop before publishing so I know how content will appear to visitors.
4. As the Site Owner, I want to save drafts and unpublish content so I can work iteratively and control what is public.
5. As a Visitor (employer/client), I want to read an “About / Résumé” page showing top skills, experience and a downloadable resume so I can quickly evaluate fit.
6. As a Visitor, I want to browse portfolio projects with short summaries and links to case studies so I can understand the owner’s work and outcomes.
7. As a Visitor, I want to read blog posts with tags and search/filter by tag so I can find relevant content about topics I care about.
8. As a Visitor, I want a simple contact form that sends an email or stores inquiries so I can reach out quickly.
9. As a Visitor on mobile, I want fast page loads and a clean layout so I can evaluate the site on my phone.

Optional/low-priority
10. As a Visitor, I want an RSS feed for the blog so I can subscribe via a feed reader.

---

## 4. Functional Requirements

Implement the following functional requirements. Each item is specific and testable.

1. Public Pages
   1.1. Home page (hero with short pitch, primary CTA to contact/resume, latest 3 blog posts, featured portfolio items).  
   1.2. About / Résumé page with sections for summary, skills, timeline/experience, education, and a link to download a PDF resume.  
   1.3. Blog list page with pagination (10 posts per page) and a grid/list view optimized for mobile.  
   1.4. Single blog post page showing title, date, author (owner), tags, and content. SEO meta tags for title, description and OG tags.  
   1.5. Portfolio list page showing project tiles (thumbnail, short summary, tags).  
   1.6. Project detail page (case study) containing: title, role, problem, solution, outcome (metrics if available), images/media gallery, and optional external links.  
   1.7. Contact page with contact form and alternative contact options (email link, LinkedIn, GitHub).

2. Built‑in Admin CMS / Admin UI
   2.1. Secure admin login (username/password) with session-based authentication. Admin account only (no public signups).  
   2.2. Dashboard showing content summary: number of published posts/projects/pages, recent activity, drafts.  
   2.3. Content editor for pages, posts, and projects with:
        - Title, slug (auto-generated but editable), publish status (draft/published), publish date (for scheduling — optional if time permits), tags, excerpt, and main content body.  
        - Content body supports Markdown with basic WYSIWYG toolbar (bold, italic, headings, links, lists, images, code blocks).  
   2.4. Media manager: upload images and PDF files, list existing media, delete media, and copy media URLs. Automatically generate optimized image sizes for responsive display.  
   2.5. Preview mode: preview the content as it will render on mobile and desktop before publishing.  
   2.6. CRUD (create/read/update/delete) for blog posts, pages, and portfolio projects. Edits to published content reflect immediately.  
   2.7. Basic input validation and sanitization to prevent XSS (server-side sanitization for any HTML).  
   2.8. Admin actions are audit‑logged (who edited what and when) for basic traceability.

3. Content Model / Data
   3.1. Unified content schema stored in a simple database (e.g., SQLite / PostgreSQL) or file-based storage if chosen (e.g., markdown + front-matter) — must support search and tag queries.  
   3.2. Tags taxonomy for posts and projects; tag pages listing content for a tag.  
   3.3. Slug rules: lowercase, hyphen-separated, max 80 chars, unique per content type.

4. Contact Form & Inquiries
   4.1. Contact form fields: name (required), email (required, validated), subject (optional), message (required), optional CV upload (PDF).  
   4.2. Submissions are sent to a configurable email address and stored in the database for retrieval in admin.  
   4.3. Basic spam protection: honeypot field and server-side rate limiting (e.g., max 5 submissions per IP per hour). CAPTCHAs are out of scope for initial MVP but can be added later.

5. Site Performance, SEO, and Accessibility
   5.1. Pages should be optimized for mobile-first performance: critical CSS inlined, images optimized and served with srcset, critical resources minimized.  
   5.2. Generate sitemap.xml and robots.txt.  
   5.3. Generate RSS feed for blog (optional but recommended).  
   5.4. Basic accessibility: semantic HTML, appropriate ARIA where needed, color contrast compliant with WCAG AA for body text.

6. Hosting, Build & Deploy
   6.1. Site must be deployable via a CI pipeline (Git-based deployment). Provide one-click deploy instructions for a target host (e.g., Vercel/Netlify or traditional Node host).  
   6.2. Environment variables for sensitive config (SMTP credentials, admin password, analytics keys).  
   6.3. Backup of database/media at least once per day or on each content update (depending on hosting).

7. Analytics & Tracking (privacy-aware)
   7.1. Integrate simple site analytics (e.g., Google Analytics or Plausible) configurable via environment variable. Do not hardcode any tracking ID.  
   7.2. If GA is enabled, add consent banner (simple opt-in) for GDPR compliance is desirable (optional for MVP if timeline constrained).

8. Security
   8.1. All admin routes behind authentication; password stored hashed (bcrypt or similar).  
   8.2. All inputs validated and sanitized; file uploads restricted to allowed types (jpg/png/webp/pdf) and size limit (e.g., 5MB).  
   8.3. Serve site over HTTPS only.

9. Optional (if time allows)
   9.1. Dark mode toggle (simple theme switching).  
   9.2. Post scheduling (publish at future date/time).  
   9.3. Social sharing buttons on posts and projects.

Acceptance criteria for MVP:
- Public site has home, about/resume, blog list, post, portfolio list, project detail, and contact pages functioning.
- Owner can sign in to admin, create/edit/publish a blog post and a project, upload images, preview, and publish.
- Contact form sends emails and stores submissions.
- Site loads on mobile within target performance metrics (Lighthouse ≥ 90 if practical).

---

## 5. Non-Goals (Out of Scope)

- Multi-user roles and permissions beyond a single admin account (no role-based access control).
- Full-featured commenting system (third-party integrations like Disqus can be added later).
- E-commerce, payments, or account registrations for visitors.
- Enterprise-level analytics and A/B testing.
- Advanced CMS features: rollback history beyond simple audit logs, collaborative editing.
- Multi-language / localization (single language only for MVP).
- Complex scheduling, workflows, or editorial approvals.
- Serverless functions outside those required for the admin API and contact form.

---

## 6. Design Considerations

High-level design rules:
- Mobile-first, minimalist visual language: generous whitespace, readable type scale, neutral color palette with one accent color.
- Simple top navigation: sticky header with logo/name, nav links (Home, About, Blog, Work, Contact). On small screens use a hamburger menu.
- Hero section on home: one-sentence value proposition, CTA buttons: "Contact" and "View Résumé".
- Card design for blog posts and projects: thumbnail, title, short excerpt, tags, read more.
- Typography: web-safe or variable font (e.g., Inter or system UI), font size scale for accessibility, line-height 1.5 for body.
- Images: responsive aspect ratios, lazy-loaded outside viewport.
- Use consistent component styles for buttons, forms, code blocks in posts, and block quotes.
- Provide links to mockups / wireframes (replace with actual link): [Design Wireframes and Style Guide] — to be attached by designer. If no designer, use clean baseline: single-column content on mobile, two-column on wide screens.

UI Requirements for Admin:
- Straightforward form layout with autosave (optional) and explicit Save/Publish buttons.
- Media manager modal accessible from editors to insert images.
- Preview should reflect final page layout and be responsive.
- Admin UI uses same minimalist styling as public site (no heavy framework needed).

Accessibility:
- Keyboard navigable, focus outlines visible, form labels associated with inputs, alt text required for uploaded images.

---

## 7. Technical Considerations

Architecture options (choose one based on team familiarity and hosting):
- Option A (recommended for rapid MVP): Next.js (React) with API routes + SQLite (or PostgreSQL) for content storage, deployed to Vercel. Admin UI implemented as part of the same app (serverless APIs). Pros: fast dev, SSR/SSG benefits, image optimization built-in.
- Option B: Static site generator (Gatsby/Hugo) with a lightweight admin that commits markdown/front-matter to Git (Netlify CMS). Pros: very fast pages; Cons: admin requires Git access or third-party provider; potentially longer setup for non-developers.
- Option C: Small Node/Express app with a simple admin panel and storage in SQLite for quickest server-side dynamic CMS.

Key technical details:
- Authentication: simple username/password with sessions (JWT server-side sessions acceptable). No OAuth required for MVP.
- Media storage: store locally (for small scale) or S3-compatible bucket. Use image processing to create responsive sizes (sharp or built-in Next/Image optimization).
- Database: SQLite acceptable for MVP; migrate to PostgreSQL if scaling expected.
- Email: use transactional email provider (SendGrid, Mailgun) configured via env variable.
- CI/CD: GitHub Actions or built-in Vercel deploy hooks.
- Backups: DB dump + media snapshot to S3 or cloud storage after each publish or daily cron.
- Logging/Monitoring: basic server logs and alerts on deployment failures.
- Rate limits and security headers (CSP, HSTS) added at hosting layer.

Performance tools:
- Use image lazy-loading, gzip/Brotli compression, and HTTP caching headers.
- Avoid heavy client-side JS; prefer server rendering or static render for public pages.

Privacy & Compliance:
- If GA used, include consent options for EU visitors. Ensure contact form storage retains minimal PII and include privacy policy page if emails are collected.

---

## 8. Success Metrics

Primary metrics (quantitative)
- Contact inquiries: target 2+ qualified leads per month within 3 months.
- Site speed: mobile Lighthouse performance score ≥ 90 (or FCP < 1.5s).  
- Content velocity: owner can publish a complete blog post in ≤ 10 minutes via admin UI.

Secondary metrics
- Organic traffic growth: +10–20% month-over-month for first 3 months.
- Bounce rate (site-wide): target < 60% within 3 months.
- Time on page for portfolio/project pages: average ≥ 90 seconds (indicates engagement).
- Uptime: 99.9% availability.

Operational metrics
- Number of CMS-related bugs reported after launch: ≤ 3 high/critical in first month.
- Mean time to deploy a content update: ≤ 5 minutes (publish -> public).

Notes on measurement:
- Use configured analytics (Google Analytics or Plausible) to measure traffic, bounce rate, time on page, and event tracking (contact form submissions).
- Track admin-side metrics with simple logs: publish times, average create/edit durations (manual measurement via checklist or admin logs).

---

## 9. Open Questions

1. Preferred technology stack: do you prefer Next.js/React, a static site + Netlify CMS approach, or a simple Node/Express admin-backed app?
2. Authentication method: single password-based admin account vs. OAuth (GitHub/Google) for the owner?
3. Hosting preference and budget (Vercel/Netlify/AWS/other)? This affects image storage and backup approach.
4. Domain and email: do you already own a domain and an email (for contact forwarding)? Which email provider to use for transactional emails?
5. Branding assets: preferred color palette, fonts, and any logo or hero image? If not provided, do we use a default minimalist style?
6. Resume format: will you upload a final PDF resume, or do you want the site to generate a resume page from structured data (and export PDF)?
7. Content frequency: how often will you publish blog posts or add projects? This affects how much editorial UX is prioritized.
8. Do you want social sharing meta defaults or custom social descriptions per post/project?
9. Analytics: do you prefer Google Analytics, Plausible, or no tracking initially?
10. Any legal requirements: privacy policy, cookie consent, or GDPR-specific wording required at launch?

---

## MVP Timeline (2–4 weeks) — Suggested Plan

Week 0 (planning, day 1–2)
- Finalize stack choice and hosting provider.
- Prepare domain, email, and analytics selection.
- Create wireframes for key pages and admin UI.

Week 1 (core build)
- Implement public routes and templates: Home, About, Blog list, Post, Work list, Project detail, Contact.
- Implement content schema and DB (or file-based storage).

Week 2 (admin + media + contact)
- Build admin authentication and CRUD editor for posts/projects/pages.
- Build media manager and image processing.
- Implement contact form, email sending, and storage.

Week 3 (polish, SEO, performance)
- Implement previews, SEO meta tags, sitemap, RSS.
- Run performance and accessibility optimizations.
- Implement backups, CI/CD.

Week 4 (QA + launch)
- QA, fix critical bugs, do usability testing with owner, finalize copy and images.
- Deploy to production, configure DNS, and monitor first 72 hours.
- Collect first analytics baseline.

If timeline needs compression, reduce optional features (preview autosave, RSS, dark mode) and prioritize core content and contact flow.

---

If you want, I can:
- Propose a recommended tech stack with file structure and example content schema, or
- Draft user flows and admin screen wireframes, or
- Produce a prioritized backlog (Jira/Trello-friendly) of tasks for a 2-week sprint.

Which follow-up would you like next?