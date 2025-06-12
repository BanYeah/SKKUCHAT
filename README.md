# SKKUCHAT
**챗봇 기반의 학교 공지사항 정보 제공 서비스**
<br>

기존 챗봇 기반 학교 정보 제공 서비스는 규칙 기반으로 최신 정보 반영에 한계가 있어, RAG 기술을 활용한 고도화된 챗봇 개발을 목표로 하고 있습니다. 다양한 출처에 흩어진 정보를 통합하기엔 초기 단계에서 무리가 있어, 1차적으로 학교 공지사항을 중심으로 정보를 제공하는 MVP 형태로 설계 및 구현하였습니다.
<br>
<br>
<br>

## Key Features
* 최신 학교 공지사항 정보 웹 크롤링 및 데이터 정제 자동화
* BM25 검색 엔진 기반 공지사항 검색
  * Reranking 및 유사도 임계값 설정으로 검색 결과 정제
* ChatGPT 기반 공지사항 정보 요약 및 질문 응답
<br>
<br>

## Future Work
* 공지사항 마감일 레이블링 (기한이 지난 공지 필터링)
* 대화 문맥 유지
* 일부 출처(기숙사, 소프트웨어학과 등)로 공지사항 정보 범위 확대
<br>
<br>

## Quick Start Guide
Step 1. 의존성 설치
```bash
# OCR용 패키지 설치 및 Mecab 설치
chmod +x setup.sh
./setup.sh

# 파이썬 모듈 설치
pip install -r requirements.txt
```
<br>

Step 2. ```.env```파일에 OPENAI_API_KEY 작성
```bash
OPENAI_API_KEY = ''
```
<br>

Step 3. 웹 페이지 실행
```bash
streamlit run app.py
```
<br>

> @SKKAI (Sungkyunkwan University AI Association)    
> 2025-1 Generative AI Session
