# Academic Marks Predictor

A Flask web app that predicts student marks based on daily study hours and shows the result with an interactive frontend dashboard.

## Features

- Clean modern UI for marks prediction
- Study-hours slider input
- Real-time prediction score update
- Circular progress indicator
- Basic hover effects and responsive layout

## Tech Stack

- Python
- Flask
- HTML, CSS, JavaScript

## Project Structure

```text
student-marks-prediction/
|-- app.py
|-- model.pkl
|-- train_model.py
|-- requirements.txt
|-- .gitignore
`-- templates/
    `-- index.html
```

## Installation

1. Open terminal in the project folder:

```powershell
cd "d:\internship projects\student-marks-prediction"
```

2. Create and activate virtual environment:

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

## Run Locally

```powershell
python app.py
```

Open: `http://127.0.0.1:5000`

## API Endpoint

### `POST /predict`

Request body:

```json
{
  "hours": 8.5
}
```

Response (example):

```json
{
  "status": "success",
  "prediction": 86.7,
  "dash_offset": 92.1,
  "metadata": {
    "engine": "Linear Regression v1.2",
    "confidence_interval": "±3.4%",
    "developer": "Tanishq Tamgadge"
  }
}
```

## Deployment (Render)

1. Push this folder to a GitHub repository.
2. Go to [Render](https://render.com) and create a **Web Service**.
3. Connect your repo.
4. Use:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Deploy.

## Notes

- `model.pkl` and `train_model.py` are included for model workflow.
- Current app prediction logic uses coefficients in `app.py`.

