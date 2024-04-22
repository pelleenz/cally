from backend.backend import backend
from frontend.frontend import frontend
import asyncio


def main():
  backend()
  frontend()

if __name__ == "__main__":
  main()