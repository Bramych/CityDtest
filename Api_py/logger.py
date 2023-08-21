
import logging
from importlib import import_module

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def log(response, request_body=None):
    logger.info(f"REQUEST METHOD: {response.request.method}")
    logger.info(f"REQUEST URL: {response.url}")
    logger.info(f"REQUEST HEADERS: {response.request.headers}")
    logger.info(f"REQUEST BODY: {request_body}\n")
    logger.info(f"STATUS CODE: {response.status_code}")
    logger.info(f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms\n")
    logger.info(f"RESPONSE HEADERS: {response.headers}")
    logger.info(f"RESPONSE BODY: {response.text}\n.\n.")

def load_json_schema(path: str, json_schema: str = 'schema'):
    """Подгрузка json-схемы из файла"""
    module = import_module(f"schema.{path}")
    return getattr(module, json_schema)