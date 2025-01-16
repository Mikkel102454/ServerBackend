from flask import Flask, send_from_directory, request, jsonify
app = Flask(__name__)
@app.route('/')
def GetIndexHTML():
    return send_from_directory("html-files", "index.html")

@app.route('/<path:filename>')
def GetCSSFiles(filename):
    return send_from_directory("html-files", filename)


@app.route('/exchange', methods=['POST'])
def HandleExcahnge():
    data = request.json
    if data.get('handleCode') is None:
        return jsonify({"status": "failure", "exitCode": 400})
    
    
    # Dosnt require login token

    handleCode = data.get('handleCode')

            


if __name__ == '__main__':
    app.run(debug=True)