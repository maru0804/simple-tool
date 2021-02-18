# simple-tool

## 1. pdf file marge app
 
pdfファイルを連結するアプリケーションです。
 
## Features
 
pdf連結のwebアプリ反りも圧倒的に高速！！(12個計９６ページ分のファイル連結１秒弱)
 
## Requirement
 
* PyPDF2 --1.26.0
* natsort --7.1.1

## Installation
 
```bash
pip install natsort
pip install PyPDF2
```
 
## Usage
 
simple-tool/pdf_marge/pdfフォルダに連結したいpdfファイル（連番入り）を入れる
 
```bash
git clone https://github.com/maru0804/simple-tool.git
cd simple-tool/pdf_marge
python pdf_marge.py
```
pdf_marge.pdfが作成される
