# 🚀 EdgeForge

<div align="center">

### AI-Powered Python Static Analysis & Edge Case Generation Platform

Analyze Python source code, detect potential issues, assess code quality, and automatically generate edge test cases through an intuitive Flask-based web interface.

# 🚀 EdgeForge

## 🌐 Live Demo

https://edgeforge-pz9o.onrender.com

AI-Powered Python Static Analysis & Edge Case Generation Platform

---

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![GitHub](https://img.shields.io/badge/Open%20Source-GitHub-181717?style=for-the-badge&logo=github)

</div>

---

# 📖 Overview

EdgeForge is a Python static analysis platform designed to help developers understand their source code before execution.

Instead of simply running code, EdgeForge parses the Python Abstract Syntax Tree (AST), extracts structural information, analyzes functions and classes, detects potential risks, and generates useful edge-case test scenarios.

The application provides an interactive Flask dashboard where users can upload Python files, view detailed analysis results, inspect generated edge cases, and download an HTML report.

---

# ✨ Features

- ✅ Python AST Parsing
- ✅ Function & Class Detection
- ✅ Parameter Analysis
- ✅ Edge Case Generation
- ✅ Static Code Analysis
- ✅ Risk Assessment
- ✅ HTML Report Generation
- ✅ Downloadable Reports
- ✅ Syntax Error Detection
- ✅ Modern Flask Dashboard
- ✅ Multiple Test File Support
- ✅ Unicode Support
- ✅ Async Function Support
- ✅ Nested Function Detection
- ✅ Object-Oriented Code Analysis

---

# 🏗 Architecture

```
                    +----------------------+
                    |   Python Source File |
                    +----------+-----------+
                               |
                               v
                      +------------------+
                      |   Flask Upload   |
                      +--------+---------+
                               |
                               v
                     +--------------------+
                     |   AST Parser       |
                     +---------+----------+
                               |
             +-----------------+----------------+
             |                                  |
             v                                  v
     +------------------+              +--------------------+
     | Static Analyzer  |              | Edge Generator     |
     +---------+--------+              +---------+----------+
               |                                 |
               +---------------+-----------------+
                               |
                               v
                    +----------------------+
                    | HTML Report Builder  |
                    +----------+-----------+
                               |
                               v
                     +--------------------+
                     | Flask Dashboard    |
                     +--------------------+
```

---

# 📂 Project Structure

```
EdgeForge/
│
├── analyzer/
├── generator/
├── parser_engine/
├── models/
├── report/
├── static/
├── templates/
├── uploads/
├── tests/
├── screenshots/
│
├── app.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🖼 Screenshots

## Home Page

![Home](screenshots/home.png)

---

## Dashboard

![Dashboard](screenshots/dashboard.png)

---

## Generated Report

![Report](screenshots/report.png)

---

## Syntax Error Detection

![Syntax Error](screenshots/syntax_error.png)

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/venkateshA-cmd/EdgeForge.git
```

Enter the project directory

```bash
cd EdgeForge
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 🚀 Usage

## Step 1 — Upload a Python File

Open the web application and upload any valid Python (.py) source file.

Examples include:

- Simple Python scripts
- Object-Oriented Programs
- Flask Applications
- Utility Modules
- Algorithm Implementations

---

## Step 2 — Automatic Analysis

EdgeForge automatically performs several analysis stages:

- Parses the Abstract Syntax Tree (AST)
- Detects functions and classes
- Extracts parameters
- Analyzes potential risks
- Generates edge-case test scenarios
- Calculates project statistics
- Builds a complete HTML report

---

## Step 3 — View Dashboard

The dashboard displays:

- Total Functions
- Total Classes
- Total Parameters
- Risk Score
- Findings
- Generated Edge Cases

---

## Step 4 — Download Report

Generate a professional HTML report that can be shared, archived, or used for documentation.

---

# 🧪 Testing

EdgeForge has been tested using multiple Python source files covering a wide range of scenarios.

### Test Coverage

| Test | Status |
|-------|--------|
| Empty File | ✅ |
| Syntax Errors | ✅ |
| Functions | ✅ |
| Nested Functions | ✅ |
| Multiple Classes | ✅ |
| OOP Programs | ✅ |
| Async Functions | ✅ |
| Decorators | ✅ |
| Unicode Support | ✅ |
| Large Files | ✅ |
| Recursion | ✅ |
| Loops | ✅ |

---

# 📊 Analysis Capabilities

EdgeForge currently analyzes:

- Python Functions
- Class Definitions
- Method Parameters
- Return Statements
- Nested Functions
- Async Functions
- Decorators
- Object-Oriented Structures
- Syntax Errors
- Code Complexity Indicators

---

# 🛠 Technologies Used

## Backend

- Python
- Flask

## Parsing Engine

- Python AST Module

## Frontend

- HTML5
- CSS3

## Reports

- HTML Report Generator

## Version Control

- Git
- GitHub

---

# 📈 Project Workflow

```
Upload Python File
        │
        ▼
AST Parsing
        │
        ▼
Structure Extraction
        │
        ▼
Static Analysis
        │
        ▼
Edge Case Generation
        │
        ▼
Risk Assessment
        │
        ▼
HTML Report Generation
        │
        ▼
Dashboard Visualization
```

---

# 📌 Sample Project Output

EdgeForge provides:

- Project Statistics
- Function Inventory
- Class Inventory
- Parameter Information
- Edge Test Cases
- Code Findings
- Risk Analysis
- Downloadable HTML Reports

---

# 🎯 Use Cases

EdgeForge is useful for:

- Students learning Python
- Software Engineering Labs
- Static Code Analysis
- Code Reviews
- Academic Projects
- Software Testing
- Edge Case Discovery
- Python Learning
- Teaching AST Concepts
- Flask Development Demonstrations

---

# 📄 Requirements

- Python 3.10+
- Flask
- Modern Web Browser

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 🌟 Key Highlights

- 🚀 Modern Flask-based Web Application
- 🧠 Python AST (Abstract Syntax Tree) Parsing
- 🔍 Static Code Analysis
- ⚡ Automatic Edge Case Generation
- 📊 Interactive Analysis Dashboard
- 📄 Professional HTML Report Generation
- 🛡️ Syntax Error Detection
- 🧪 Comprehensive Test Coverage
- 📦 Clean Project Architecture
- 💻 Beginner-Friendly User Interface

---

# 🛣️ Roadmap

## Version 1.1

- [ ] PDF Report Export
- [ ] CSV Report Export
- [ ] Code Complexity Metrics
- [ ] Function Dependency Graph
- [ ] Duplicate Code Detection

## Version 1.2

- [ ] Multi-file Project Analysis
- [ ] ZIP Upload Support
- [ ] Batch Processing
- [ ] Enhanced Risk Scoring

## Version 2.0

- [ ] AI-powered Code Suggestions
- [ ] Code Refactoring Recommendations
- [ ] REST API
- [ ] Docker Support
- [ ] User Authentication
- [ ] Project History Dashboard

---

# 🤝 Contributing

Contributions are welcome!

If you would like to improve EdgeForge:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

Please keep pull requests focused and include clear descriptions of your changes.

---

# 🐞 Reporting Issues

If you discover a bug or have a feature request:

- Open a GitHub Issue.
- Include steps to reproduce the problem.
- Describe the expected and actual behavior.
- Attach screenshots if applicable.

---

# 📚 Learning Goals

EdgeForge demonstrates practical concepts including:

- Python Programming
- Flask Web Development
- Static Code Analysis
- Abstract Syntax Trees (AST)
- Software Testing
- Edge Case Generation
- Software Engineering Practices
- Git & GitHub Workflows

---

# 📜 License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.

---

# 👨‍💻 Author

**Venkatesh A**

- GitHub: https://github.com/venkateshA-cmd

---

# ⭐ Support

If you found this project useful:

- ⭐ Star this repository
- 🍴 Fork it
- 📢 Share it with others

Your support helps improve the project and encourages future development.

---

<div align="center">

## 🚀 EdgeForge

**Analyze Better • Test Smarter • Build Stronger**

Made with ❤️ using Python & Flask.

</div>
