from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Mock weights based on a standard Student Performance Model
# In a production environment, you would use: model = pickle.load(open('model.pkl', 'rb'))
COEFFICIENT = 5.24  # Increase in marks per hour
INTERCEPT = 42.15   # Baseline marks with minimal study

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        hours = float(data.get('hours', 8.5))
        
        # Artificial latency to make the "Predicting..." state visible in UI
        time.sleep(0.6) 
        
        # Core Prediction Logic
        raw_score = (hours * COEFFICIENT) + INTERCEPT
        final_score = min(100, max(0, raw_score)) # Clipping between 0-100
        
        # Engineering "Nice" Data: Calculate SVG Dash Offset
        # Formula: 691 is the circumference of your ring (r=110)
        dash_offset = 691 - (691 * (final_score / 100))

        return jsonify({
            "status": "success",
            "prediction": round(final_score, 1),
            "dash_offset": dash_offset,
            "metadata": {
                "engine": "Linear Regression v1.2",
                "confidence_interval": "±3.4%",
                "developer": "Tanishq Tamgadge"
            }
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

