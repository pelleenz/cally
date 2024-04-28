from backend.backend import backend
from frontend.frontend import frontend
import threading
import config


def main():
  t2 = threading.Thread(target=backend).start()
  frontend()

if __name__ == "__main__":
  main()