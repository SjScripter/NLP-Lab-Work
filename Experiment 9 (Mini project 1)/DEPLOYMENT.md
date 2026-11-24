# Complete Deployment Guide for News Reel Script Synthesizer

This document explains step-by-step how to host and deploy this application to production or cloud environments.

---

## Option 1: Streamlit Community Cloud (Recommended - Free & 2 Minutes)

Streamlit Community Cloud is the standard, zero-cost, serverless hosting option for Streamlit projects.

### Steps:
1. **Push your code to GitHub**:
   - Create a new public or private repository on GitHub (e.g., `news-reel-generator`).
   - In your workspace directory, initialize git and push:
     ```bash
     git init
     git add .
     git commit -m "Initial commit of News Reel Generator"
     git branch -M main
     git remote add origin https://github.com/<your-username>/news-reel-generator.git
     git push -u origin main
     ```
2. **Deploy on Streamlit Community Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
   - Click **"New app"**.
   - Select your repository (`news-reel-generator`), branch (`main`), and set the main file path to:
     ```text
     app.py
     ```
   - Click **"Deploy!"**.
   - Streamlit will read `requirements.txt`, install dependencies, and give you a public URL (e.g., `https://news-reel-generator.streamlit.app`).

---

## Option 2: Render or Railway (PaaS - Container/Web Service)

Both **Render** and **Railway** allow free or low-cost deployment directly from GitHub.

### Using Render:
1. Push your repository to GitHub.
2. Sign in at [render.com](https://render.com) and click **New + -> Web Service**.
3. Connect your GitHub repository.
4. Set the following settings:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
5. Click **Create Web Service**.

---

## Option 3: Docker Container (Any Cloud - AWS, GCP, Azure, DigitalOcean)

If you want a portable container to run anywhere:

### 1. Create a `Dockerfile`:
```dockerfile
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. Build and run locally or in cloud:
```bash
docker build -t news-reel-app .
docker run -p 8501:8501 news-reel-app
```

---

## Option 4: Linux VPS (Ubuntu / Debian on AWS EC2, DigitalOcean Droplet, Linode)

If deploying to a virtual private server:

1. **SSH into your server and install python/pip**:
   ```bash
   sudo apt update && sudo apt install -y python3-pip python3-venv git
   ```
2. **Clone the code & setup environment**:
   ```bash
   git clone <repo-url>
   cd "experiment 9"
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Run with `systemd` (background service)**:
   Create a service file `/etc/systemd/system/newsreel.service`:
   ```ini
   [Unit]
   Description=News Reel Synthesizer App
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/experiment 9
   ExecStart=/home/ubuntu/experiment 9/venv/bin/streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
   Start and enable:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start newsreel
   sudo systemctl enable newsreel
   ```
4. **Nginx Reverse Proxy & SSL (Optional)**:
   Point port `80/443` to `http://localhost:8501` and attach a free Let's Encrypt certificate with `certbot`.
