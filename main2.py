import requests
import json

# Replace with your News API key
api_key = "42459870cdcb4e63a6258691de1a03c5"  # <- Put your API key here!
query = "France"  # France - Searching for news about France

url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}&language=fr&pageSize=5"  # Use 'fr' for the French language

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if "articles" in data and len(data["articles"]) > 0:
        news_articles = []
        for article in data["articles"][:5]:
            news_articles.append({
                "Title": article["title"],
                "Source": article["source"]["name"],
                "Date": article["publishedAt"],
                "Description": article["description"],
                "URL": article["url"]
            })

        print("\n📰 **News about France** 🇫🇷\n")  # News about France
        for i, article in enumerate(news_articles, 1):
            print(f"🔹 {i}. {article['Title']}")
            print(f"   🏢 Source: {article['Source']}")  # Source
            print(f"   📅 Date: {article['Date']}")  # Date
            print(f"   📝 {article['Description']}")
            print(f"   🔗 Read More: {article['URL']}\n")  # Read More
    else:
        print("No articles found for this search.")
else:
    print(f"Error: {response.status_code} - {response.text}")  # Displays the error code and response text for debugging.


# --- How to obtain a News API key ---
# 1.  Go to https://newsapi.org/
# 2.  Create an account (if you don't already have one).
# 3.  Once logged in, you will find your API key on your dashboard. It is a long string of letters and numbers.
# 4.  Replace "YOUR_NEWS_API_KEY" in the code with your actual API key.

# --- English Translation of the French output ---
#   (This is what the program will display when it works correctly)

# 📰 **News about France** 🇫🇷

# 🔹 1. [Article Title]
#    🏢 Source: [News Source Name]
#    📅 Date: [Publication Date]
#    📝 [Article Description]
#    🔗 Read More: [Article URL]

# ... (and so on for up to 5 articles)