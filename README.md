
# 🌌 YOU-N-I-VERSE Builder

A self-organizing universe builder that transforms your conversations, code snippets, and notes into a structured application automatically.

## 🚀 What It Does

Drop your files (conversations, code, docs) into `/uploads/` and the Universe Builder will:

- **Analyze** your content using NLP and pattern recognition
- **Classify** files by type (Python, HTML, text conversations, etc.)
- **Extract** intent, structure, and relationships
- **Generate** a complete app structure in `/generated_app/`
- **Provide** a live preview of what's being built

## 🏗️ Project Structure

```
universe_builder/
├── app.py                    # Main Flask app (serves build triggers)
├── builder_engine.py         # Orchestrates the whole pipeline
├── parser/
│   ├── layout_organizer.py   # Creates directory structure from content
│   ├── spec_extractor.py     # Extracts intent/specs from files
│   └── file_classifier.py    # Detects file types
├── uploads/                  # Drop your files here
├── generated_app/            # Your generated universe appears here
├── replit_ui/
│   ├── index.html            # Live preview interface
│   └── universe.css          # Cosmic styling
└── README.md
```

## 🛠️ How to Use

1. **Start the Builder**
   ```bash
   python universe_builder/app.py
   ```

2. **Upload Your Files**
   - Drop conversations, code snippets, or notes into `/uploads/`
   - Supported formats: `.py`, `.html`, `.js`, `.txt`, `.md`, `.json`

3. **Trigger the Build**
   - Visit the web interface and click "Trigger Build"
   - Or POST to `/build` endpoint

4. **Preview Your Universe**
   - Check `/generated_app/` for your scaffolded application
   - View live preview at `/preview`

## 🌟 Features

- **Smart File Classification**: Automatically detects Python, HTML, JavaScript, text, and JSON files
- **Intent Extraction**: Pulls out goals, features, and structure from conversations
- **Modular Generation**: Creates organized folder structures with backend, frontend, docs
- **Live Preview**: Real-time UI to see your universe being built
- **Self-Expanding**: Generated apps include hooks for further expansion

## 🎯 Example Workflow

1. Upload a conversation about building a bot system
2. Upload some Python code snippets
3. Upload HTML mockups
4. Trigger build
5. Get a complete Flask app with:
   - Organized backend modules
   - Frontend templates
   - Documentation
   - Configuration files

## 🚀 API Endpoints

- `GET /` - Welcome message
- `POST /build` - Trigger universe generation
- `GET /status` - Check uploaded files
- `GET /preview` - Live preview interface
- `GET /file_content?path=<file>` - Get generated file content

## 🌌 Generated App Structure

Your generated universe will include:

```
generated_app/
├── app.py              # Main Flask application
├── backend/            # Python modules and logic
├── frontend/
│   ├── templates/      # HTML components
│   └── static/         # JavaScript and CSS
├── docs/               # Documentation from conversations
├── config/             # Configuration files
└── README.md           # Generated documentation
```

## 🔧 Customization

The builder is designed to be modular. You can extend:

- **File Classifiers**: Add support for new file types
- **Spec Extractors**: Enhance content analysis
- **Layout Generators**: Create new app structures
- **UI Components**: Customize the preview interface

## 🌟 Next Steps

1. Add LLM integration for deeper conversation analysis
2. Support for more frameworks (React, Vue, etc.)
3. Real-time file watching
4. Advanced template system
5. Deploy integration

---

**Ready to build your universe?** 🌌

Drop your files and let the cosmic magic begin!
