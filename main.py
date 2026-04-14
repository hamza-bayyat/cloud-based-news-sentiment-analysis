import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from firebase_config import db

NEWS_API_KEY = "****************************"
NEWS_API_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

def fetch_articles():
    response = requests.get(NEWS_API_URL)
    articles = []
    if response.status_code == 200:
        data = response.json()
        for i, item in enumerate(data.get('articles', [])):
            articles.append({
                'index': i,
                'title': item['title'],
                'link': item['url']
            })
    else:
        print("Error fetching news articles:", response.status_code)
    return articles

def add_sentiments(articles):
    analyzer = SentimentIntensityAnalyzer()
    for article in articles:
        score = analyzer.polarity_scores(article['title'])
        article.update({
            'sentiment': score,
            'mood': 'good' if score['compound'] >= 0.05 else 'bad' if score['compound'] <= -0.05 else 'neutral'
        })
    return articles

def save_to_firebase(articles):
    for article in articles:
        doc_ref = db.collection('articles').document(str(article['index']))
        doc_ref.set(article)

def filter_articles(articles, mood):
    return [a for a in articles if a['mood'] == mood] if mood in ['good', 'neutral', 'bad'] else articles

def display_articles(articles):
    for a in articles:
        print(f"{a['index']}. {a['title']} → {a['mood']} ({a['sentiment']['compound']})")

def show_summary(article):
    print(f"\nLink: {article['link']}")

def main():
    articles = add_sentiments(fetch_articles())
    save_to_firebase(articles)

    mood = input("Enter your mood (good, neutral, bad): ").strip().lower()
    filtered = filter_articles(articles, mood)
    print(f"\nArticles matching '{mood}':\n")
    display_articles(filtered)

    try:
        index = int(input("\nEnter article index to read: "))
        selected = next(a for a in articles if a['index'] == index)
        show_summary(selected)
    except:
        print("Invalid index.")

main()
