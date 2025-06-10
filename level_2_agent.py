from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.url import UrlKnowledge
from agno.models.anthropic import Claude
from agno.storage.sqlite import SqliteStorage
from agno.vectordb.lancedb import LanceDb, SearchType

from dotenv import load_dotenv
import os

# Carga automáticamente las variables de .env
load_dotenv()

# Ahora puedes leer la clave como si fuera una variable de entorno
anthropic_key = os.getenv("ANTHROPIC_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

# Load Agno documentation in a knowledge base
knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/introduction.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
        # Use OpenAI for embeddings
        embedder=OpenAIEmbedder(id="text-embedding-3-small", dimensions=1536),
    ),
)

# Store agent sessions in a SQLite database
storage = SqliteStorage(table_name="agent_sessions", db_file="tmp/agent.db")

agent = Agent(
    name="Agno Assist",
    model=Claude(id="claude-3-haiku-20240307"),
    instructions=[
        "Search your knowledge before answering the question.",
        "If you find relevant information in your knowledge base, start your response with 'Based on my knowledge:' and then provide the answer.",
        "If you don't find relevant information in your knowledge base, start your response with 'I don't have specific information about this in my knowledge base. Based on my general knowledge:' and then provide your best answer.",
        "Present information clearly and concisely.",
    ],
    knowledge=knowledge,
    storage=storage,
    add_datetime_to_instructions=True,
    # Add the chat history to the messages
    add_history_to_messages=True,
    # Number of history runs
    num_history_runs=3,
    markdown=True,
)

if __name__ == "__main__":
    # Load the knowledge base, comment out after first run
    # Set recreate to True to recreate the knowledge base if needed
    agent.knowledge.load(recreate=False)
    
    # Intenta primero con una pregunta sobre Agno (que debería estar en la base de conocimiento)
    print("\n=== Pregunta sobre Agno (debe estar en la base de conocimiento) ===")
    agent.print_response("What are the components of Agno?", stream=True)
    
    # Luego intenta con una pregunta fuera de la base de conocimiento
    print("\n=== Pregunta sobre Elon Musk (no debe estar en la base de conocimiento) ===")
    agent.print_response("Who is Elon Musk?", stream=True)
    