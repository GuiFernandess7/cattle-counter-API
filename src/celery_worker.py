import os
from celery import Celery
from dotenv import load_dotenv
from src.services.upload_image import ImageUploader
from src.errors.write_file_error import WriteImageError

load_dotenv(".env")

app = Celery(__name__)
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND")

@app.task(name="upload_image")
def upload_image_task(filename, file_content, min_contour_area=100, max_file_size=None):
    """
    Processa o upload de imagem e retorna o resultado da contagem.
    
    Args:
        filename: Nome do arquivo de imagem
        file_content: Conteúdo binário do arquivo
        min_contour_area: Área mínima do contorno (padrão: 100)
        max_file_size: Tamanho máximo do arquivo em bytes (opcional, usa padrão de 10MB se None)
    
    Returns:
        dict: Dicionário com mensagem e resultado da contagem
    """
    try:
        # Obtém o tamanho máximo da variável de ambiente se não foi passado
        if max_file_size is None:
            max_file_size_env = os.getenv("MAX_FILE_SIZE")
            if max_file_size_env:
                max_file_size = int(max_file_size_env)
        
        # Processa a imagem e obtém o resultado
        count = ImageUploader.get_results_from_image(
            filename=filename,
            file_content=file_content,
            min_contour_area=min_contour_area,
            max_file_size=max_file_size
        )
        
        return {
            "message": "Image processed successfully",
            "count": count,
            "filename": filename
        }
    except WriteImageError as e:
        # Re-raise para que o Celery capture o erro corretamente
        raise e
    except Exception as e:
        # Captura outros erros e os relança como WriteImageError para consistência
        raise WriteImageError(f"Error processing image: {str(e)}")