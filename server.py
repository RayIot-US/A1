from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/update', methods=['GET'])
def update():
    ambient_temp = request.args.get('ambient')
    object_temp = request.args.get('object')
    
    if ambient_temp and object_temp:
        print(f"Received Data: Ambient={ambient_temp}°C, Object={object_temp}°C")
        return jsonify({"status": "success", "message": "Data received"})
    
    return jsonify({"status": "error", "message": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
