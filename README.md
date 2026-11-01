# VazhehKav | واژه‌کاو

**VazhehKav** is a Persian-language comment intelligence platform that combines Natural Language Processing (NLP), machine learning, and Django to analyze user-generated comments.

The platform evaluates comments from two perspectives:

- **Recommendation Analysis:** Estimates how likely a comment is to recommend a product or service.
- **Offensive Content Detection:** Estimates how likely a comment is to contain offensive language.

Built with Python and Django, VazhehKav also provides user accounts, an API for submitting comments, persistent storage, and an analytics dashboard for exploring comment statistics.

> **Project Status:** Initial implementation. Model evaluation, security improvements, automated testing, and deployment preparation are ongoing.

## Features

### Machine Learning & NLP

- Analyzes Persian-language comments using trained machine learning models.
- Predicts recommendation likelihood.
- Detects potentially offensive content.
- Applies Persian text preprocessing using [Hazm](https://github.com/roshan-research/hazm).
- Loads trained models through serialized Scikit-learn pipelines.

### Web Application

- User registration and authentication.
- Custom user model with phone-number-based accounts.
- API key generation for authenticated API access.
- Comment storage with prediction scores and optional tags.
- Dashboard for exploring comment statistics.
- Monthly statistics covering:
  - Recommended comments
  - Not-recommended comments
  - Offensive comments
  - Non-offensive comments

### REST API

- Accepts Persian comments for analysis and storage.
- Supports optional tags and dates.
- Associates submitted comments with user accounts through API keys.

## How It Works

The platform processes comments through the following workflow:

1. **Input:** A user submits a Persian-language comment.
2. **Preprocessing:** The text is normalized and processed using Hazm and other text-processing utilities.
3. **Prediction:** Two trained machine learning pipelines estimate the recommendation and offensiveness probabilities.
4. **Storage:** The comment and its associated prediction scores can be stored in the database.
5. **Analytics:** Stored comments are aggregated and presented through the dashboard.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Persian NLP | Hazm |
| Text Processing | Emoji |
| Data Visualization | Matplotlib |
| Web Framework | Django |
| REST API | Django REST Framework |
| Database | SQLite |
| Configuration | python-dotenv |

## Project Structure

```text
vazheh-kav/
├── data/
├── notebooks/
├── web/
│   ├── accounts/
│   ├── config/
│   ├── core/
│   ├── services/
│   │   └── models/
│   └── manage.py
├── .gitignore
├── LICENSE
└── requirements.txt
```

- `data/`: Dataset-related files.
- `notebooks/`: Jupyter notebooks for data exploration, preprocessing, and model development.
- `web/accounts/`: User account and authentication functionality.
- `web/config/`: Django project configuration.
- `web/core/`: Main application functionality.
- `web/services/`: Model loading and prediction services.
- `web/services/models/`: Saved machine learning pipelines.

## API Usage

### Analyze a Comment

**Endpoint:** `POST /analyze_comment/`

The API accepts the following fields:

| Field | Required | Description |
|---|---|---|
| `api_key` | Yes | API key associated with the user account |
| `text` | Yes | Persian comment to analyze |
| `tag` | No | Optional tag for categorizing the comment |
| `date` | No | Optional date associated with the comment |

**Example Request Body:**

```json
{
    "api_key": "YOUR_API_KEY",
    "text": "کیفیت این محصول واقعاً عالی بود.",
    "tag": "product-feedback",
    "date": "2026-10-27"
}
```

A successful request returns a confirmation message indicating that the comment has been saved.

> **Note:** The current API endpoint does not return prediction scores directly in its response. Recommendation and offensiveness scores are stored alongside the submitted comment and can be explored through the dashboard.

## Limitations & Future Improvements

VazhehKav is an initial implementation and has several areas that require further development:

- **Language Support:** Currently designed for Persian-language comments only.
- **Model Evaluation:** Comprehensive evaluation metrics and a reproducible evaluation methodology need to be documented.
- **Prediction Reliability:** Model predictions are estimates and should not be considered perfectly reliable classifications.
- **Input Validation:** API validation and error handling require further improvement.
- **Security:** The development configuration needs additional security hardening before public deployment.
- **Testing:** Automated test coverage needs to be expanded.
- **Documentation:** API documentation and setup instructions can be improved.

## License

This project is licensed under the [MIT License](LICENSE).
