from flask import Flask, request, jsonify, render_template
from deepface import DeepFace
# from flask_cors import CORS
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
# CORS(app)
CORS(app, resources={r"/verify": {"origins": "*"}})
# img_path= "Vedant.jpg"
# next_path="Me.jpg"
img_path= "uploaded_image.jpg"
next_path="uploaded_photo.jpg"

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    try:
        
        img_file = request.files['image']
        photo_file = request.files['photo']
        img_file.save(img_path)
        photo_file.save(next_path)
        
        result = DeepFace.verify(
            img1_path=img_path,
            img2_path=next_path,
        )
        return jsonify(result)
    except Exception as e:
        print("Error occurred:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
