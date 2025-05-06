from langchain_community.agent_toolkits import SparkSQLToolkit, create_spark_sql_agent
from langchain_community.utilities.spark_sql import SparkSQL
from langchain_aws import ChatBedrock
import os
import dotenv
from pyspark.sql import SparkSession
import pyspark.sql.functions as F


def test_sparksql_agent():

    dotenv.load_dotenv()
    # Set LANGSMITH_PROJECT environment variable
    os.environ['LANGSMITH_PROJECT'] = "describe_works"

    # Claude is a good alternative to GPT-4o:
    # https://blog.promptlayer.com/big-differences-claude-3-5-vs-gpt-4o/
    llm = ChatBedrock(
        model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        # model_id="us.meta.llama3-3-70b-instruct-v1:0",
        # model_id="us.meta.llama3-2-3b-instruct-v1:0",
        # model_id="us.deepseek.r1-v1:0",
        model_kwargs=dict(temperature=0.2),
        # other params...
    )

    spark = SparkSession.builder \
        .appName("test_pyspark") \
        .config("spark.driver.memory", "12g") \
        .config("spark.executor.memory", "12g") \
        .config("spark.sql.orc.enableVectorizedReader", "false") \
        .config("spark.sql.parquet.columnarReaderBatchSize", "1024") \
        .config("spark.sql.orc.columnarReaderBatchSize", "1024") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    # Create a Spark SQL connection
    # Note: You'll need to have Spark and a database set up
    spark_sql = SparkSQL(spark_session=spark, include_tables=["works"])

    from langgraph.checkpoint.memory import MemorySaver

    toolkit = SparkSQLToolkit(db=spark_sql, llm=llm)
    memory = MemorySaver()
    agent_executor_mem = create_spark_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        max_iterations=200,
        checkpointer=memory,
        config=dict(configurable=dict(thread_id="user_conversation_1"))
    )

    result = agent_executor_mem.run(
        "Write helpful documentation for the \"Items\" \"Complex Array Structure\" in works table")

    print(result)
