# Study Buddy AI

**Project Summary**

Study Buddy AI is an educational application built with **Streamlit** that allows users to automatically generate quizzes based on topic, question type (multiple choice or fill-in-the-blanks), difficulty level, and number of questions. The app evaluates answers and provides a **score** along with a **confidence level** using the **Hallucinate Detector** from *Victara*. Results can be saved as CSV files.

---

## Features

* Choose topic, difficulty level, and number of questions.
* Two question types: **Multiple Choice (MCQ)** and **Fill-in-the-Blanks**.
* Automatic quiz generation and instant results.
* Score calculation with confidence level (Victara Hallucination Detector).
* Export results to **CSV**.
* CI/CD pipeline: **Jenkins** for CI and **ArgoCD** for CD.
* Deployable on cloud servers or Kubernetes clusters.

---

## [Demo](https://drive.google.com/file/d/1tkaI-hLyGhF62cAcBcYE6OQQoPQFiVGL/view?usp=sharing))

---

## Architecture

* **Frontend & App**: streamlit
* **Backend Logic**: Python (within Streamlit app)
* **Model / AI**: **Groq API** for question and answer generation
* **Hallucination Detection**: Victara API
* **CSV Export**: Python (Pandas/CSV writer)
* **CI**: Jenkins
* **CD**: ArgoCD (with Kubernetes manifests)

---

## Usage

1. Run the app locally:

   ```bash
   streamlit run app.py
   ```
2. Enter the quiz parameters (topic, difficulty, type, number of questions).
3. Answer the quiz and view your score + confidence level.
4. Download results as CSV via the **Download CSV** button.

---


## CI/CD Setup

### Why separate CI and CD?

* **CI (Continuous Integration):** Build, test, and package (e.g., Docker image). Ensures quality before release.
<img width="1850" height="525" alt="Image" src="https://github.com/user-attachments/assets/b03416d1-c3f6-4afa-900f-f9249d5d3061" />

* **CD (Continuous Deployment):** Deploy to production. Separation avoids broken builds reaching production and simplifies debugging.
<img width="1417" height="602" alt="Image" src="https://github.com/user-attachments/assets/c241150a-1de2-4e75-8cb3-43329c57a74c" />

### Why ArgoCD for CD?

* **GitOps-based**: Git as the single source of truth.
* **Automated sync & rollback**: Easy rollbacks and continuous sync with Kubernetes.
* **Great visibility**: UI to monitor app health and deployments.
* **Kubernetes-native**: Designed specifically for K8s.

---


## Structure



```
.
├── manifests/
│   ├── deployment.yaml
│   └── service.yaml
├── src/
│   ├── common/
│   │   ├── init.py
│   │   ├── custom_exception.py
│   │   └── logger.py
│   ├── config/
│   │   ├── init.py
│   │   └── setting.py
│   ├── generator/
│   │   ├── init.py
│   │   └── question_generator.py
│   ├── llm/
│   │   ├── init.py
│   │   └── groq_client.py
│   ├── models/
│   │   ├── init.py
│   │   └── question_schema.py
│   ├── prompt_catalog/
│   │   ├── init.py
│   │   └── template.py
│   └── utils/
│       ├── init.py
│       ├── halluicinate.py
│       └── util_functions.py
├── .env
├── .gitignore
├── application.py
├── Dockerfile
├── Jenkinsfile
├── kubectl
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```
