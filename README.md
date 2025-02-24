# Economic Diplomacy Portal

## 🌍 Overview
The **Economic Diplomacy Portal** is an AI-powered platform designed to provide real-time economic insights, predictive analytics, and interactive visualizations. It supports **investors, policymakers, and embassy personnel** by aggregating economic data, forecasting trends, and offering an AI chatbot for economic and visa-related inquiries.

## 🚀 Key Features
- **Data Pipeline** – Automated collection and processing of economic indicators.
- **Predictive Analytics** – AI models for **inflation** and **exchange rate forecasting**.
- **Visualization** – Integrated **Grafana dashboards** for interactive economic data analysis.
- **Intelligent Chatbot** – AI-driven chatbot answering economic and visa-related questions.
- **Secure & Scalable** – Built with **Django**, **MySQL**, and **NVIDIA AI Inference**.

## 📌 System Requirements
Before you begin, ensure you have the following installed:
- **Python 3.9+**
- **Django 3.2.25**
- **MySQL 8.0+**
- **Node.js & npm** (For Grafana installation)
- **Docker** (For running Grafana dashboards)

## 🔧 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/GeraldMajoni/economic-diplomacy-project.git
cd economic-diplomacy-project
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate    # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure MySQL Database**
Ensure MySQL is running and create a database:
```sql
CREATE DATABASE economic_diplomacy_db;
CREATE USER 'econ_user'@'localhost' IDENTIFIED BY '********';
GRANT ALL PRIVILEGES ON economic_diplomacy_db.* TO 'econ_user'@'localhost';
FLUSH PRIVILEGES;
```

### **5️⃣ Apply Migrations & Create Superuser**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Follow the prompts to create an admin user
```

### **6️⃣ Load Initial Data (Optional)**
```bash
python manage.py loaddata initial_data.json
```

### **7️⃣ Start the Django Server**
```bash
python manage.py runserver
```
Access the application at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

## 📊 Setting Up Grafana for Economic Dashboards
### **1️⃣ Install Grafana (Using Docker)**
```bash
docker run -d -p 3000:3000 --name=grafana grafana/grafana
```

### **2️⃣ Install Grafana Image Renderer**
```bash
docker run -d --name=grafana-image-renderer -p 8081:8081 grafana/grafana-image-renderer
```

### **3️⃣ Access Grafana & Set Up Dashboards**
Visit **[http://localhost:3000](http://localhost:3000)**, log in with default credentials (`admin/admin`), and configure dashboards.

## 🤖 Using the AI Chatbot
- The chatbot answers **economic** and **visa-related** queries.
- **System Rules:**
  - Neutral on **political topics**.
  - Provides **free visa information** (30 days for Africans, Commonwealth, and Francophone countries).
  - Redirects **economic policy queries** to **[Rwanda Development Board](https://rdb.rw/)**.

## 🛠 Deployment (Optional)
To deploy the project on **Heroku** or **AWS**, follow these steps:
```bash
pip install gunicorn
heroku create economic-diplomacy
heroku config:set DATABASE_URL='your_production_db_url'
git push heroku main
```

## 🎯 Contributing
We welcome contributions! To get started:
1. Fork the repo
2. Create a new branch (`feature-new-functionality`)
3. Commit changes and push to GitHub
4. Submit a pull request

## 📄 License
This project is licensed under the **MIT License**.

---
### 📌 **Project GitHub Repository:** [Economic Diplomacy Project](https://github.com/GeraldMajoni/economic-diplomacy-project)
