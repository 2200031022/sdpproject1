from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Dummy user data (replace this with a database in a real application)
users = {
    'john_doe': {'username': 'john_doe', 'password': 'password123', 'role': 'faculty'},
    'jane_smith': {'username': 'jane_smith', 'password': 'studentpass', 'role': 'student'},
}

# User class for Flask-Login
class User(UserMixin):
    def __init__(self, user_id, role):
        self.id = user_id
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    user_data = users.get(user_id)
    if user_data:
        return User(user_id, user_data['role'])
    return None

@app.route('/login/<username>/<password>')
def login(username, password):
    user = users.get(username)

    if user and user['password'] == password:
        user_obj = User(username, user['role'])
        login_user(user_obj)
        return redirect(url_for('profile'))

    return "Invalid credentials"

@app.route('/profile')
@login_required
def profile():
    role = current_user.role
    if role == 'faculty':
        return render_template('faculty_profile.html')
    elif role == 'student':
        return render_template('student_profile.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
