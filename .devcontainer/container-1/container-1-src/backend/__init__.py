import logging
import sys

logging.basicConfig(
  stream=sys.stdout,
  format='%(asctime)s %(levelname)-8s %(message)s',
  level=logging.INFO,
  datefmt='%Y-%m-%d %H:%M:%S')
logging.basicConfig(
  stream=sys.stderr,
  format='%(asctime)s %(levelname)-8s %(message)s',
  level=logging.ERROR,
  datefmt='%Y-%m-%d %H:%M:%S')
