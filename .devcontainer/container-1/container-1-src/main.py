from backend.backend import backend
from frontend.frontend import frontend
import threading


def main():
  t2 = threading.Thread(target=backend)
  # t1 = threading.Thread(target=frontend)
  
  t2.start()
  # t2.start()
  
  frontend()

if __name__ == "__main__":
  main()