import os
from flask import *
from groq import Groq

app = Flask(__name__)
client = Groq(api_key = os.environ.get("GROQ_API_KEY"))

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI System Health Monitor</title>
    <style>
        body { font-family: sans-serif; margin: 40px; line-height: 1.6; }
        textarea { width: 100%; padding: 10px; border-radius: 5px; }
        button { background: #0078d4; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; }
        .result-box { background: #f4f4f4; padding: 20px; border-left: 5px solid #0078d4; margin-top: 20px; white-space: pre-wrap; }
    </style>
</head>
<body>
    <h1>AI Log Analyzer</h1>
    <p>Anomaly detection using<strong>Groq</strong></p>
    <form method="POST">
        <textarea name="logs" rows="8" placeholder="Paste your system logs here..."></textarea><br><br>
        <button type="submit">Analyze</button>
    </form>
    {% if result %}
    <div class="result-box">
        <h3>Analysis Result:</h3>
        {{ result }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET" ,"POST"])
def index():
	result = None
	if request.method == 'POST':
		user_logs = request.form.get("logs")
		system_prompt = (
			"You are a Senior DevOps and Security Engineer. Analyze the following logs "
			"for: 1) Critical Errors, 2) Security Vulnerabilities (unauthorized access), "
			"and 3) Performance warnings. Provide a concise bullet-pointed 'Health Score' "
			"and recommendation."
		)
		try:
			chat_completion = client.chat.completions.create(
				messages=[
					{
						"role": "user",
						"content": f"Analyze these application logs for anomalies or security risks. Be concise: {user_logs}",
					}
				],
				model="llama-3.3-70b-versatile",
			)
			result = chat_completion.choices[0].message.content
		except Exception as e:
			result = f"Error connecting to Groq: {str(e)}"
	
	return render_template_string(HTML_TEMPLATE,result = result)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
