#!/bin/bash
sudo apt update

# OCR용 패키지 설치
pip install pytesseract
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-kor

# Mecab-ko 설치 여부 확인
echo
read -p "Do you want to install Mecab? (y/n): " install_mecab

if [ "$install_mecab" == "y" ] || [ "$install_mecab" == "Y" ]; then
    # Mecab-ko 설치 (Ubuntu)
    cd ~
    wget https://bitbucket.org/eunjeon/mecab-ko/downloads/mecab-0.996-ko-0.9.2.tar.gz
    tar xvfz mecab-0.996-ko-0.9.2.tar.gz
    cd mecab-0.996-ko-0.9.2
    ./configure
    make
    make check
    sudo make install

    # Mecab-dic 설치 (Ubuntu)
    cd ~
    wget https://bitbucket.org/eunjeon/mecab-ko-dic/downloads/mecab-ko-dic-2.1.1-20180720.tar.gz
    tar xvfz mecab-ko-dic-2.1.1-20180720.tar.gz
    cd mecab-ko-dic-2.1.1-20180720
    ./configure
    make
    sudo make install

    # Mecab-dic 경로 문제 해결
    sudo mkdir -p /usr/local/lib/mecab/dic
    sudo ln -s /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ko-dic /usr/local/lib/mecab/dic/mecab-ko-dic
else
    echo "Skipping Mecab installation."
fi