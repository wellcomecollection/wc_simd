from langchain_aws import ChatBedrock
import dotenv


dotenv.load_dotenv()


def get_llm(
        model_id: str = "eu.anthropic.claude-3-7-sonnet-20250219-v1:0",
        temperature: float = 0.2) -> ChatBedrock:
    """

    Returns a ChatBedrock LLM instance with the specified model ID and parameters.

    Returns:
        ChatBedrock: An instance of the ChatBedrock LLM with the specified model ID and parameters.
    """
    # Set the model ID and parameters for the LLM

    # Claude is a good alternative to GPT-4o:
    # https://blog.promptlayer.com/big-differences-claude-3-5-vs-gpt-4o/

    llm = ChatBedrock(
        model_id=model_id,
        # model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
        # model_id="us.meta.llama3-3-70b-instruct-v1:0",
        model_kwargs=dict(temperature=temperature),
    )

    return llm
