# Production: debug=False

from app import app


app.run(debug=False, port=8000, host='0.0.0.0')
