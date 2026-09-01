# RAG-ассистент по материалам сайта

FastAPI-приложение, которое индексирует публичные страницы и отвечает на
вопросы с опорой на найденные фрагменты.

## Возможности

- загрузка URL из файла, формы или CLI;
- очистка HTML и разбиение текста на фрагменты;
- локальные или OpenAI-эмбеддинги;
- хранение документов и векторов в SQLite;
- поиск релевантных фрагментов;
- краткий, расширенный и extractive-режимы ответа;
- ссылки на источники в тексте;
- web-интерфейс, REST API и CLI;
- экспорт ответа в Markdown.

## Стек

Python, FastAPI, SQLite, sentence-transformers, OpenAI API, BeautifulSoup4,
httpx и Jinja2.

## Запуск

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
Copy-Item links.example.txt links.txt
uvicorn app.main:app --reload
```

- интерфейс: http://127.0.0.1:8000/ui/
- Swagger: http://127.0.0.1:8000/docs
- healthcheck: http://127.0.0.1:8000/health

По умолчанию используются локальные эмбеддинги. Для режима OpenAI укажите
`OPENAI_API_KEY` и `EMBEDDING_BACKEND=openai`.

## CLI

```powershell
python cli.py ingest --file links.txt
python cli.py ask -q "Что умеет сервис?" --mode sources
python cli.py ask -q "Что умеет сервис?" --mode inline --out-md answer.md
```

## API

| Метод | Путь | Назначение |
| --- | --- | --- |
| `GET` | `/health` | состояние приложения |
| `POST` | `/ingest` | индексация URL |
| `POST` | `/ask` | ответ на вопрос |

## Конфигурация

Основные переменные перечислены в `.env.example`. Подробности по режимам,
индексации и API приведены в [README_DETAILED.md](README_DETAILED.md).

## Документация

Исходные требования приведены в [TASK.md](TASK.md).
