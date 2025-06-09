from dotenv import load_dotenv
import os

# Carga automáticamente las variables de .env
load_dotenv()

# Ahora puedes leer la clave como si fuera una variable de entorno
anthropic_key = os.getenv("ANTHROPIC_API_KEY")


from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.yfinance import YFinanceTools
# from agno.models.ollama import Ollama

agent = Agent(
    model=Claude(id="claude-sonnet-4-20250514"),
    tools=[YFinanceTools(stock_price=True)],
    instructions="Use tables to display data. Don't include any other text.",
    markdown=True,
)

# agent = Agent(
#     model=Ollama(id="llama3.2:latest"),
#     tools=[YFinanceTools(stock_price=True)],
#     instructions="Use tables to display data. Don't include any other text. Always return the current value of the stock price.",
#     markdown=True,
# )


agent.print_response("What is the stock price of Apple?", stream=True)
