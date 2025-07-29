from pathlib import Path

def create_directories_and_files(output_dir: str):
    """
    Crea la estructura de carpetas dentro del directorio dado y archivos con código.
    """
    # Convertir la ruta base en un objeto Path (Aseguramos que apunta al directorio principal)
    base_path = Path(__file__).resolve().parent  # Esto apunta al directorio que contiene `generator.py`
    
    # Definir las subcarpetas dentro de 'app'
    subdirs = ['api', 'core', 'domain', 'infrastructure', 'schemas']
    
    # Crear el directorio 'app' si no existe
    app_dir = base_path / 'app'
    app_dir.mkdir(parents=True, exist_ok=True)
    print(f"Carpeta 'app' creada en: {app_dir}")
    
    # Crear las subcarpetas y archivos dentro de 'app'
    for dir_name in subdirs:
        # Ruta completa para cada subcarpeta
        dir_path = app_dir / dir_name
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Carpeta '{dir_name}' creada en: {dir_path}")
        
        # Definir los archivos y su contenido según las plantillas
        if dir_name == 'api':
            create_file(dir_path, '__init__.py')
            create_file(dir_path, 'email_controller.py', template_file=base_path / 'templates' / 'email_controller_template.py')
        elif dir_name == 'core':
            create_file(dir_path, '__init__.py')
            create_file(dir_path, 'config.py', template_file=base_path / 'templates' / 'config_template.py')  
        elif dir_name == 'domain':
            create_file(dir_path, '__init__.py')
            create_file(dir_path, 'models.py', template_file=base_path / 'templates' / 'models_template.py')  # Plantilla para models.py
            create_file(dir_path, 'services.py', template_file=base_path / 'templates' / 'services_template.py')  # Plantilla para services.py
        elif dir_name == 'infrastructure':
            create_file(dir_path, '__init__.py')
            create_file(dir_path, 'resend_client.py', template_file=base_path / 'templates' / 'resend_client.py')
        elif dir_name == 'schemas':
            create_file(dir_path, '__init__.py')
            create_file(dir_path, 'email_schema.py', template_file=base_path / 'templates' / 'email_schema_template.py')


def create_file(directory: Path, filename: str, template_file: Path = None):
    """
    Crea un archivo con contenido dado en el directorio especificado.
    
    :param directory: El directorio donde se creará el archivo.
    :param filename: El nombre del archivo a crear.
    :param template_file: El archivo de plantilla con el contenido a copiar (opcional).
    """
    # Ruta completa del archivo a crear
    file_path = directory / filename
    
    # Si se proporciona un archivo de plantilla, lo leemos y usamos su contenido
    if template_file:
        with open(template_file, 'r') as template:
            content = template.read()
    else:
        content = ""  # Si no se proporciona plantilla, dejamos el contenido vacío

    # Crear y escribir en el archivo
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Archivo '{filename}' creado en: {file_path}")


# Ejemplo de uso
create_directories_and_files('./rapid-mailer')  # Asegúrate de pasar el path correcto
