from flask import Flask, request, jsonify
from deepface import DeepFace

app = Flask(__name__)

@app.route('/face_recognition', methods=['POST'])
def recognize():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image file uploaded.'}), 400
        if 'new' not in request.files:
            return jsonify({'error': 'No image file uploaded.'}), 400
        # Get the files from the POST request
        img_file = request.files['image']
        new_file = request.files['new']


        # Save the images temporarily
        img_path = 'first.jpg'
        new_path = 'second.jpg'
        
        img_file.save(img_path)
        new_file.save(new_path)

        # Perform verification using DeepFace
        result = DeepFace.verify(img1_path=img_path, new1_path=new_path)

        # Delete temporary image files after verification
        # os.remove(img_path1)
        # os.remove(img_path2)

        # Return the result as JSON
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
