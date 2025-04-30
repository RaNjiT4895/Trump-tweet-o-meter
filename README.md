# Trump Tweet-O-Meter™

Real-Time Social Media Sentiment Analysis

---

## 📌 Overview

**Trump Tweet-O-Meter™** is a real-time NLP-powered application that fetches recent tweets related to Donald Trump, classifies the sentiment of each tweet using VADER (Valence Aware Dictionary and sEntiment Reasoner), and visualizes public opinion through an interactive Streamlit dashboard. It is useful for tracking sentiment trends, analyzing public discourse, and detecting shifts in political sentiment.

---

## 🚀 Features

- Real-time tweet fetching using the Twitter API (via Tweepy)
- Sentiment analysis using VADER (`positive`, `neutral`, `negative`)
- Tweets stored and indexed in MongoDB
- Interactive Streamlit dashboard for:
  - Viewing tweets with sentiment labels
  - Filtering tweets by sentiment
  - Bar chart visualization of sentiment distribution
- Containerized using Docker for consistent deployment

---

## ⚙️ Requirements

- Python 3.9+
- Twitter Developer Account & Bearer Token
- MongoDB (local or Atlas)
- Docker (for containerized deployment)

---

## 🧪 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/trump-tweet-o-meter.git
cd trump-tweet-o-meter
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
TWITTER_BEARER_TOKEN=your_bearer_token_here
MONGO_URI=mongodb://localhost:27017
```

---

## ⚙️ Working

### ✅ Tweet Ingestion
- `fetch_tweets.py` uses the Twitter API to fetch live tweets about Donald Trump.

### ✅ Sentiment Analysis
- VADER assigns a sentiment score (`positive`, `neutral`, or `negative`) to each tweet.

### ✅ Storage
- Tweets and sentiment data are stored in MongoDB for easy retrieval and analysis.

### ✅ Visualization
- `app.py` or `visualize.py` runs a Streamlit dashboard that:
  - Displays tweets in real time  
  - Offers filters by sentiment  
  - Shows charts of sentiment distribution

---

## 🐳 Docker Deployment

### 1. Build the Docker Image

```bash
docker build -t trump-tweet-o-meter .
```

### 2. Run the Container

```bash
docker run -p 8501:8501 trump-tweet-o-meter
```

📍 Access the app at: [http://localhost:8501](http://localhost:8501)

---

## 🧰 Technologies Used

- **Python**
- **Tweepy** – Twitter API
- **VADER** – Sentiment Analyzer
- **MongoDB** – NoSQL Storage
- **Streamlit** – Visualization
- **Docker** – Containerization

---

## 🤝 Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Suggestions and improvements are always welcome!
