import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    request = get_request(url)
    p_tags = get_p_tags(request)
    article = generate_article(p_tags)
    print("".join(article[4:]))

def get_request(url):
    return requests.get(url)

def get_p_tags(request):
    request_html = request.text
    soup = BeautifulSoup(request_html,"html.parser")
    a_tags = soup.find_all('p')
    return a_tags

def generate_article(p_tags):
    return [element.get_text() for element in p_tags]

if __name__ == "__main__":
    main()