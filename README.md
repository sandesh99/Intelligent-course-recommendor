# Intelligent Course Recommender CLI

A lightweight Python CLI tool to provide **personalized course recommendations** and **career/learning path guidance** based on your background, interests, and goals. It uses **OpenAI embeddings** and **RAG-based Q\&A** for smarter recommendations and context-aware answers.

---

## Why This Project Exists

With so many online courses available, students often feel overwhelmed. This tool helps by:

* Suggesting courses that match your profile.
* Adapting recommendations based on your feedback.
* Answering learning path questions considering your goals.

---

## Key Features

* **Personalized Recommendations:** Top courses based on your profile and interests.
* **Feedback Loop:** "Like" or "Dislike" courses to improve future suggestions.
* **RAG Q\&A Agent:** Ask career/learning questions like “Should I learn Python or R?”.
* **Human-friendly CLI:** Interactive, easy-to-use menu with input validation.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/course-recommender.git
cd course-recommender
```

2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Data

* `data/courses.json` – Predefined dataset of 40 curated courses.
* `data/feedback.json` – Stores user feedback.
* `data/knowledge_base/` – Markdown files used for career guidance and learning path Q\&A.

---

## Usage

Run the CLI:

```bash
python src/cli.py
```

Interactive menu example:

```
Welcome to the Course Recommender CLI!
Enter your name: Alice
Enter your background: Final-year CS student
Enter your interests: AI, Data Science
Enter your career goals: Become an ML Engineer

--- Menu ---
1. Get course recommendations
2. Ask a career/learning question
3. Exit
Choose an option:
```

* **Option 1:** Shows top 5 recommended courses.
* **Option 2:** Ask questions about learning paths or career.
* **Option 3:** Exit the program.

---

## Feedback Handling

* Enter numbers of courses you liked or disliked (comma-separated).
* Invalid entries are skipped and reported together:

```
Skipped invalid liked course numbers: a, 100
Skipped invalid disliked course numbers: x
```

* Feedback is stored in `feedback.json` and used to improve future recommendations.

---

## Sample Session

```
Top 5 courses for you:
1. Introduction to AI (ai, machine-learning, beginners)
2. Machine Learning Specialization (machine-learning, data-science)
3. Deep Learning for NLP (nlp, deep-learning)
4. Data Science Capstone Project (data-science, project)
5. Generative AI with LLMs (generative-ai, llm, transformers)

Liked courses (comma) or skip: 1,5
Disliked courses (comma) or skip: 3

Feedback recorded!!

Enter your question: Should I learn Python or R for Data Science?
Answer:
Python is recommended for most data science workflows including ML, deep learning, and AI. R is better for statistical analysis but less versatile for production ML pipelines.
```


---

## Design Choices

* **OpenAI Embeddings** – Semantic matching of user profile with course descriptions.
* **Chroma DB** – Stores vectorized knowledge base for RAG retrieval.
* **Tag-based Feedback** – Adjusts course rankings based on likes/dislikes.
* **Modular Architecture** – CLI, recommender, embeddings, QA agent separated for maintainability.
* **Humanized CLI** – Clear prompts, input validation, and concise output.

