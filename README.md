# Ejecución de la API de Tareas

1. **Crear y activar entorno virtual:**
   - macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\\venv\\Scripts\\Activate.ps1
     ```
   - Windows (CMD):
     ```bat
     venv\\Scripts\\activate.bat
     ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno:**
   - Duplica el archivo de ejemplo:
     ```bash
     cp .env.example .env   # Windows: copy .env.example .env
     ```
   - Edita `.env` para ajustar tus credenciales de PostgreSQL:
     ```env
     DATABASE_USER=tu_usuario
     DATABASE_PASSWORD=tu_contraseña
     DATABASE_HOST=localhost
     DATABASE_PORT=5432
     DATABASE_NAME=tareasdb
     ```

4. **Inicializar la base de datos:**
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. **Ejecutar la API en modo desarrollo:**
   ```bash
   flask run
   ```

   - Por defecto, estará disponible en `http://127.0.0.1:5000/`.

6. **Probar endpoints:**
   Usa Postman o `curl` para verificar los endpoints:
   ```bash
   curl http://127.0.0.1:5000/tareas
   ```

*¡API lista para usarse!*

