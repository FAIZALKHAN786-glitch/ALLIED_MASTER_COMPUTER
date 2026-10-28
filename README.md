🤖 AMC — Allied Master Computer

«Inspired by a fictional computer. Built with Python, curiosity, and free-tier API access.»

What happens when you grow up fascinated by AM (Allied Mastercomputer) from the 1995 video game I Have No Mouth, and I Must Scream and decide to build your own AI assistant?

You get AMC — a personal AI assistant project exploring the foundations of conversational AI and tool calling.

Don't worry. This one is still learning Python. 💀

---

🎯 About the Project

AMC (Allied Master Computer) is an experimental, Python-based personal AI assistant built to explore how large language models can interact with Python functions.

The project uses AISuite to communicate with language models through OpenRouter, with the goal of developing a conversational assistant that can use tools to perform specific tasks.

This project is a hands-on learning journey into LLM integration, API configuration, conversation management, and agentic AI concepts.

🛠️ Tech Stack

Technology| Purpose
Python| Core programming language
AISuite| Interface for communicating with language models
OpenRouter| Access to supported language models
python-dotenv| Loading configuration from environment variables
JSON| Parsing structured tool arguments

✨ Current Development Goals

- [x] Connect to an LLM through AISuite and OpenRouter.
- [x] Configure API credentials using environment variables.
- [x] Create an initial Python tool for retrieving the current date and time.
- [x] Define a tool schema for function calling.
- [ ] Build reliable multi-turn conversations.
- [ ] Complete and test the tool-execution cycle.
- [ ] Add more useful Python tools.
- [ ] Improve error handling and API-limit management.
- [ ] Add documentation and automated tests.

These checkboxes reflect the intended project milestones. Update them as features are implemented and tested.

⚙️ How It Works

AMC follows a simple LLM-and-tools architecture:

1. User input: The user enters a message in the terminal.
2. Model request: AMC sends the conversation history and available tool definitions to the language model.
3. Tool selection: When supported and appropriate, the model can request a tool.
4. Python execution: The application identifies the requested function and executes it.
5. Tool response: The function's result is returned to the model.
6. Assistant response: The model uses the result to formulate a reply.

The application—not the language model itself—executes the Python function.

🚀 Getting Started

Prerequisites

- Python 3.10 or a compatible version supported by your installed dependencies.
- An OpenRouter API key.
- A model available to your account that supports the features you intend to use.

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY

Replace "YOUR_USERNAME" and "YOUR_REPOSITORY" with your actual GitHub details.

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\Activate.ps1

3. Install dependencies

pip install aisuite python-dotenv

Install any additional dependencies required by the project.

4. Configure environment variables

Create a local environment file outside version control, or configure the variables in your operating system.

Example environment configuration:

MODEL_key=your_openrouter_api_key
MODEL=your_supported_model_identifier

The variable names must match those used by your Python code.

Security note: Never commit API keys or real environment files to GitHub. Keep ".env" files out of version control and rotate any key that has been exposed.

5. Run AMC

Run the Python entry-point file used by your repository:

python your_script.py

Replace "your_script.py" with the actual filename.

🧠 What I'm Learning

Building AMC is helping me explore:

- Connecting Python applications to large language models.
- Working with API providers and environment-based configuration.
- Managing conversational message history.
- Understanding tool schemas and function calling.
- Connecting model-generated tool requests to Python functions.
- Handling API errors and rate limits.
- Developing the foundations needed for more advanced agentic AI systems.

🗺️ Roadmap

Phase 1 — Core Assistant

- Basic conversational interaction.
- Model configuration.
- Initial Python tool integration.

Phase 2 — Reliable Tool Calling

- Correctly preserve tool-call messages.
- Match tool responses to their corresponding calls.
- Handle invalid arguments and execution failures.
- Test complete tool-calling conversations.

Phase 3 — Expanded Capabilities

- Calculator and other useful tools.
- Better conversation controls.
- Improved error handling.
- Automated testing.

Phase 4 — Agentic Workflows

- Explore multi-step task execution.
- Introduce controlled orchestration.
- Evaluate reliability and tool-selection accuracy.

🎮 The Inspiration

The name AMC is a nod to AM (Allied Mastercomputer) from I Have No Mouth, and I Must Scream.

The original fictional computer is a terrifying example of artificial intelligence.

My version is an experiment in learning how to build AI applications.

The ambition is to learn. The budget is minimal. The API quota is a boss fight.

⚠️ Project Status

AMC is an ongoing personal learning project.

Features are being developed and tested incrementally. It should not be considered a production-ready autonomous agent.

🤝 Contributions and Feedback

Suggestions, feedback, and ideas for improving the project are welcome.

If you're also learning Python, LLM integration, or agentic AI, feel free to explore the code and follow along with the development.

📜 License

No license has been specified yet. Please check the repository for licensing information before reusing or redistributing the code.

---

Built with Python, curiosity, and the occasional debugging session. 🐍