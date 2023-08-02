from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.nytimes.com/"
    request = get_request(url)
    titles = parse_titles(request)
    print(title_list(titles))

def get_request(url):
    return requests.get(url)

def parse_titles(request):
    request_html = request.text
    soup = BeautifulSoup(request_html,"html.parser")
    titles = soup.find_all("h3")
    return titles

def title_list(titles):
    titles_list = []
    for heading in titles:
        titles_list.append(heading.get_text())
    return titles_list

if __name__ == "__main__":
    main()