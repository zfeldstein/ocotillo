from bs4 import BeautifulSoup
from urllib import request

def html_to_text(url):
    print("querying url %s" % url)
    try: 
        sources = request.urlopen(url).read().decode('utf8')
    except:
        print("Unable to query %s" % url)
        return False
    soup = BeautifulSoup(sources,"html.parser")
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())    
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    f = open("mars_temp.txt","w")
    f.write(text)
    return text
