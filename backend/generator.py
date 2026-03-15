def generate_pipeline(req):

    workflow = """
name: Python CI Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:

      - name: Checkout Code
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Tests
        run: pytest
"""

    dockerfile = """
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","main.py"]
"""

    return workflow, dockerfile

if language == "node":
    workflow = """
name: Node CI

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - uses: actions/setup-node@v3
      with:
        node-version: 18

    - run: npm install
    - run: npm test
"""