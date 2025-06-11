import json

from tqdm import tqdm

from openai import OpenAI
from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


class QueryResponse(BaseModel):
    query: list[str]

def QueryGen():
    with open("./data/skku_notices.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    queries = []
    for id, notice in tqdm(data.items(), desc="Generating queries"):
        response = client.responses.parse(
            model="gpt-4o-mini",
            input=[
                {
                    "role": "system",
                    "content": "너는 찾고 싶은 학과 공지사항이 있는 성균관대학교 학부생이고, 학교 챗봇에 질문을 통해 그 공지사항을 찾으려고 할거야. 다음으로 너가 찾고 싶은 공지사항의 제목과 내용이 주어지면 해당 공지사항을 찾기 위해 챗봇에게 질문할 적절한 쿼리 5개를 생성해줘.",
                },
                {
                    "role": "user",
                    "content": f"제목: {notice["title"]} 내용: {notice["content"]}",
                },
            ],
            text_format=QueryResponse,
        )
        queries.append({'id': id, 'query': response.output_parsed.query})

    with open("./data/skku_notices_queries.json", "w", encoding="utf-8") as f:
        json.dump(queries, f, ensure_ascii=False, indent=4)
