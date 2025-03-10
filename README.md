# InsightBot: University Recommendation System for International Students

InsightBot (Comprehensive Master's Program Assistant for Student Success) is an intelligent chatbot that assists international students in selecting the right university and timing their studies in the United States. The system provides tailored recommendations based on factors such as field of study, cost of living, weather preferences, job market outlook, and university strengths for specific courses.

![InsightBot Logo](data/compass_logo_wide.png)

## 🎯 Project Overview

InsightBot helps international students make informed decisions through:

- Personalized university recommendations
- Cost of living analysis for different states 
- Weather and climate insights
- Job market trend analysis for various fields
- Scholarship identification from universities and external sources

## 🚀 Features

### User-Friendly Web Interface
- Interactive web application built with Streamlit
- Intuitive UI with easy-to-use filters and preferences
- Clear visualization of recommendations and insights

### Personalized Recommendations
- University suggestions based on field of study, budget, location, and weather preferences
- Detailed insights about programs, costs, and campus features
- Weather analysis for different regions

### Knowledge Base Integration
- ChromaDB vector database for context-aware recommendations
- Retrieval-Augmented Generation (RAG) for providing relevant information
- Persistent memory across sessions to provide consistent guidance

### Application Management
- Application tracking for multiple universities
- Downloadable application checklist (DOCX format)
- Customizable application tracker template (CSV format)

### User Sessions
- User profiles with saved preferences
- Persistent chat history
- Continuous refinement of recommendations based on interactions

## 🛠️ Technical Architecture

The system uses several components:

- **Frontend**: Streamlit web application
- **Vector Database**: ChromaDB for storing embeddings
- **LLM Integration**: OpenAI API for generating recommendations
- **External Data**: OpenWeather API for climate information
- **Document Processing**: Python-docx for handling document templates

## 📋 Requirements

```
streamlit
pandas
chromadb
openai
python-docx
requests
pysqlite3-binary
docx
```

## 🔧 Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/insightbot.git
   cd insightbot
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment secrets:
   Create a `.streamlit/secrets.toml` file with the following contents:
   ```toml
   open-key = "your-openai-api-key"
   pinecone_api_key = "your-pinecone-api-key"
   open-weather = "your-openweather-api-key"
   ```

4. Prepare your data:
   - Ensure the `data` directory contains:
     - `University_Data.docx`: Contains university information
     - `Avg_Living_Expenses.csv`: Contains state-wise living cost data
     - `Employment_Projections.csv`: Contains job market trends
     - `compass_logo.png` and `compass_logo_wide.png`: Application logos

5. Launch the application:
   ```bash
   streamlit run new_agent.py
   ```

## 🖥️ Usage Guide

### First-time Setup
1. Enter your name to create a user profile
2. Set your preferences:
   - Field of study
   - Budget range
   - Preferred locations
   - Weather preferences

### Chat Interface
- Ask questions about universities, programs, costs, or job prospects
- Request specific information about universities or locations
- Explore scholarship opportunities
- Get weather comparisons

### Special Commands
- Click "Top 3 Recommendations" to get personalized university suggestions
- Download application checklists in DOCX format
- Access application tracking templates in CSV format
- Add universities to your tracking list by saying "add [university name] to the tracker"

### Example Queries
- "Tell me about computer science programs in the Northeast"
- "What's the cost of living in California?"
- "How's the job market for data science graduates?"
- "Compare UNC Chapel Hill and Georgia Tech for engineering"
- "What scholarships are available for international students?"

## 📊 Data Integration

The system integrates multiple data sources:

1. **University Information**: Comprehensive details about universities, programs, and costs
2. **Living Expenses**: State-wise cost of living indices for groceries, housing, utilities, transportation, healthcare, and miscellaneous expenses
3. **Employment Projections**: Future outlook for various occupations including growth rates, annual openings, and median wages
4. **Weather Data**: Real-time climate information from OpenWeather API

## 👨‍💻 Development

For developers looking to extend the functionality:

- `new_agent.py`: Main application file
- `chromadb_server.py`: Server for handling database queries
- `compass_main.py`: Streamlit UI components (may be renamed in future updates)
- `langchain123.py`: Integration with external APIs
- `clear_pine.py`: Utility for managing Pinecone indexes

## 📄 License

[Include appropriate license information here]

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact

[Include your contact information or project maintainer details here]

---

*InsightBot - Helping international students navigate their educational journey with confidence.*
