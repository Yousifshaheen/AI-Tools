import streamlit as st
# تتتتتتتتتتتتتتتتتتتتتتتتتتتتت
st.set_page_config(page_title="AI Tools For Students", layout="wide")

st.title("🎓 AI Tools For Students")

tools_data = {
    "Understanding Concepts": {
        "ChatGPT": {
            "description": "Explains difficult concepts in simple language.",
            "use": "Understanding medical and academic topics.",
            "strength": "Interactive and flexible responses.",
            "link": "https://chat.openai.com",
            "image": "https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg"
        },
        "Gemini": {
            "description": "Google AI assistant for learning and reasoning.",
            "use": "Deep explanations and advanced topics.",
            "strength": "Google ecosystem integration.",
            "link": "https://gemini.google.com",
            "image": "https://upload.wikimedia.org/wikipedia/commons/8/8f/Google-gemini-icon.svg"
        },
        "Claude": {
            "description": "Detailed long-form AI assistant.",
            "use": "Complex concept explanation.",
            "strength": "Clear structured answers.",
            "link": "https://claude.ai",
            "image": "https://claude.ai/images/claude_app_icon.png"
        }
    },

    "Writing & Academic Writing": {
        "Grammarly": {
            "description": "Grammar and writing assistant.",
            "use": "Improve assignments and reports.",
            "strength": "Professional writing enhancement.",
            "link": "https://www.grammarly.com",
            "image": "https://upload.wikimedia.org/wikipedia/commons/d/d5/Grammarly_icon.svg"
        },
        "QuillBot": {
            "description": "Paraphrasing and rewriting tool.",
            "use": "Rewrite academic text.",
            "strength": "Strong paraphrasing engine.",
            "link": "https://quillbot.com",
            "image": "https://assets.quillbot.com/images/meta/logo.png"
        },
        "Notion AI": {
            "description": "Writing and note organization inside Notion.",
            "use": "Writing and organizing study notes.",
            "strength": "Writing + productivity together.",
            "link": "https://www.notion.so/product/ai",
            "image": "https://upload.wikimedia.org/wikipedia/commons/4/45/Notion_app_logo.png"
        }
    },

    "Research & Scientific Papers": {
        "Perplexity": {
            "description": "Search engine with cited answers.",
            "use": "Quick scientific research.",
            "strength": "Reliable references.",
            "link": "https://www.perplexity.ai",
            "image": "https://www.perplexity.ai/favicon.ico"
        },
        "SciSpace": {
            "description": "Explains research papers.",
            "use": "Understanding academic articles.",
            "strength": "Simplifies scientific papers.",
            "link": "https://www.scispace.com",
            "image": "https://www.scispace.com/favicon.ico"
        },
        "Elicit": {
            "description": "Literature review assistant.",
            "use": "Finding and comparing papers.",
            "strength": "Strong for research.",
            "link": "https://elicit.com",
            "image": "https://elicit.com/favicon.ico"
        },
        "Consensus": {
            "description": "Scientific evidence search.",
            "use": "Evidence-based answers.",
            "strength": "Finds scientific consensus.",
            "link": "https://consensus.app",
            "image": "https://consensus.app/favicon.ico"
        },
        "Scite": {
            "description": "Tracks paper citations.",
            "use": "Evaluate paper credibility.",
            "strength": "Citation intelligence.",
            "link": "https://scite.ai",
            "image": "https://scite.ai/favicon.ico"
        }
    },

    "Notes & Summarization": {
        "NotebookLM": {
            "description": "Summarizes your uploaded files.",
            "use": "Lecture summaries.",
            "strength": "Works on your documents.",
            "link": "https://notebooklm.google",
            "image": "https://ssl.gstatic.com/docs/doclist/images/mediatype/icon_1_document_x16.png"
        },
        "Mem.ai": {
            "description": "Smart knowledge organization.",
            "use": "Structured notes.",
            "strength": "Auto-linking notes.",
            "link": "https://mem.ai",
            "image": "https://mem.ai/favicon.ico"
        },
        "Otter.ai": {
            "description": "Converts speech to notes.",
            "use": "Lecture transcription.",
            "strength": "Excellent voice notes.",
            "link": "https://otter.ai",
            "image": "https://otter.ai/favicon.ico"
        }
    },

    "Organization & Productivity": {
        "Flow": {
            "description": "Focus management tool.",
            "use": "Study sessions.",
            "strength": "Maintains concentration.",
            "link": "https://www.flow.app",
            "image": "https://www.flow.app/favicon.ico"
        },
        "Forest": {
            "description": "Focus timer app.",
            "use": "Avoid distractions.",
            "strength": "Motivating focus.",
            "link": "https://www.forestapp.cc",
            "image": "https://www.forestapp.cc/favicon.ico"
        }
    },

    "Presentations & Visual Learning": {
        "Canva": {
            "description": "Design presentations easily.",
            "use": "Create slides.",
            "strength": "Beautiful templates.",
            "link": "https://www.canva.com",
            "image": "https://static.canva.com/static/images/favicon.ico"
        },
        "Gamma": {
            "description": "AI presentation creator.",
            "use": "Generate slides fast.",
            "strength": "Very fast creation.",
            "link": "https://gamma.app",
            "image": "https://gamma.app/favicon.ico"
        }
    },

    "Diagrams & Medical Visualization": {
        "Excalidraw": {
            "description": "Create diagrams visually.",
            "use": "Medical concept maps.",
            "strength": "Simple visual learning.",
            "link": "https://excalidraw.com",
            "image": "https://excalidraw.com/favicon.ico"
        }
    },

    "Career & Interview Prep": {
        "Final Round AI": {
            "description": "AI interview coach.",
            "use": "Interview preparation.",
            "strength": "Professional training.",
            "link": "https://www.finalroundai.com",
            "image": "https://www.finalroundai.com/favicon.ico"
        }
    }
}

category = st.sidebar.radio("Select Category", list(tools_data.keys()))
st.header(category)

tool_names = list(tools_data[category].keys())
tabs = st.tabs(tool_names)

for tab, tool in zip(tabs, tool_names):
    info = tools_data[category][tool]

    with tab:
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader(tool)
            st.info(info["description"])
            st.success(f"Best Use: {info['use']}")
            st.warning(f"Strength: {info['strength']}")
            st.link_button("🔗 Visit Website", info["link"])

        with col2:
            st.image(info["image"], use_container_width=True)
