from bs4 import BeautifulSoup
import sys
def update_heading(soup):
    h1_tag = soup.select_one("header.article-header h1")
    new_heading = input("Enter article title (h1): ").strip()
    if h1_tag:
        h1_tag.string = new_heading
    else:
        article_header = soup.select_one("header.article-header")
        if article_header:
            new_h1 = soup.new_tag("h1")
            new_h1.string = new_heading
            article_header.append(new_h1)
    soup = BeautifulSoup(soup.prettify(), "html.parser")  # keep indentation
    return soup

def update_cover_image(soup):
    img_tag = soup.select_one("#header-img")
    if img_tag:
        new_src = input("Enter new cover image path: ").strip()
        new_alt = input("Enter alt text for cover image: ").strip()
        if new_src:
            img_tag["src"] = new_src
            for source in img_tag.find_parent("picture").find_all("source"):
                source["srcset"] = new_src
        if new_alt:
            img_tag["alt"] = new_alt
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    return soup

def add_paragraph(soup):
    main_tag = soup.select_one("main.article")
    if main_tag:
        text = input("Enter paragraph text: ").strip()
        if text:
            p_tag = soup.new_tag("p")
            p_tag.string = text
            main_tag.append(p_tag)
    soup = BeautifulSoup(soup.prettify(), "html.parser")
    return soup

def save_html(soup, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "article.html"
    with open(filename, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Example workflow
    soup = update_heading(soup)
    soup = update_cover_image(soup)
    soup = add_paragraph(soup)

    save_html(soup, filename)
    print("Article updated and saved with proper indentation.")
