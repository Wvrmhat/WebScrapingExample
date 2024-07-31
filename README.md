Web scraping example. Includes job listing site and a site for pulling weather data from a table

## What I learnt
---
Entry point, allows specific blocks of code to be run directly. Allows for testing of modules which can then be used in other scripts by importing.
>if __name__ = '__main__':
---
Shebang specifies which interpreter/application should be used to run specified files
>#!/usr/bin/env python3

>Takes python from the environment of the system

In linux it is possible to make files executable
>chmod +x main.py

>This allows it to be run without specifying python

Windows looks at file extensions, but Linux does not. Files in linux can be handled by shabang in python.

## Things to note about Web Scraping
---
Crawling is how search engines find websites, this is the predecessor to web scraping.
Web scraping is not completely illegal. Though some sites do not allow it at all.
The python library "BeautifulSoup", is a html parsing library which allows python to filter and gather information from webpages.
