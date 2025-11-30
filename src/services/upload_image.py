import uuid
import os
from inference_sdk import InferenceHTTPClient
from src.errors.write_file_error import WriteImageError

class ImageUploader:
    # Tamanho máximo padrão: 10MB (10 * 1024 * 1024 bytes)
    DEFAULT_MAX_FILE_SIZE = 10 * 1024 * 1024

    @classmethod
    def __get_unique_filename_path(cls, filename):
        unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[1]
        return unique_filename

    @classmethod
    def __write_file(cls, filename, file_content, max_size=None):
        # Define o tamanho máximo padrão se não for especificado
        if max_size is None:
            max_size = cls.DEFAULT_MAX_FILE_SIZE
        
        # Valida o tamanho do arquivo antes de escrever
        file_size = len(file_content)
        if file_size > max_size:
            max_size_mb = max_size / (1024 * 1024)
            file_size_mb = file_size / (1024 * 1024)
            raise WriteImageError(
                f"File size ({file_size_mb:.2f} MB) exceeds maximum allowed size ({max_size_mb:.2f} MB)"
            )
        
        unique_filename = cls.__get_unique_filename_path(filename)
        image_path = os.path.join('media', unique_filename)

        try:
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            
            with open(image_path, 'wb') as f:
                f.write(file_content)
        except Exception as e:
            raise WriteImageError(f"Error writing image to folder: {e}")
        else:
            return image_path

    @classmethod
    def get_results_from_image(cls, filename, file_content, min_contour_area, max_file_size=None):
        new_image_path = cls.__write_file(filename, file_content, max_size=max_file_size)
        client = InferenceHTTPClient(
            api_url=os.getenv("ML_SERVER"), api_key=os.getenv("API_KEY")
        )
        result = client.run_workflow(
            workspace_name=os.getenv("MY_WORKSPACE"),
            workflow_id=os.getenv("WORKFLOW_ID"),
            images={"image": new_image_path},
            use_cache=True,
        )
        return len(result[0]["predictions"]["predictions"])