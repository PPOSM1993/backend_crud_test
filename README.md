# Prueba Tecnica de Backend

### Clonar el repositorio

```bash
git clone https://github.com/PPOSM1993/backend_crud_test.git
```

### Entrar al directorio

```bash
cd backend_crud_test
```

### Crear un entorno virtual

```bash
python -m venv env
```

### Ingresar al entorno virtual

```bash
source env/bin/activate  # En Windows usa env\Scripts\activate
```

### Instalar las dependencias

```bash
pip install -r requirements.txt
```

### Ejecutar las migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Ejecutar en el servidor

```bash
python manage.py runserver
```

### Para pruebas de la API

```bash
python manage.py test
```