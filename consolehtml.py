# ConsoleHTML | Free to use for personal and commercial use, just give credit to Amsilla.com
# You need to install these packages: art, colorama, bs4
import art
import colorama
from bs4 import BeautifulSoup

def encode(html_tag):
    soup = BeautifulSoup(html_tag, 'html.parser')
    tag = soup.find()
    tag_name = tag.name
    content = tag.text
    attributes = [f"{attr}={value}" for attr, value in tag.attrs.items()]
    return [tag_name, content, *attributes]
class Snapshot:
    def __init__(self, skeleton):
        self.data = "HTML.tag."+skeleton[0]+"!!" + skeleton[1]
