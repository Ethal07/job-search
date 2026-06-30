# Job Match AI (DWP Job Scraper + CV Matcher)

## Overview

Job Match AI is a Python-based system that automatically collects job listings from the UK Government “Find a Job” service, processes them into structured data, and uses AI to evaluate how well each role matches a candidate’s CV.  
The goal is to reduce manual job searching by ranking roles based on skill alignment, experience fit, and role suitability.

## Key Features

* Scrapes job listings from a server-rendered job board
* Extracts structured job data (title, company, location, salary, description, tags)
* Normalises and cleans raw job text into consistent records
* Stores job data in a structured format for processing
* AI-powered job matching against a candidate CV
* Generates a match score and explanation for each job
* Ranks jobs by suitability

## System Architecture

Job Site (DWP Find a Job)  
↓  
HTML Scraper  
        ↓  
Data Parser / Normaliser  
        ↓  
Job Dataset (TXT / JSON / SQLite)  
        ↓  
CV Profile Extraction  
        ↓  
AI Matching Engine  
        ↓  
Ranked Job Results  

## How It Works

### 1. Job Collection

The scraper downloads job listing pages and extracts each job card using structured HTML selectors.  
Each job includes:  
* Job title
* Employer
* Location
* Salary
* Employment type (Full time / Hybrid / etc.)
* Job description
* Application URL

### 2. Data Processing

Raw scraped data is converted into a consistent format for downstream processing.  
Jobs are:  
1. Cleaned (removal of HTML noise and whitespace)
2. Normalised (consistent salary and tag formats)
3. Deduplicated using unique job identifiers

### 3. CV Processing

The user CV is converted into structured JSON containing:
* Skills
* Experience
* Education
* Target roles
This allows efficient comparison with job requirements.

### 4. AI Matching

Each job is evaluated against the CV using an LLM. The model returns:
* Match score (0–100)
* Strengths (why it fits)
* Missing skills
* Explanation of suitability

### 5. Ranking

Jobs are sorted by:
* AI match score
* Relevance of required skills
* Salary (optional weighting)
* Recency of posting

## Example Output

Job: Corporate Finance Manager  
Company: North Kesteven District Council  
Location: Sleaford, UK  
Salary: £54,014 - £56,301  
Match Score: 87/100  
Strengths:
- Strong finance and analytical requirements align with CV
- Experience in structured environments matches internship background
Missing Skills:
- Local government finance experience
Summary:  
High relevance role with strong skill overlap in finance and data analysis.

## Tech Stack

* Python 3.13
* HTTP client: requests / httpx
* HTML parsing: selectolax
* Data storage: JSON / TXT / SQLite
* AI integration: LLM API (OpenAI or equivalent)
* Optional backend: Flask

## Project Structure

job-match-ai/  
│  
├── scraper/  
│   ├── fetch_jobs.py  
│   ├── parse_jobs.py  
│  
├── data/  
│   ├── jobs.txt / jobs.json  
│  
├── ai/  
│   ├── cv_parser.py  
│   ├── job_scorer.py  
│  
├── database/  
│   ├── jobs.db  
│  
├── main.py  
└── README.md

## Future Improvements

Replace text storage with SQLite database  
Add embeddings-based semantic job search  
Build Flask dashboard for results browsing  
Automate daily job scraping  
Add email notifications for high-match jobs  
Generate tailored CVs or cover letters per job  

## Notes

This project is designed for educational and personal use. Scraping is performed on publicly accessible job listings and should respect the website’s terms of service and rate limits.

## Author

Built as a personal project exploring:  
* Web scraping  
* Data engineering  
* AI-assisted decision systems  
* Job market analysis