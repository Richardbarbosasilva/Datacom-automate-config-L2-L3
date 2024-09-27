from flask import Flask, render_template, request, jsonify


app = Flask(__name__, static_folder="static")  # Specify the static folder

@app.route('/', methods=['GET', 'POST'])
def form_page():
  if request.method == 'POST':
    # Extract user input from form data (replace with your field names)
    user_name = request.form['user_name']
    script_type = request.form['script_type']

    # Process user input and generate script content
    script_content = f"This script is for {user_name} and uses script type: {script_type}"

    # Implement log generation here (optional)

    # Prepare response data
    response = {'message': 'Script generated!', 'script': script_content}
    return jsonify(response)
  else:
    return render_template('dm4370EDDmetroscript.html')  # Replace with your form template

@app.route('/script_page')
def show_script():
  return render_template('dm4370EDDmetroscript.html')  # Replace with your script template

if __name__ == '__main__':
  app.run(debug=True)



  
