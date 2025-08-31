# 🌍 Travel Advisory Agentic AI

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com/) [![Streamlit](https://img.shields.io/badge/Streamlit-1.49+-FF4B4B.svg)](https://streamlit.io/) [![LangChain](https://img.shields.io/badge/LangChain-0.3%2B-yellow)](https://www.langchain.com/) [![LangGraph](https://img.shields.io/badge/LangGraph-0.6.6%2B-yellow)](https://www.langchain.com/)

An **agentic AI-powered travel advisory system** that provides personalized trip planning, real-time weather updates, cost estimations, restaurant and attraction suggestions, and currency conversions. This project combines **FastAPI**, **Streamlit**, and **LangChain-based agentic workflows** to deliver a comprehensive, interactive travel assistant.

---

## ✨ Key Features

- 🧳 **Personalized Trip Planning** – Generate day-by-day itineraries with tourist and off-beat options.
- 🍽️ **Restaurant & Activity Suggestions** – Search local restaurants, attractions, and activities.
- 🌦️ **Weather Updates** – Real-time weather data and forecasts using OpenWeatherMap.
- 💱 **Currency Conversion** – Convert travel expenses to local currencies.
- 💵 **Expense Planning** – Estimate hotel costs, daily budgets, and total trip expenses.
- ⚡ **Multi-Model LLM Support** – Plug-and-play with Groq, OpenAI, or Google GenAI.
- 🖼️ **Graph-based Agent Workflow** – Visualize agent reasoning and tool usage.
- 💻 **Interactive UI** – Streamlit-powered chat interface for seamless user experience.

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
 git clone https://github.com/iampraveens/travel-advisory-agentic-ai.git
 cd travel-advisory-agentic-ai
```

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file in the root directory and add your API keys:

```env
OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key
GEMINI_API_KEY=your_google_genai_key
GPLACES_API_KEY=your_google_places_key
OPENWEATHERMAP_API_KEY=your_openweathermap_key
EXCHANGE_RATE_API_KEY=your_exchange_rate_key
```

### 5️⃣ Start backend (FastAPI)

```bash
uvicorn main:app --reload --port 8000
```

### 6️⃣ Launch frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 💡 Usage Example

- Open the Streamlit app in your browser.
- Ask a travel-related query, e.g.:

```
Can you help me plan a 2-day trip to Dubai?
```

- The agent will:
  - Suggest detailed itineraries
  - Recommend hotels, restaurants, and activities
  - Provide weather forecasts
  - Estimate expenses and convert to AED

---

## 📂 Project Structure

```
travel-advisory-agentic-ai/
├── README.md                  # Project documentation
├── app.py                     # Streamlit frontend for the chatbot
├── LICENSE                    # MIT License
├── main.py                    # FastAPI backend for query handling
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── template.sh                # Script to generate project structure
├── agent/                     # Agentic workflow components
│   ├── __init__.py
│   └── agentic_workflow.py    # LangGraph-based agent builder
├── config/                    # Configuration files
│   ├── __init__.py
│   └── config.yaml            # LLM provider settings
├── prompts/                   # Prompt templates
│   ├── __init__.py
│   └── prompt_template.py     # System prompt for the travel agent
├── research/                  # Experimental notebooks
│   ├── experiments.ipynb      # General experiments
│   └── trials.ipynb           # LLM loading trials
├── tools/                     # Tool definitions
│   ├── __init__.py
│   ├── currency_conversion_tool.py
│   ├── expense_calculation_tool.py
│   ├── place_search_tool.py
│   └── weather_info_tool.py
└── utils/                     # Utility modules
    ├── __init__.py
    ├── config_loader.py       # YAML config loader
    ├── currency_converter.py  # Currency conversion logic
    ├── expense_calculator.py  # Expense calculation functions
    ├── model_loader.py        # LLM loader
    ├── place_info_searcher.py # Place search integrations
    └── weather_info.py        # Weather API wrappers
```

---

## 📦 Dependencies

- **FastAPI** – Backend API
- **Streamlit** – Frontend UI
- **LangChain / LangGraph** – Agentic workflows
- **Groq / OpenAI / Google GenAI** – LLM providers
- **Google Places API** – Place, restaurant, and activity search
- **OpenWeatherMap API** – Weather updates
- **ExchangeRate API** – Currency conversion

(See `requirements.txt` for full list.)

---

## 🤝 Contribution Guidelines

Contributions are welcome! To contribute:

1. **Fork the Repository**:
   Fork the project on GitHub and clone your fork locally.

2. **Create a Branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**:

   - Follow the project’s coding style and structure.
   - Add or update tests if applicable.
   - Update documentation (e.g., `README.md`, docstrings) for new features.

4. **Test Your Changes**:

   - Ensure the application runs without errors.
   - Test with a sample database to verify query generation and visualization.

5. **Submit a Pull Request**:

   - Push your branch to your fork.
   - Open a pull request with a clear description of your changes and their purpose.
   - Reference any related issues.

6. **Code Review**:
   - Respond to feedback during the review process.
   - Ensure your code adheres to the project’s standards.

Please ensure your contributions align with the project’s MIT License.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed with ❤️ by **Praveen S** ([GitHub](https://github.com/iampraveens))
