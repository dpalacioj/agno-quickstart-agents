# Agno Quickstart Agents

This repository contains examples of intelligent agents built with Agno, demonstrating progressive levels of complexity and capabilities.

## Repository Structure

- **Level 1 Agent**: Basic agent setup with simple Q&A capabilities
- **Level 2 Agent**: Knowledge-enhanced agent with vector database integration
- **Level 3 Agent**: Memory-enabled agent with financial tools integration

## Models Used

The examples in this repository use the following models:

- **Claude 3 Haiku**: Powers the main agents in levels 2 and 3
- **OpenAI o3-mini**: Used for memory management in level 3 agent
- **OpenAI Embeddings**: Used for vector embeddings in level 2

## Agent Capabilities

### Level 1: Basic Agent
A simple conversational agent with no persistent memory or specialized knowledge.

### Level 2: Knowledge-Enhanced Agent
Features:
- RAG (Retrieval-Augmented Generation) architecture
- Vector database integration (LanceDB)
- Persistent conversation storage (SQLite)
- Contextual awareness

### Level 3: Memory-Enabled Agent with Tools
Features:
- Agentic memory management
- Financial data tools integration (YFinance)
- Reasoning capabilities
- Data visualization tools
- Memory persistence across conversations

## Getting Started

1. Clone this repository
2. Set up your API keys in a `.env` file (ANTHROPIC_API_KEY and OPENAI_API_KEY)
3. Install dependencies
4. Run the examples: `python level_1_agent.py`, etc.

---

Source: Official Agno documentation  
https://docs.agno.com/introduction/agents
