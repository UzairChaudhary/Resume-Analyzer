from flask import Flask, render_template, url_for, request, session, redirect, abort, jsonify
from werkzeug.utils import secure_filename
#import os,re
#import spacy, fitz,io
from bson.objectid import ObjectId
from pip._vendor import cachecontrol
#import pathlib
import requests
import tempfile
#from MediaWiki import get_search_results
#import shutil


def download_file(url, download_folder):
    response = requests.get(url)

    # Create the download folder if not exists
    os.makedirs(download_folder, exist_ok=True)

    # Generate a temporary filename
    _, temp_filename = tempfile.mkstemp(suffix='.pdf', dir=download_folder)

    with open(temp_filename, 'wb') as file:
        file.write(response.content)

    print("File Name: ",temp_filename)
    return temp_filename