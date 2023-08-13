from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.nytimes.com/"
    request = get_request(url)
    titles = parse_titles(request)
    titles_text = title_list(titles)
    file_name = get_file_name()
    save_file(file_name,titles_text)

def get_request(url):
    return requests.get(url)

def parse_titles(request):
    request_html = request.text
    soup = BeautifulSoup(request_html,"html.parser")
    titles = soup.find_all("h3")
    return titles

def title_list(titles):
    return [heading.get_text() for heading in titles]

def get_file_name():
    return input("Chosoe a file name: ").strip()

def save_file(file_name, titles):
    titles_text = "\n".join(titles)
    with open(file_name + '.txt', 'w', encoding='utf-8') as file:
        file.write(titles_text)

if __name__ == "__main__":
    main()