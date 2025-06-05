from src.text2sql import Text2SQL


def test_postgres():
    worker = Text2SQL(
        db_uri="postgresql+psycopg2://postgres:123456@localhost:25432/test",
        llm_uri="llm+ollama://qwen2.5:32b@localhost:11434",
        milvus_uri="http://read:123456@localhost:29530",
        collection_name="sql_references",
        embedding_uri="embedding+ollama://bge-m3@localhost:11434"
    )
    res = worker("公司的设备清单", ["assets", "users", "projects"])
    print(res, file=open("test.log", "a+"))
    assert len(res.sql) > 0


def test_mysql():
    worker = Text2SQL(
        db_uri="mysql+pymysql://root:123456@localhost:23306/test",
        llm_uri="llm+ollama://qwen2.5:32b@localhost:11434",
        milvus_uri="http://read:123456@localhost:29530",
        collection_name="sql_references",
        embedding_uri="embedding+ollama://bge-m3@localhost:11434"
    )
    res = worker("用户清单", [])
    print(res, file=open("test.log", "a+"))
    assert len(res.sql) > 0
