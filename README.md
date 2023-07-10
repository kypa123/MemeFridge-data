# MemeFridge-data
밈장고 프로젝트의 컨텐츠를 웹 크롤링(나무위키), LLM chat(Bard, ChatGPT)에서 받아옵니다.

현재 ChatGPT에서 데이터를 받아오는 기능만 구현되어 있습니다.

받아온 컨텐츠의 중복검사 후 데이터베이스에 저장하며, FastAPI를 통한 api를 제공합니다.
