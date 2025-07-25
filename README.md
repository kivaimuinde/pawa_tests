
#  AI Travel Assistant

A full-stack AI-powered travel advisory assistant that allows users to ask travel-related questions and receive intelligent, well-formatted responses using **Google Gemini**. Built using:

- **Backend**: Python + FastAPI
- **Frontend**: Next.js + TailwindCSS
- **LLM Integration**: Google Gemini (free tier)

---

## Features

- Input travel questions and get AI-generated, structured responses
- Real-time API communication with Gemini via Google API
- Modern, responsive UI with TailwindCSS
- (Optional) Query history tracking by session ID

---

##  Project Structure

```
ai-travel-assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── components/
│   ├── pages/
│   ├── styles/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

##Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-travel-assistant.git
cd ai-travel-assistant
```

---

### 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Create `.env` file (not included in repo)

Create a `.env` file inside the `backend/` directory with the following content:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_API_URL=https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent
```

Then run the server:

```bash
uvicorn app.main:app --reload --port 8000
```

---

### 3. Frontend Setup (Next.js)

```bash
cd frontend
npm install
npm run dev
```

This will start the frontend at [http://localhost:3000](http://localhost:3000)

---

## Environment Variables Template

You must create this file manually as `.env`:

```bash
# backend/.env
GEMINI_API_KEY=your_api_key_here
GEMINI_API_URL=https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent
```

---

## Deployment

You may deploy the frontend and backend separately using platforms like:

- **Frontend**: Vercel, Netlify
- **Backend**: Railway, Render, Fly.io

Make sure to set the proper environment variables during deployment.

---

## Prompts & Prompt Engineering

The backend sends the following prompt to Gemini:

```
You are an intelligent travel advisor AI. Respond in a clear, organized format.
User question: <USER_QUERY>

Structure the answer with clear headings (e.g., Visa, Passport, Travel Advisories, etc.)
```

---

## License

MIT License
