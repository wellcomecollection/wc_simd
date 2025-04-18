from langchain_aws import ChatBedrock
import dotenv


dotenv.load_dotenv()

llm = ChatBedrock(
    # model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    model_id="us.meta.llama3-3-70b-instruct-v1:0",
    model_kwargs=dict(temperature=0),
    # other params...
)
