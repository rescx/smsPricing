from flask import Flask, render_template, flash, request, redirect, url_for, send_file, Response
from io import StringIO
import openpyxl
import csv
import pandas as pd
import ETL


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mts_file = request.files.get('mts').read().decode('windows-1251')
        redash_file = request.files.get('redash').read().decode('windows-1251')
        result_file = ETL.processFiles(mts_file, redash_file)
        resp_headers = {
            "Content-Disposition":
            "attachment;filename=test.xlsx"
        }
        return Response(result_file, mimetype="application/vnd.ms-excel", headers=resp_headers)
    return render_template('index.html')
