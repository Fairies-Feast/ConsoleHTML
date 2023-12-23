# ConsoleHTML | Free to use for personal and commercial use, just give credit to Amsilla.com
# You need to install these packages: art, colorama, readchar
import art
import colorama
from readchar import readkey, key

def clear():
    print("\033[H\033[2J", end="", flush=True)

def encode(htmls): # Assuming there are spaces between attributes
  tagname = "p"
  if htmls.startswith("<!--") and htmls.endswith("-->"):
    tagname = "COMMENT"
  elif " " in htmls and "<" in htmls:
    tagname = htmls.split(" ")[0].replace("<", "")
  elif ">" in htmls:
    tagname = htmls.split(">")[0].replace("<","")
  return [tagname]
