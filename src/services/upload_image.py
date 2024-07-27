#from google.cloud import storage
#from src.db.config.base import BUCKET_NAME
import uuid
import os
import cv2 as cv

from errors.write_file_error import WriteImageError

class ImageUploader:

    @classmethod
    def __get_unique_filename_path(cls, filename):
        unique_filename = str(uuid.uuid4()) + os.path.splitext(filename)[1]
        return unique_filename

    @classmethod
    def __write_file(cls, filename, file_content):
        unique_filename = cls.__get_unique_filename_path(filename)
        image_path = os.path.join('media', unique_filename)

        try:
            with open(image_path, 'wb') as f:
                f.write(file_content)
        except Exception as e:
            raise WriteImageError(f"Error writing image to folder: {e}")
        else:
            return image_path

    @classmethod
    def __process(cls, path, min_contour_area):
        image = cv.imread(path)
        hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
        white_mask = cv.inRange(hsv, (0,0, 180), (172,111,255))
        contours, _ = cv.findContours(white_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        filtered_contours = [cnt for cnt in contours if cv.contourArea(cnt) > min_contour_area]
        cattle_count = len(filtered_contours)
        return cattle_count

    @classmethod
    def get_results_from_image(cls, filename, file_content, min_contour_area):
        new_image_path = cls.__write_file(filename, file_content)
        results = cls.__process(new_image_path, min_contour_area)
        return results

    """ @classmethod
    def send_to_bucket(cls, file_path, unique_filename):
        ""Not implemented""
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(unique_filename)

        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_path} to {cls.GCS_BUCKET_NAME} as {unique_filename}") """