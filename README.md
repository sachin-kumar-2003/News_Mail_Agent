# News Mail Agent 

<img width="1058" height="555" alt="diagram-export-1-28-2026-10_48_10-AM" src="https://github.com/user-attachments/assets/cbc64958-b39b-44ca-898e-244fddbee991" />



https://github.com/user-attachments/assets/fdfb2c54-d377-4863-bf7f-91ef44aa67f2



# News Mail Agent 

 A lightweight full‑stack project that fetches news and sends summaries via email. The repository contains a Python backend that handles news retrieval and mail sending, and a Vite-powered frontend for UI.

 **Repository structure**

 - `backend/` : Python backend (news fetcher, mail sender, API)
	 - `main.py` — backend entrypoint / API
	 - `news.py` — news fetching logic
	 - `send_mail.py` — mail sending utilities
	 - `system_prompt.py`, `chat.py`, `check_json.py` — helper scripts
	 - `env.bat`, `run.bat`, `freeze.bat` — Windows helper scripts
	 - `requirements.txt` — Python dependencies
 - `frontend/` : Vite + React frontend
	 - `src/` — React source files (`App.jsx`, `main.jsx`, components)
	 - `package.json`, `vite.config.js` — frontend config
 - `README.md` — this file

 **Features**

 - Periodically fetches latest news items (backend)
 - Composes and sends email summaries (SMTP)
 - Simple React frontend to view/send news summaries

 **Quickstart (Windows)**

 1. Backend

		- Open a terminal and create a virtual environment (recommended):

			```powershell
			python -m venv .venv
			.\\.venv\\Scripts\\Activate.ps1
			cd backend
			pip install -r requirements.txt
			```

		- Configure environment variables. See [backend/env.bat](backend/env.bat) for an example of the variables used by the backend (SMTP credentials, recipient address, API keys, etc.). You can copy and edit that file or set variables in your environment.

		- Start the backend using the bundled script:

			```powershell
			..\\backend\\run.bat
			```

			Or run the app directly (if it uses `uvicorn`):

			```powershell
			uvicorn main:app --reload --app-dir backend
			```

 2. Frontend

		- From the repository root:

			```powershell
			cd frontend
			npm install
			npm run dev
			```

		- Open the local dev URL shown by Vite (commonly http://localhost:5173).

 **Configuration**

 - Mail and API settings: edit [backend/env.bat](backend/env.bat) or set environment variables directly. The backend reads SMTP host, port, username, password, and any news API keys from the environment.
 - Frontend settings (if any) live in `frontend/` and can be adjusted in `vite.config.js` or your environment.

 **Development notes**

 - Use `backend/freeze.bat` to generate a `requirements.txt` snapshot when adding Python packages.
 - The backend exposes endpoints for fetching news and triggering mail sends; check `backend/main.py` for routes and payloads.

 **Testing & Running**

 - Manual test: run the backend, then use the frontend UI to trigger a mail send or call the backend endpoints directly via `curl` or Postman.

 **Contributing**

 - Fork the repo, create a feature branch, and open a pull request with your changes. Include tests or manual steps to validate the change.

 **License**

 This project is available under the MIT License. See `LICENSE` if present or add one to clarify licensing.

 ---

 If you want, I can also:

 - Add a sample `.env` file with the expected environment variables.
 - Add step-by-step Windows screenshots or CI workflow for deployment.



