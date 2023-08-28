from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Edsontorres12@'
app.config['MYSQL_DB'] = 'first_flask'
mysql = MySQL(app)

@app.route('/')
def leer_todo():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios')
    usuarios = cur.fetchall()
    cur.close()
    return render_template('leer.html', usuarios=usuarios)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (nombre, email) VALUES (%s, %s)', (nombre, email))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('leer_todo'))
    return render_template('crear.html')

if __name__ == '__main__':
    app.run(debug=True)
