from flask import Flask, redirect, url_for, request, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Route untuk halaman sukses yang menerima parameter 'name' dari URL
@app.route('/success/<name>')
def success(name):
    return f'Welcome {name}!'  # Menampilkan pesan selamat datang dengan nama pengguna

# Route untuk halaman login dengan metode POST dan GET
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':  # Jika metode permintaan adalah POST
        user = request.form.get('nm')  # Ambil data dari form dengan nama 'nm'
        return redirect(url_for('success', name=user))  # Redirect ke fungsi 'success' dengan parameter 'name'
    elif request.method == 'GET':  # Jika metode permintaan adalah GET
        user = request.args.get('nm')  # Ambil parameter 'nm' dari URL
        if user:  # Jika parameter 'nm' tersedia
            return redirect(url_for('success', name=user))  # Redirect ke fungsi 'success' dengan parameter 'name'
        else:
            return render_template('login.html')  # Tampilkan halaman login jika parameter 'nm' tidak ada

# Jalankan aplikasi dalam mode debug
if __name__ == '__main__':
    app.run(debug=True)
