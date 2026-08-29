from typing import List, Literal
from pydantic import Field, AnyHttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # OpenAI
    openai_api_key: str | None = Field(None, alias="OPENAI_API_KEY")
    openai_chat_model: str = Field("gpt-4o", alias="OPENAI_CHAT_MODEL")
    openai_embedding_model: str = Field("text-embedding-3-large", alias="OPENAI_EMBEDDING_MODEL")

    # Embeddings backend
    embedding_backend: Literal["openai", "local"] = Field("local", alias="EMBEDDING_BACKEND")
    local_embedding_model: str = Field(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
        alias="LOCAL_EMBEDDING_MODEL",
    )

    # RAG / crawling
    user_agent: str = Field("Portfolio-RAG-Bot/1.0 (+https://example.org)", alias="USER_AGENT")
    chunk_size: int = Field(400, alias="CHUNK_SIZE")
    chunk_overlap: int = Field(80, alias="CHUNK_OVERLAP")
    top_k: int = Field(6, alias="TOP_K")
    max_context_chars: int = Field(12000, alias="MAX_CONTEXT_CHARS")
    timeout_seconds: int = Field(30, alias="TIMEOUT_SECONDS")

    # DB
    sqlite_path: str = Field("rag.db", alias="SQLITE_PATH")

    # Links
    seed_links_file: str | None = Field(None, alias="SEED_LINKS_FILE")

    # Optional seed URLs are supplied through SEED_LINKS_FILE.
    seed_links: List[AnyHttpUrl] = []


settings = Settings()
