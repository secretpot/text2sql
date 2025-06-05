import re
from enum import Enum
from pydantic import BaseModel
from typing import Optional


class ModelType(Enum):
    LLM = "LLM"
    EMBEDDING = "EMBEDDING"


class APIType(Enum):
    OPENAI = "OPENAI"
    OLLAMA = "OLLAMA"


class AiApi(BaseModel):
    model_type: ModelType
    api_type: APIType
    api_uri: str
    model: str
    api_key: Optional[str] = ""


def parse_ai_uri(uri: str) -> AiApi:
    pattern = re.compile(
        r"(?P<model_type>[^+]+)\+"
        r"(?P<api_type>[^:]+)://"
        r"(?P<model>[^:@]+)"
        r"(?::(?P<model_tag>[^@]+))?"
        r"(?:@(?P<api_key>[^@]+))?"
        r"@(?P<ip>[^:]+):(?P<port>\d+)"
    )

    match = pattern.fullmatch(uri)
    if not match:
        expected_format = "model_type+api_type://model[:model_tag]@[api_key]@ip:port"
        raise ValueError(f"Invalid AI API string format: {uri}, expected format: {expected_format}")

    model_type = ModelType(match.group("model_type").upper())
    api_type = APIType(match.group("api_type").upper())
    model_name = match.group("model")
    model_tag = match.group("model_tag") or "latest"
    api_key = match.group("api_key") or ""
    ip = match.group("ip")
    port = match.group("port")

    api_uri = f"{ip}:{port}"
    model_full = f"{model_name}:{model_tag}" if model_tag else model_name

    return AiApi(
        model_type=model_type,
        api_type=api_type,
        api_uri=api_uri,
        model=model_full,
        api_key=api_key
    )
