from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST': 
        user = request.form.get('nm')  
        return redirect(url_for('success', name=user))
    elif request.method == 'GET':  
        user = request.args.get('nm')  
        if user:  
            return redirect(url_for('success', name=user))
        else:
            
            return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
