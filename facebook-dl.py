#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import requests
import urllib.request
import random
import argparse

good = "\033[92m✔\033[0m"
yeah = "\U0001f919"

# This magic spell lets me erase the current line. 
# I can use this to show for example "Downloading..."
# and then "Downloaded" on the line where 
# "Downloading..." was.  
ERASE_LINE = '\x1b[2K'


# This extracts the video url
def extract_url(html, quality):
    # Standard Definition video 
    if quality == "sd":
        # if not found skip
        url = '' if re.search('sd_src:"(.+?)"', html) is None else re.search('sd_src:"(.+?)"', html)[0]
    else:
        # High Definition video
        url = re.search('hd_src:"(.+?)"', html)
        if url is None:
            # not found, retrieving from sd quality
            url = extract_url(html, "sd")
        else:
            url = url[0]

    # cleaning the url
    url = url.replace('hd_src:"', '')
    url = url.replace('sd_src:"', '')
    url = url.replace('"', "")

    return url


# extract video name
def video_name(file_url):
    mp4_value = ""
    for el in file_url.split("/"):
        if ".mp4" in el:
            mp4_value = el
            break

    if mp4_value != '':
        mp4_value = mp4_value.split(".mp4")[0]

    # if not found generates a random number that will be the file name
    name = mp4_value if mp4_value != "" else str(random.random())[3:12]

    return name


# download a list of video
def download_video_list(url_list, resolution):
    for idx, el in enumerate(url_list):

        info = str(idx + 1) + "] Video: "
        if el in (None, ''):
            print(info + "Not valid" + el)
            continue

        print(info + el)

        inner_url = requests.get(el)
        download_video(inner_url.text, resolution)


def download_video(url, resolution):
    file_url = extract_url(url, resolution)

    if file_url == '':
        print("Skipped video, empty url")
        return

    file_name = "fb_videos/" + video_name(file_url) + ".mp4"
    print("Downloading video...", end='\r', flush=True)

    # Downloads the video
    urllib.request.urlretrieve(file_url, file_name)
    sys.stdout.write(ERASE_LINE)
    print(good, "Video downloaded:", file_name)


def main():
    parser = argparse.ArgumentParser(description="Download videos from facebook from your terminal")

    parser.add_argument('url', action="store")
    parser.add_argument('resolution', action="store", nargs="?")

    args = parser.parse_args()

    print("Fetching source code...", end="\r", flush=True)
    r = requests.get(args.url)
    sys.stdout.write(ERASE_LINE)
    print(good, "Fetched source code")

    url_list = args.url.split(",")
    print("\n" + str(len(url_list)) + " videos found")
    if len(url_list) > 1:
        download_video_list(url_list, args.resolution)
    else:
        download_video(r.text, args.resolution)

    print(yeah, "All video have been downloaded", yeah)


if __name__ == "__main__":
    main()
