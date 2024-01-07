from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    # Extract the 'code' from the query parameters
    code = request.args.get('code')

    if code:
        # Now you can exchange 'code' for an access token with GitHub
        return f"Received code: {code}"
    else:
        return "No code received", 400
    
@app.route('/<path:path>')
def catch_all(path):
    print(f"Received request to {path}")
    return "Path not found", 404

@app.route('/test')
def test():
    print("Received test request")
    return "Test route works!"

if __name__ == "__main__":
    app.run(port=8000,debug=True)