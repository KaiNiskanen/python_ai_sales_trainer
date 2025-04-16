# AI Sales Trainer - MVP

A simple AI-powered sales training application that helps sales professionals improve their skills through sequential reasoning, personalized feedback, and interactive conversation practice.

## Overview

The MVP version of AI Sales Trainer demonstrates core functionality of sequential reasoning and conversational AI to help sales professionals practice and improve their skills. This minimal implementation focuses on delivering essential features with an API-first architecture that supports future expansion.

## MVP Goals

- Validate the core concept of an AI sales trainer with sequential reasoning
- Deliver a working prototype with essential functionality
- Focus on backend intelligence rather than frontend polish
- Establish an API-first architecture that supports future expansion

## Must-Have Features

- Simple chat interface for interacting with the AI sales trainer
- One complete sales scenario (cold calling) implemented with sequential reasoning
- Basic user authentication (email/password)
- Conversation history storage
- Sequential feedback system that analyzes and provides structured advice

## Tech Stack

### Backend (Primary Focus)

- Python: Core programming language
- FastAPI: High-performance web framework for building APIs
- OpenAI API: Integration with GPT-4 for conversational capabilities
- supabase database: Simple storage for user data and conversations


### Frontend (Minimal Implementation)

Single-page application with:
- Login form
- Scenario selection screen (cold calling only for MVP)
- Chat interface
- Basic feedback display

Technology options:
- AI-generated React (recommended for speed)
- Any frontend capable of making API calls

## API Endpoints

- POST /api/auth/register - Create new user
- POST /api/auth/login - Authenticate user
- GET /api/scenarios - List available scenarios
- POST /api/chat - Send/receive messages with the AI trainer
- GET /api/conversations - Retrieve conversation history

## Development Plan

### Phase 1: Backend Foundation (2 weeks)
- Set up FastAPI project structure
- Implement user authentication
- Create database models
- Set up OpenAI API integration
- Implement basic conversation endpoint

### Phase 2: AI Agent Development (2 weeks)
- Design sequential reasoning process for sales training
- Implement prompt engineering for sales scenarios
- Create feedback generation system
- Test conversation flow and AI responses

### Phase 3: Frontend Implementation (1 week)
- Generate/create simple frontend with authentication
- Implement chat interface
- Connect frontend to backend API
- Test end-to-end functionality

### Phase 4: Testing & Refinement (1 week)
- User testing with 3-5 sales professionals
- Fix critical bugs and issues
- Refine AI responses based on feedback
- Document API for future development

## Success Criteria

- Users can complete a full cold calling practice session
- AI provides sequential analysis (at least 3 distinct steps)
- Feedback is specific and actionable for sales improvement
- System maintains conversation context
- API response time under 3 seconds

## Setup and Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-sales-trainer.git
cd ai-sales-trainer

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your OpenAI API key and other configuration

# Run the backend server
uvicorn app.main:app --reload
```

## Project Structure

```
ai-sales-trainer/
├── app/
│   ├── main.py            # FastAPI application entry point
│   ├── api/               # API routes
│   ├── core/              # Core settings and config
│   ├── agents/            # AI agent implementation
│   │   └── sales_agent.py # Sequential reasoning sales agent
│   ├── models/            # Data models and schemas
│   ├── db/                # Database models
│   └── services/          # Business logic
├── frontend/              # Simple frontend implementation
├── tests/                 # Backend unit tests
├── .env.example           # Environment variable template
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Technical Architecture

```
┌─────────────────┐      ┌───────────────────────┐      ┌─────────────┐
│                 │      │                       │      │             │
│  Frontend       │──────▶  FastAPI Backend      │──────▶  OpenAI API │
│  (Simple UI)    │      │  (Sequential Logic)   │      │  (GPT-4)    │
│                 │◀─────│                       │◀─────│             │
└─────────────────┘      └───────────────────────┘      └─────────────┘
                                    │
                                    │
                                    ▼
                          ┌─────────────────┐
                          │                 │
                          │  SQLite         │
                          │  Database       │
                          │                 │
                          └─────────────────┘
```

## Out of Scope for MVP

- Multiple sales scenarios beyond cold calling
- Advanced analytics and progress tracking
- Team/manager features
- Mobile app versions
- Custom scenario creation
- Integration with CRM systems 