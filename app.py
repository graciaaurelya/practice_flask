from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'ini adalah halaman utama'

@app.route('/home')
def homePage():
    return render_template ('home.html')

@app.route('/about')
def aboutPage():
    return render_template ('about.html')

@app.route('/contact')
def contactPage():
    return render_template ('contact.html')

# Handling GET request
@app.route('/database', methods=['GET'])
def getDatabase():
    return jsonify({"message": "Halo kamu menggunakan metode get"})

# Handling POST request
@app.route('/database', methods=['POST'])
def postDatabase():
    data = request.json
    return jsonify({"message": "kamu menggunakan metode post"})

# Handling PUT request
@app.route('/database/<int:id>', methods=['PUT'])
def putDatabase(id):
    data = request.json
    return jsonify({"message": f"Data with ID {id} updated", "updated_data": data})

# Handling DELETE request
@app.route('/database/<int:id>', methods=['DELETE'])
def deleteDatabase(id):
    return jsonify({"message": f"Data with ID {id} deleted"})

if __name__ == '__main__':
    app.run(debug=True,port=8888), 