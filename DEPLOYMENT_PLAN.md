# Deployment Plan: Render

This document outlines the steps to deploy **Signature Celebrations** to Render.

## 1. Project Preparation

### Requirements
Ensure `requirements.txt` is in the root directory.
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn -k uvicorn.workers.UvicornWorker website.backend.app:app --bind 0.0.0.0:$PORT`

### Environment Variables
In the Render Dashboard, go to **Environment** and add the following:
- **`PYTHONPATH`**: `.` (This ensures the `website` module is discoverable).

## 2. Render Setup Configuration

When creating a new **Web Service** on Render, use these settings:

| Field | Value |
| :--- | :--- |
| **Name** | `SignatureCelebrations` |
| **Language** | `Python 3` |
| **Branch** | `main` |
| **Region** | `Oregon (US West)` |
| **Root Directory** | (Leave empty) |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn -k uvicorn.workers.UvicornWorker website.backend.app:app --bind 0.0.0.0:$PORT` |

## 3. Post-Deployment Verification

1. Once the build is successful, Render will provide a URL (e.g., `https://signaturecelebrations.onrender.com`).
2. Verify that all pages load correctly:
   - `/` (Home)
   - `/inflatables`
   - `/tents-equipment`
   - `/nerf-wars`
   - `/stag-and-doe`
   - `/snack-machines`
   - `/faq`
   - `/terms-of-service`
   - `/privacy-policy`
   - `/contact-us`

## 4. Troubleshooting

- **ModuleNotFoundError:** Ensure `PYTHONPATH` is set to `.` in the Render environment variables.
- **Port Errors:** Render automatically assigns a port via the `$PORT` environment variable; do not hardcode the port in your `app.py`.
- **Static Files:** The application is configured to serve static files from `website/frontend`. Ensure this folder structure is maintained in your repository.
