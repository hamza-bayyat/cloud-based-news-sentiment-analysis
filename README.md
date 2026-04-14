# cloud-based-news-sentiment-analysis
This project is a cloud-native application designed to act as an intelligent filter for news consumption. It fetches real-time headlines, analyzes their emotional tone using Natural Language Processing (NLP), and stores the results in a cloud database for personalized user access.

🚀 FeaturesReal-time News Fetching: Integrated with NewsAPI to pull the latest headlines via HTTP requests.Sentiment Analysis: Uses NLTK’s VADER engine to categorize news into 'good', 'neutral', or 'bad' based on compound scores.Cloud Storage: Synchronizes analyzed data with Firebase Firestore for a scalable, NoSQL backend.Mood-Based Filtering: Provides a command-line interface for users to select news that matches their current emotional state.Containerized Deployment: Fully packaged with Docker for consistent performance across any system.

🛠️ Tech StackLanguage: 
Python 3.10+
NLP Library: NLTK (VADER Lexicon)
Cloud Database: Firebase Firestore
Containerization: Docker 
APIs: NewsAPI

📋 Prerequisites: Before running the application, ensure you have:
A NewsAPI Key.
A Firebase Project with a service account key saved as firebase_credentials.json in the root directory.

⚙️ Installation & Setup:
Clone the repository: git clone https://github.com/hamza-bayyat/cloud-based-news-sentiment-analysis.git
cd cloud-based-news-sentiment-analysis
Environment Setup: Add your NEWS_API_KEY to main.py and place your firebase_credentials.json in the project folder.
Local Execution: pip install -r requirements.txt
python main.py

🐳 Docker Deployment The application is containerized to handle all dependencies, including the NLTK VADER lexicon.
Build the Image: docker build -t news-sentiment-app .
Run the Container: docker run -it news-sentiment-app

📂 Project Structure
main.py: Core logic for fetching, analyzing, and filtering news.
firebase_config.py: Initializes the Firebase Admin SDK and Firestore client.
Dockerfile: Defines the environment and ensures the vader_lexicon is downloaded.
requirements.txt: Lists Python dependencies (requests, nltk, firebase-admin).

⚠️ Challenges & SolutionsAPI Stability: 
Implemented robust error handling and response validation to manage incomplete data or API downtime.
Dependency Management: Solved NLTK data requirements within the Docker environment by including a specific download command in the Dockerfile.
