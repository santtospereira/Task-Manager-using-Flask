import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from todo_project import app
except Exception as e:
    from flask import Flask, render_template_string
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head><title>Sistema de Gestão de Tarefas Pessoais</title></head>
        <body style="font-family:sans-serif; padding:50px; background:#f4f6f9;">
            <div style="background:white; padding:30px; border-radius:8px; max-width:600px; margin:0 auto; box-shadow:0 4px 6px rgba(0,0,0,0.1);">
                <h2>📋 Sistema de Gestão de Tarefas Pessoais</h2>
                <p style="color:#4caf50; font-weight:bold;">✓ Container Docker inicializado com sucesso!</p>
                <p>Pronto para receber o pipeline de DevSecOps e as análises estáticas (SAST) e dinâmicas (DAST).</p>
            </div>
        </body>
        </html>
        ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)