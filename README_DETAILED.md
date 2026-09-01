# RAG Assistant: конфигурация и API

## Архитектура

```text
Web UI / CLI
      │
      ▼
   FastAPI
      │
      ├── загрузка и очистка HTML
      ├── разбиение на фрагменты
      ├── локальные или OpenAI-эмбеддинги
      ├── поиск по косинусной близости
      └── формирование ответа
      │
      ▼
    SQLite
```

Документы, фрагменты и векторы хранятся в SQLite. Файл базы задаётся через
`SQLITE_PATH`.

## Режимы ответа

| Режим | Результат |
| --- | --- |
| `simple` | краткий ответ |
| `sources` | ответ со списком источников |
| `inline` | ссылки на источники внутри текста |
| `extractive` | выдержки без генерации LLM |

## Индексация

Создайте `links.txt` на основе `links.example.txt`. Файл содержит по одному URL
на строку; пустые строки и строки, начинающиеся с `#`, пропускаются.

```powershell
Copy-Item links.example.txt links.txt
python cli.py ingest --file links.txt
python cli.py ingest --urls https://example.com/page-1 https://example.com/page-2
```

Те же URL можно передать через web-интерфейс или `POST /ingest`.

Пример запроса:

```json
{
  "urls": ["https://example.com/page-1"]
}
```

## Ответы на вопросы

```powershell
python cli.py ask -q "Какие услуги доступны?" --mode simple
python cli.py ask -q "Какие услуги доступны?" --mode sources
python cli.py ask -q "Какие услуги доступны?" --mode inline
python cli.py ask -q "Какие услуги доступны?" --mode extractive
```

Пример `POST /ask`:

```json
{
  "question": "Какие услуги доступны?",
  "mode": "sources",
  "top_k": 6
}
```

## Переменные окружения

| Переменная | Назначение |
| --- | --- |
| `EMBEDDING_BACKEND` | `local` или `openai` |
| `LOCAL_EMBEDDING_MODEL` | модель sentence-transformers |
| `OPENAI_API_KEY` | ключ OpenAI API |
| `OPENAI_CHAT_MODEL` | модель для ответа |
| `OPENAI_EMBEDDING_MODEL` | модель эмбеддингов |
| `CHUNK_SIZE` | размер фрагмента |
| `CHUNK_OVERLAP` | перекрытие фрагментов |
| `TOP_K` | число результатов поиска |
| `MAX_CONTEXT_CHARS` | максимальный размер контекста |
| `TIMEOUT_SECONDS` | таймаут загрузки страницы |
| `SQLITE_PATH` | путь к SQLite |
| `SEED_LINKS_FILE` | файл с URL |

## Структура

```text
app/main.py         FastAPI и REST API
app/webui.py        web-интерфейс
app/ingest.py       загрузка и индексация
app/rag.py          поиск и формирование ответа
app/db.py           SQLite
app/embeddings.py   эмбеддинги
cli.py              командная строка
templates/          HTML-шаблоны
static/             CSS и JavaScript
```

## Ограничения

- качество ответа зависит от содержимого и структуры исходных страниц;
- при смене модели эмбеддингов базу необходимо переиндексировать;
- OpenAI-режим требует действующего API-ключа;
- `extractive` работает без LLM.
