# DLsite Crawler

A Python program for scraping information from DLsite, a popular online store for downloadable content in Japan.

## Overview

This program provides functions to extract information about specific products, including their tags and selling data. It also includes a function to extract product IDs from DLsite search pages.

## Installation

To use this program, make sure you have Python 3.x installed and the following libraries

requests
re


## Usage

The program can be used to extract various information from DLsite. Here's a quick guide to using the provided functions:

- `get_web_text(product_id)`: Extracts the text of the HTML website of the game with the input product ID.
- `get_game_tags(web_txt)`: Extracts game tags from the given web page text.
- `get_data_json(product_id)`: Retrieves the selling data JSON of the game with the given product ID.
- `get_product_id(base_url:str, page_num = 1)`: Extracts product IDs from a DLsite search page.

Make sure to import the necessary functions before using them in your own scripts.

Place the DLsite_Crawler.py file under your directory and then use `import DLsite_Crawler` to import the library

## Example

I am currently using it to make a dataset includes all the selling data and tags of all the games with a higher sales number over 1000.

So I will upload more program and data later.

## Questions

Free to ask!!!

I am a Noob in python but I will try my best!

## License

This project is licensed under the MIT License

Feel free to contribute to the project by forking and creating pull requests. If you encounter any issues, please open an issue on the GitHub repository.
