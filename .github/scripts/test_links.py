"""
    Copyright 2020 - NOVA
    Script that veryfies that all links in the wiki are working
    Process Improvement Proposal by: Daniel Elias
    Author: Daniel Elias
"""

from os import listdir
from os.path import isfile, join
import re
import urllib.request
import urllib.parse
import time
import json
from os import environ

def find_md_links(md):
    """
    Returns list of links found inside the file data
    """
    md = md.replace('"', " ").replace(')', " ").replace('(', " ")
    links = re.findall(r'(https?://github.com[^\s]+)', md)
    return links

def run():
    """
        1. Gets all files in the current directory
        2. Finds all links in the file 
        3. Saves links to links dictionary (key = filename)
        4. For each link in each file:
            5. Try to open the file, if it fails it is an invalid link,
               save invalid link in wrong_links dictionary
            6. If file is opened and page is a "Create New Page" page,
               it is an invalid link and it is saved in the wrong_links dictionary
        7. Return wrong_links dictionary
    """
    onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
    links = {} # Save the links found in each file
    broken_links = {} # Save the links that are not valid in each of the files
    print("Testing links...")
    for file in onlyfiles:
        f = open(file, "r", encoding="utf8")
        md = f.read()
        md_links =  find_md_links(md)   
        if file in links.keys():
            links[file] += md_links
        else:
            links[file] = md_links

    for key in links:
        for link in links[key]:
            time.sleep(1) #Avoid GitHub detecting us a robot
            encodedUrl = urllib.parse.quote(link, safe=':/')
            try: 
                webUrl =  urllib.request.urlopen(encodedUrl)
                data = webUrl.read().decode("utf-8")
                if "Create New Page" in data:
                    if key in broken_links.keys():
                        broken_links[key].append(link)
                    else:
                        broken_links[key] = [link]
            except:
                if key in broken_links.keys():
                    broken_links[key].append(link)
                else:
                    broken_links[key] = [link]
    return broken_links

broken_links = run()

if len(broken_links) > 0:
    environ['RESPONSE'] = "Error: Some links are not working: " + json.dumps(broken_links)
    print("!!! Some links in Nova's wiki are not working.")
    for doc in broken_links:
        for broken_link in broken_links[doc]:
            print("There is a broken link in document: " + doc)
            print("\t The broken link is: " + broken_link)
    exit(-1)
else:
    print("All links in Nova's wiki are working! Thank you for the quality of your work!")
    environ['RESPONSE'] = "Success: All links are working"
    exit(0)