# Text2SQL
A simple implementation of Text2SQL.

## Requirements
- Python 3.12.3+
- Postgresql / Mysql
- LLM API
- *Milvus 2.5.0+*
- *Embedding API*

## Definition
### LLM URI
A db-uri-style string that provides information for calling the model API.
#### Format
```plaintext
<model_type>+<api_type>://<model>[:<model_tag>]@[<api_key>]@<ip>:<port>
```
#### Supported Model Type
- llm
- embedding
#### Supported API Type
- ollama
- openai
#### Example
llm+ollama://qwen2.5:32b@localhost:11434
### SQL References
Optional metadata stored in Milvus.
Provide some sql references for problems similar to the current problem.
#### Format
Must contain `query` and `sql` fields.
Vector field will be matched the embedding of query.


## Usage
```python
from text2sql import Text2SQL
worker = Text2SQL(
    db_uri="postgresql+psycopg2://postgres:123456@localhost:5432/test",
    llm_uri="llm+ollama://qwen2.5:32b@localhost:11434",
    milvus_uri="http://read:123456@localhost:19530",
    collection_name="sql_references",
    embedding_uri="embedding+ollama://bge-m3@localhost:11434"
)
sql = worker("公司的设备清单", ["assets", "users", "projects"]).sql
```
