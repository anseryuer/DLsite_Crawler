import requests
import re

def get_web_text(product_id) -> str:
    """
    Extract the text of the html website of the game with the input product id.
    https://www.dlsite.com/maniax/work/=/product_id/{product_id}.html
    """
    if product_id[0:2] == "VJ":
        return requests.get(f"https://www.dlsite.com/maniax/work/=/product_id/{product_id}.html").text
    else:
        return requests.get(f"https://www.dlsite.com/pro/work/=/product_id/{product_id}.html").text


def get_game_tags(web_txt) -> list:
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

    pattern = r'work\.genre">(.*?)</a>'

    results = re.findall(pattern, web_txt)
    return results

def get_data_json(product_id) -> dict:
    """
    Get the selling data json of the game with the given product id.
    """
    if product_id[0:2] == "VJ":
        json = requests.get(f"https://www.dlsite.com/pro/product/info/ajax?product_id={product_id}").json()
    else:# RJ123456 or RJ12345678
        json = requests.get(f"https://www.dlsite.com/maniax/product/info/ajax?product_id={product_id}").json()
    key = list(json.keys())[0]
    new_json = json[key]
    new_json['product_id'] = key

    return new_json

def get_product_id(base_url:str, page_num = 1) -> list:
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
        pattern = r' data-product_id="([^"]*)"'
        result.extend(re.findall(pattern, web_text))
    for lk in result:
        processed_rsl.append(lk)
    return processed_rsl
