from bs4 import BeautifulSoup
from urllib import request

def html_to_text(url, outfile):
    print("querying url %s" % url)
    try: 
        sources = request.urlopen(url).read().decode('utf8')
    except:
        print("Unable to query %s" % url)
        return False
    soup = BeautifulSoup(sources,"html.parser")
    for script in soup(["script", "style", 'a']):
        script.decompose()
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())    
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    f = open(outfile,"w")
    f.write(text)
    return text

html_to_text('https://books.google.com/books?id=8lGNQMUTr0gC&printsec=frontcover&dq=cosmology+history&hl=en&sa=X&ved=0ahUKEwi4ttjq1MjcAhWSyIMKHT7LA1cQ6AEIRTAF#v=onepage&q=cosmology%20history&f=false', './google-book.txt')
