# SKKUCHAT
> 챗봇 기반의 학교 공지사항 정보 제공 서비스
<br>

기존 챗봇 기반 학교 정보 제공 서비스는 규칙 기반으로 최신 정보 반영에 한계가 있어, RAG 기술을 활용한 고도화된 챗봇 개발을 목표로 설정하였습니다.
<br>
<br>

## Key Features
* 학교 공지사항 정보 웹 크롤링 및 데이터 정제
* BM25 검색 엔진 기반 공지사항 검색
  * Reranking 및 유사도 임계값 설정으로 검색 결과 정제
* ChatGPT 기반 공지사항 정보 요약 및 질문 응답
<br>
<br>

## Future Work
* 공지사항 마감일 레이블링 (기한이 지난 공지 필터링)
* 대화 문맥 유지
<br>
<br>

## Quick Start Guide
의존성 설치
```bash
chmod +x setup.sh
./setup.sh

pip install -r requirements.txt # Mecab 설치 확인
```
<br>

웹 페이지 실행
```bash
streamlit run streamlit.py
```
<br>
<br>

> @SKKAI (Sungkyunkwan University AI Association)    
> 2025-1 Generative AI Session