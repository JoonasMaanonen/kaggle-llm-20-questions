import os

from google.cloud import storage

GCS_CLIENT = storage.Client()


def load_model_from_gcs(bucket_name: str, model_id: str):
    model_bucket = GCS_CLIENT.bucket(bucket_name)
    model_blob = model_bucket.blob(f"models/{model_id}.tar.gz")
    model_dir = "../models"
    os.makedirs(model_dir, exist_ok=True)
    model_blob.download_to_filename(f"{model_dir}/{model_id}.tar.gz")
