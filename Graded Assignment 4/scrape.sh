#!/bin/sh
# Usage:
# ./scrape.sh https://sanand0.github.io/tdsdata/crawl_html/

wget --recursive --page-requisites --convert-links $1
