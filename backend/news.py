import requests
from bs4 import BeautifulSoup

def national_news():
    url = "https://www.indiatoday.in/india"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article", class_="B1S3_story__card__A_fhi")

    all_news = []

    for article in articles:
        # 1. News Type (Category)
        category_tag = article.find("h4", class_="B1S3_cat__title___NXs1")
        category = category_tag.get_text(strip=True) if category_tag else "N/A"

        # 2. News Heading (Title)
        title_tag = article.find("h3")
        title = title_tag.find("a").get_text(strip=True) if title_tag else "N/A"

        # 3. News Description (Summary)
        desc_tag = article.find("div", class_="B1S3_story__shortcont__inicf")
        description = desc_tag.find("p").get_text(strip=True) if desc_tag else "N/A"

        all_news.append({
            "type": category,
            "heading": title,
            "description": description
        })

    return all_news

def international_news():
    url = "https://www.indiatoday.in/world"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article", class_="B1S3_story__card__A_fhi")

    all_news = []

    for article in articles:
        # 1. News Type (Category)
        category_tag = article.find("h4", class_="B1S3_cat__title___NXs1")
        category = category_tag.get_text(strip=True) if category_tag else "N/A"

        # 2. News Heading (Title)
        title_tag = article.find("h3")
        title = title_tag.find("a").get_text(strip=True) if title_tag else "N/A"

        # 3. News Description (Summary)
        desc_tag = article.find("div", class_="B1S3_story__shortcont__inicf")
        description = desc_tag.find("p").get_text(strip=True) if desc_tag else "N/A"

        all_news.append({
            "type": category,
            "heading": title,
            "description": description
        })

    return all_news

print(international_news()[0])

def sports_news():
    url = "https://www.indiatoday.in/sports"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article", class_="B1S3_story__card__A_fhi")

    all_news = []

    for article in articles:
        # 1. News Type (Category)
        category_tag = article.find("h4", class_="B1S3_cat__title___NXs1")
        category = category_tag.get_text(strip=True) if category_tag else "N/A"

        # 2. News Heading (Title)
        title_tag = article.find("h3")
        title = title_tag.find("a").get_text(strip=True) if title_tag else "N/A"

        # 3. News Description (Summary)
        desc_tag = article.find("div", class_="B1S3_story__shortcont__inicf")
        description = desc_tag.find("p").get_text(strip=True) if desc_tag else "N/A"

        all_news.append({
            "type": category,
            "heading": title,
            "description": description
        })

    return all_news

# print(sports_news()[5])

def technology_news():
    url = "https://www.indiatoday.in/technology"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article", class_="B1S3_story__card__A_fhi")

    all_news = []

    for article in articles:
        # 1. News Type (Category)
        category_tag = article.find("h4", class_="B1S3_cat__title___NXs1")
        category = category_tag.get_text(strip=True) if category_tag else "N/A"

        # 2. News Heading (Title)
        title_tag = article.find("h3")
        title = title_tag.find("a").get_text(strip=True) if title_tag else "N/A"

        # 3. News Description (Summary)
        desc_tag = article.find("div", class_="B1S3_story__shortcont__inicf")
        description = desc_tag.find("p").get_text(strip=True) if desc_tag else "N/A"

        all_news.append({
            "type": category,
            "heading": title,
            "description": description
        })

    return all_news
# print(technology_news()[0])