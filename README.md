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

## 2. take good picture app
 
有名人と似た瞬間の画像を保存するカメラアプリです。
 
## Features
 
自分の好きな俳優と似た瞬間のフレームを保存する
 
## Requirement
 
* python --3.7 
* opencv --3.4.2
* numpy --1.18.1
* pillow --8.0.1

## Installation
 
```bash
pip install natsort
pip install PyPDF2
```
 
## Usage
 
pythonファイルと同じ階層にcomp_img,save_imgの二つのフォルダーを作成します。

comp_imgに比較したい有名人の顔画像を４枚入れます。（顔のみで、正方形の画像が好ましい）

Pythonプログラムを実行し、顔を動かしてみましょう。
 
```bash
git clone https://github.com/maru0804/simple-tool.git
cd simple-tool/take_good_pic
mkdir comp_img
mkdir save_img
python cap_scr.py
```
（注意）類似度が高いと判定する閾値は１４８としています。適宜調節してみてください。

