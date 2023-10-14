import requests
import re

def get_web_text(product_id):
    """
    Extract the text of the html website of the game with the input product id.
    https://www.dlsite.com/maniax/work/=/product_id/{product_id}.html
    """
    return requests.get(f"https://www.dlsite.com/maniax/work/=/product_id/{product_id}.html").text


def get_game_tags(web_txt):
    """
    Extracts game tags from the given web page text.

    Parameters:
    web_txt (str): The web page text containing the tags.

    Returns:
    list: A list containing the extracted game tags.

    Example:
    >>> web_text = "Some web page text containing <a href='https://www.dlsite.com/maniax/fsr/=/genre/123/from/'>tag1</a> and <a href='https://www.dlsite.com/maniax/fsr/=/genre/456/from/'>tag2</a>"
    >>> get_labels(web_text)
    ['tag1', 'tag2']
    """

    pattern = r'<a href="https://www\.dlsite\.com/maniax/fsr/=/genre/\d+/from/work\.genre">(.*?)</a>'

    results = re.findall(pattern, web_txt)
    return results

def get_data_json(product_id):
    """
    Get the selling data json of the game with the given product id.
    """
    return requests.get(f"https://www.dlsite.com/maniax/product/info/ajax?product_id={product_id}").json()

def get_product_id(base_url:str, page_num = 1):
    """
    This function extracts product IDs from a DLsite search pages.
    
    Args:
    base_url (str): The base url of (a example url) of the search page. Can be any page number of the dlsite search page
    page_num (int): The number of pages to scrape. Default is 1. The function will get all the product_id with RJ123456 format in all the page urls generated from the base url from ...page/1... to ...page/{page_num}...

    Returns:
    list: A list of product IDs in the format 'RJ123456'.

    Usage:
    >>> product_ids = get_product_id(3)
    >>> print(product_ids)
    ['RJ123456', 'RJ234567', 'RJ345678', ...] # List of product IDs from the requested number of pages.
    """
    
    create_url_from_page = lambda base_url, page: re.sub(r'(/page/)\d+', r'\g<1>' + str(page), base_url)

    result = []
    processed_rsl = []
    for i in range(1,page_num+1):
        web_text = requests.get(create_url_from_page(base_url,i)).text
        pattern = r'id="_RJ\d{6}"'
        result.extend(re.findall(pattern, web_text))
    for lk in result:
        processed_rsl.append(lk[5:-1])
        #print(lk[5:-1])
    return processed_rsl
