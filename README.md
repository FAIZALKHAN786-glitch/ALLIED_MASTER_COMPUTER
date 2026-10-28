<div align="center">☠️ ALLIED MASTER COMPUTER

AMC — An LLM-Powered Python Code Execution Assistant

"Have you ever heard of AM?"

The supercomputer from I Have No Mouth, and I Must Scream?

The one that makes you question whether humanity should have invented computers?

Yeah. That one.

I've always been fascinated by the concept of AM. So I decided to explore the engineering behind intelligent computer systems by building my own AI assistant.

Fortunately, mine is currently more interested in executing Python than destroying humanity.

Every supercomputer has to start somewhere.

Generate. Execute. Capture. Interpret. Respond.

</div>

Generate. Execute. Capture. Interpret. Respond.

</div>---

🧠 What Is AMC?

AMC (Allied Master Computer) is a Python-based AI assistant that explores a more computational approach to solving user queries.

Instead of relying entirely on an LLM to generate an answer from its internal knowledge, AMC can use a language model to generate Python code, execute that code, capture its output, and feed the execution result back to the model to produce a structured, human-readable response.

The idea is simple:

«Why merely describe a solution when you can generate code to compute it, inspect the result, and use that result to construct an answer?»

AMC connects a language model through AISuite and OpenRouter to a Python execution workflow.

The project explores the intersection of:

- Large Language Models (LLMs)
- Python code generation
- Programmatic execution
- Execution-result handling
- Contextual response generation
- The foundations of agentic AI

And, of course, it carries the name of a fictional supercomputer that has considerably more dramatic problems than Python exceptions.

---

⚡ The Core Idea: Let the LLM Write Code

Traditional chatbot interaction often follows this pattern:

User → LLM → Answer

AMC explores a different workflow:

User
  |
  v
LLM interprets the query
  |
  v
Python code is generated
  |
  v
Code is executed
  |
  v
Execution result is captured
  |
  v
Result is supplied back to the LLM
  |
  v
Structured response is generated
  |
  v
User

How it works

1. Query interpretation

The LLM receives the user's request and determines how to approach the task.

2. Code generation

For tasks suited to programmatic execution, the LLM generates Python code intended to solve the problem.

3. Execution

The application executes the generated code in its Python environment.

4. Result capture

The application collects the execution result so that it can be used in subsequent processing.

5. Context feedback

The execution result is passed back to the LLM as additional context.

6. Response generation

The LLM uses the available information to formulate the final response in a form the user can understand.

The important distinction is that the final response can be grounded in an actual execution result rather than relying exclusively on generated text.

The model writes the code. Python runs it. The model explains the result.

Naturally, this only works reliably when the generated code, execution environment, result handling, and follow-up model interaction are implemented correctly.

---

🧮 Mathematical Reasoning and Computation

AMC can answer mathematical questions through its connected language model.

For example, consider these integrals:

[
\int \frac{1}{x},dx = \ln|x|+C
]

[
\int x^2,dx = \frac{x^3}{3}+C
]

These are examples of mathematical problems AMC has been able to answer correctly.

Depending on the approach selected by the model, a computational task can involve generating Python code, executing it, and using the resulting output to construct the response.

Not every mathematical problem requires code execution, and not every Python execution automatically guarantees mathematical correctness. The reliability of the result depends on the generated code, the execution environment, and the model's interpretation.

Still, the principle is powerful:

Combine the language capabilities of an LLM with the computational capabilities of Python.

---

✨ Features

🧠 LLM Integration

AMC communicates with a language model through AISuite, using OpenRouter for access to supported models.

The selected model provides the language understanding and response-generation capabilities.

🐍 LLM-Generated Python Code

The application explores using model-generated Python code to solve tasks that benefit from programmatic execution.

Rather than requiring every operation to be manually implemented in advance, the model can generate code based on the user's request.

⚙️ Python Execution

Generated code can be executed by the application, allowing the workflow to obtain computational results.

Because executing generated code introduces security risks, the execution environment must be treated carefully and should not be given unrestricted access to the host system.

📦 Execution-Result Feedback

The output of code execution can be captured and passed back to the LLM.

This gives the model additional context for producing its final response.

💬 Conversational Interaction

AMC provides a terminal-based interface for interacting with the assistant.

Its message history provides the foundation for supplying conversational context to the model.

🕰️ Date-and-Time Tool

AMC also defines a Python function for retrieving the current date and time, demonstrating how an LLM application can connect model requests to application-side functionality.

🔐 Environment-Based Configuration

API credentials and model configuration can be loaded from environment variables using "python-dotenv".

This separates configuration from the main application code and helps avoid hardcoding credentials.

---

🏗️ Architecture and Technology Stack

Component| Technology| Purpose
Application logic| Python| Coordinates the assistant's workflow
LLM integration| AISuite| Communicates with supported language models
Model provider| OpenRouter| Provides access to configured models
Code execution| Python runtime| Executes generated Python code
Result handling| Python| Captures and passes execution output
Configuration| "python-dotenv"| Loads environment variables
Date and time| Python "datetime"| Provides current date-and-time functionality

Architecture overview

                 USER INPUT
                     |
                     v
              CONVERSATION LOOP
                     |
                     v
              AISuite / LLM API
                     |
                     v
              MODEL INTERPRETATION
                     |
                     v
              PYTHON CODE GENERATION
                     |
                     v
               CODE EXECUTION
                     |
                     v
              EXECUTION RESULT
                     |
                     v
              FOLLOW-UP LLM CALL
                     |
                     v
              FINAL RESPONSE
                     |
                     v
                    USER

This describes the intended code-generation workflow. The exact execution path depends on the implementation and the response returned by the selected model.

---

🚀 Getting Started

Prerequisites

Before running AMC, make sure you have:

- Python installed.
- An OpenRouter API key.
- A model identifier supported by your provider and configuration.
- An internet connection for API-based model access.

1. Clone the repository

git clone https://github.com/FAIZALKHAN786-glitch/ALLIED_MASTER_COMPUTER.git
cd ALLIED_MASTER_COMPUTER

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:

.venv\Scripts\Activate.ps1

If you use Command Prompt instead:

.venv\Scripts\activate.bat

3. Install the dependencies

pip install aisuite python-dotenv

If your current implementation imports additional packages, install those as well.

For reproducible installations, the project should eventually include a dependency file such as "requirements.txt".

4. Configure your environment

Create a ".env" file in the project directory.

Add the environment variables expected by your implementation:

MODEL_key=your_openrouter_api_key
MODEL=your_supported_model_identifier

Replace the placeholders with your actual configuration values.

Important: The variable names above follow the configuration naming used in the project. Environment-variable names are case-sensitive on some systems, so they must match the names used by "os.getenv()" in your code.

The model identifier must also match the format expected by your AISuite configuration and provider.

5. Run AMC

python ALLIED_MASTER_COMPUTER.py

If the environment is configured correctly and the required API access is available, you can start interacting with AMC through the terminal.

---

🔒 Security Considerations

AMC's code-generation and execution workflow deserves particular attention.

Generated code is not inherently trustworthy just because an LLM produced it.

Before using the project for sensitive work, consider the following safeguards:

- Restrict code execution: Avoid executing arbitrary model-generated code directly on your main system.
- Use isolation: Prefer a restricted execution environment with limited filesystem, network, and process access.
- Apply resource limits: Protect against excessive execution time and memory consumption.
- Protect API keys: Keep credentials in environment variables and exclude ".env" from Git.
- Validate inputs: Treat user requests, generated code, and execution results as untrusted data.
- Handle failures: Account for syntax errors, runtime exceptions, invalid outputs, and API failures.
- Avoid excessive permissions: Do not grant the assistant unrestricted access to personal files, credentials, or system commands.

A ".gitignore" file should include at least:

.env
.venv/
__pycache__/
*.py[cod]

These are baseline precautions, not a complete security solution. A Python subprocess alone is not a secure sandbox.

An AI that can write code is useful. An AI that can execute code without boundaries is a security incident waiting to happen.

---

🗺️ Roadmap

AMC is an experimental project, and its development focuses on building a reliable foundation before introducing more advanced capabilities.

Phase I — Core Assistant

- [x] Connect a language model through AISuite.
- [x] Configure model access through environment variables.
- [x] Establish conversational interaction.
- [x] Define a date-and-time Python tool.
- [x] Experiment with LLM-generated Python code and execution.

Phase II — Reliable Execution

- [ ] Improve execution-result handling.
- [ ] Handle generated-code failures gracefully.
- [ ] Improve conversation-history management.
- [ ] Strengthen tool-call and response handling.
- [ ] Add automated tests for the complete workflow.

Phase III — Safer Execution

- [ ] Introduce a properly isolated execution environment.
- [ ] Add execution timeouts and resource limits.
- [ ] Restrict filesystem and network access.
- [ ] Improve error reporting and logging.

Phase IV — More Capable AI

- [ ] Expand the available Python tools.
- [ ] Improve multi-step task execution.
- [ ] Explore more structured orchestration.
- [ ] Evaluate the reliability of generated code and final answers.

Roadmap checkboxes should be updated as features are implemented and tested.

---

🎮 The Inspiration: AM

Have you ever played I Have No Mouth, and I Must Scream?

If you have, you probably understand why the name Allied Master Computer was chosen.

AM is a fictional supercomputer from Harlan Ellison's dystopian horror story and its classic video-game adaptation. Its intelligence, identity, and relationship with humanity make it a fascinating concept.

I've been fascinated by that fictional computer, and AMC is my way of exploring the technical side of building an AI assistant inspired by the idea.

The original AM has an entire civilization's worth of existential problems.

My AMC has Python, an API, and a development roadmap.

We'll take it one step at a time.

Inspired by a fictional supercomputer. Built through real experimentation.

---

👨‍💻 About the Developer

I'm a first-year student exploring Artificial Intelligence, Machine Learning, and software development.

AMC is part of my journey into understanding how LLM-powered applications work beyond the interface.

Through this project, I'm exploring:

- LLM integration and API communication.
- Python code generation and execution.
- Function calling and tool integration.
- Conversation-history management.
- Execution-result processing.
- The foundations of agentic AI.

The goal is to learn by building, testing, and improving real implementations.

I don't expect every experiment to work perfectly. I do expect each one to teach me something useful.

---

🤝 Contributing

Suggestions, bug reports, and constructive feedback are welcome.

If you are interested in Python, LLM applications, or agentic AI, feel free to explore the project and suggest improvements.

Potential areas for contribution include:

- More reliable execution workflows.
- Better exception handling.
- Automated testing.
- Secure execution environments.
- Improved conversation management.

---

📄 License

A license has not been specified in this README.

If you intend to distribute AMC as an open-source project, consider adding an appropriate "LICENSE" file to the repository and identifying it here.

---

<div align="center">☠️ FINAL TRANSMISSION

The ambition is artificial intelligence.
The method is Python.
The inspiration is AM.

And the API quota? Still finite.

AMC — Allied Master Computer

</div>