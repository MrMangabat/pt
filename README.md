# PT Application

This repository contains the **backend** (FastAPI) and **frontend** (Nuxt 3) code for the PT (Personal Training) application.

## Prerequisites

- **Node.js** (v16 or later) and **npm** or **yarn**
- **Python** (>= 3.10)
- (Optional) **virtualenv** or built-in `venv` for Python environments

---

## Backend Setup

1. Open a terminal and navigate to the backend folder:

   ```powershell
   cd backend
   ```

2. Create and activate a virtual environment (Windows PowerShell):

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate
   ```

3. Upgrade pip and install Python dependencies (reads from `pyproject.toml`):

   ```powershell
   pip install --upgrade pip
   pip install .
   ```

4. Run the FastAPI server:

   ```powershell
   python run.py
   ```

   The API will be available at `http://localhost:8000`.

---

## Frontend Setup

1. In a new terminal, navigate to the frontend folder:

   ```bash
   cd frontend
   ```

2. Install JavaScript dependencies:

   ```bash
   npm install
   # or
   yarn install
   ```

3. Start the Nuxt development server:

   ```bash
   npm run dev
   # or
   yarn dev
   ```

   The frontend will be available at `http://localhost:3000` by default.

---

## Usage

- **Landing page:** `http://localhost:3000/landingpage`
- **Pricing & Registration:** Navigate via the UI
- **API docs:** `http://localhost:8000/docs`

---

## Project Structure

```
pt/
├── backend/        # FastAPI server (Python)
├── frontend/       # Nuxt 3 application (Vue)
└── README.md       # This file
```

---

For any issues or questions, please open an issue on this repo. Enjoy!
