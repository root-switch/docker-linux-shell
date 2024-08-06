from flask import Flask, request, render_template
import docker
import random

app = Flask(__name__)
client = docker.from_env()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        port = random.randint(20000, 30000)
        container_name = f"{username}_shell"

        
        container = client.containers.run(
            'shell_base',
            name=container_name,
            ports={'22/tcp': port},
            detach=True
        )

        
        exec_command = f'sh -c "echo \'ubuntu:{password}\' | chpasswd"'
        client.containers.get(container_name).exec_run(exec_command, user='root')

        return f"Shell created for {username}. Access it at port {port} with username 'ubuntu'."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
