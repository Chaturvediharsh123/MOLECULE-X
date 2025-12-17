# Molecule-X: AI-Native Multi-Agent Drug Repurposing Copilot

Molecule-X transforms months of manual drug research into hours of automated AI-driven insights. This multi-agent system coordinates specialized AI agents to gather, analyze, and synthesize scientific, clinical, patent, and market data into ranked drug repurposing opportunities.

## ✨ Key Features

- 🤖 **Multi-Agent AI System** - Autonomous agents for knowledge, clinical trials, patents, and market analysis
- 🎯 **Drug Repurposing Assistant** - Query any drug for potential new therapeutic applications
- 🧪 **Molecular Toxicity Predictor** - Predict toxicity from SMILES notation using ML
- 📊 **Evidence-Based Ranking** - Scores opportunities based on scientific validation and feasibility
- 🚀 **Real-World Ready** - Works with ANY drug query, powered by Google Gemini API

## 🧠 System Architecture

```
User Query ("Explore neurological uses of Ketamine")
   ↓
Master Agent (LLM-powered extraction)
   ↓
┌─────────────┬──────────────┬──────────────┬──────────────┐
Patent Agent  Clinical Agent Knowledge Agent Market Agent
└─────────────┴──────────────┴──────────────┴──────────────┘
   ↓
Autonomous Data Gathering + Analysis
   ↓
Evidence Synthesis + Ranking
   ↓
Innovation Dossier (Final Output)
```

## 🔧 Core Technologies

| Component | Technology |
|----------|------------|
| LLM | Google Gemini API (gemini-2.5-flash) |
| Agent Framework | Custom Python Multi-Agent System |
| ML Model | RandomForest (scikit-learn) |
| Molecular Featurization | RDKit Morgan Fingerprints |
| Data Sources | PubMed, ClinicalTrials.gov APIs |
| UI | Streamlit |
| Environment | Python 3.11+ |

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key
Create a `.env` file in the project root:
```env
GOOGLE_API_KEY=your_google_api_key_here
```
Get your free Gemini API key: https://aistudio.google.com/apikey

### 3. Train the Toxicity Model (First Time Only)
```bash
python src/train.py
```

### 4. Launch the Application
```bash
# Option 1: Using main entry point
python main.py

# Option 2: Direct Streamlit launch
streamlit run src/app.py

# Option 3: Windows quick launch
run.bat
```

### 5. Start Researching!
- **Drug Repurposing**: Enter queries like "Explore neurological uses of Ketamine beyond anesthesia"
- **Toxicity Prediction**: Input SMILES notation (e.g., `CN(C)C=O`)

## 📁 Project Structure

```
molecule-x/
├── src/
│   ├── app.py                 # Streamlit UI (main interface)
│   ├── advanced_agents.py     # Multi-agent orchestration system
│   ├── llm_utils.py          # Google Gemini API integration
│   ├── fixed_utils.py        # Mock data utilities (PubMed, trials)
│   ├── train.py              # ML model training
│   ├── predict.py            # Toxicity prediction CLI
│   ├── featurize.py          # Molecular fingerprint generation
│   └── simulate_impact.py    # Impact simulation analysis
├── data/
│   └── molecules.csv         # Training dataset (SMILES + labels)
├── models/
│   └── molecule_x_model.pkl  # Trained RandomForest model
├── .env                      # API key configuration (create this)
├── main.py                   # Main entry point
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

## 🎯 How It Works

### Drug Repurposing Mode
1. **Query Input**: "Explore neurological uses of Ketamine beyond anesthesia"
2. **LLM Extraction**: Gemini API extracts drug name (Ketamine) and indication (neurological)
3. **Agent Coordination**: Specialized agents gather evidence from multiple sources
4. **Synthesis**: Master agent ranks opportunities based on scientific feasibility
5. **Output**: Comprehensive research dossier with ranked insights

### Toxicity Prediction Mode
1. **SMILES Input**: Molecular structure notation (e.g., `CCO` for ethanol)
2. **Featurization**: RDKit generates Morgan fingerprints
3. **Prediction**: RandomForest model predicts toxicity probability
4. **Risk Assessment**: High/Low risk classification

## 🏆 Benefits

- 🚀 **10x Faster Research**: Hours instead of months for comprehensive drug analysis
- 💡 **Any Drug, Any Indication**: LLM-powered extraction works with real-world queries
- 📊 **Evidence-Based Decisions**: Multi-source validation reduces clinical trial risk
- 🎯 **Actionable Insights**: Ranked opportunities with detailed justification
- 💰 **Cost-Effective**: Free Gemini API for unlimited research queries

## 🛠️ Implementation Status

- ✅ Google Gemini API integration (gemini-2.5-flash)
- ✅ Multi-agent orchestration system
- ✅ Drug name & indication extraction from natural language
- ✅ Knowledge, Clinical, Patent, Market agents
- ✅ Evidence synthesis and ranking
- ✅ Molecular toxicity prediction (RandomForest + RDKit)
- ✅ Streamlit web interface
- ✅ Fallback extraction for API quota limits
- ⚠️ Using mock data sources (replace with live APIs in production)

## 📊 Example Queries

### Drug Repurposing
- "Explore neurological uses of Ketamine beyond anesthesia"
- "What are the potential uses of metformin in cancer treatment?"
- "Investigate ivermectin for viral infections"
- "Can aspirin be repurposed for Alzheimer's disease?"

### Toxicity Prediction
- `CCO` - Ethanol
- `CN(C)C=O` - Dimethylformamide
- `CC(=O)O` - Acetic acid
- `CCCC` - Butane

## ⚠️ Important Notes

### API Quota Limits
The free Gemini API has rate limits. If you see "429 quota exceeded" errors:
- Check usage: https://ai.dev/usage?tab=rate-limit
- Get new key: https://aistudio.google.com/apikey
- The app will fall back to keyword extraction automatically

### SMILES Input
When using the Toxicity Predictor, enter ONLY the SMILES notation without labels:
- ✅ Correct: `CN(C)C=O`
- ❌ Wrong: `CN(C)C=O,1` (don't include the label from CSV)

## 🔮 Future Enhancements

1. **Live API Integration**: Real PubMed & ClinicalTrials.gov data
2. **Vector Database**: RAG-based evidence retrieval with FAISS
3. **Advanced Scoring**: Multi-factor weighted ranking algorithms
4. **Patent Analysis**: Real-time patent freedom analysis
5. **Market Intelligence**: Current market size & competition data
6. **Export Features**: PDF/Word report generation

## 📚 Technologies Used

- **Python 3.11+**: Core language
- **Google Gemini API**: LLM for drug extraction and synthesis
- **Streamlit**: Interactive web interface
- **RDKit**: Molecular informatics and fingerprinting
- **scikit-learn**: Machine learning (RandomForest)
- **pandas/numpy**: Data manipulation

## 📄 License

This project is for research and educational purposes.