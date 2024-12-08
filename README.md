### Intensive Foundation in Computer Science and Programming
# Summative 1 - Set Programming Exercises

This guide demonstrates how to test simple Python functions using [`pytest`](https://docs.pytest.org/en/stable/contents.html) in a local setup.

The code in this repository serves as an example, demonstrating how specific tasks are achieved. 

This README follows the steps shown in the video and provides you with a set of easily copyable commands for setting up a local virtual environment.

## Local Setup Instructions

### Step 1: Create a Project Folder

Create a folder for your project where you will keep your Python files and virtual environment.

1. Open your terminal (Command Prompt on Windows, Terminal on macOS/Linux).
2. Use the following commands to create a new folder and navigate into it.

```bash
# Replace "project-folder" with your desired folder name
mkdir project-folder
cd project-folder
```

### Step 2: Set Up a Virtual Environment

#### Windows Setup

1. Make sure you have installed Python 3.7 or higher. You can check your version by running:

```bash
python --version
```


2. Create a virtual environment in your project folder.


```bash
python -m venv venv
```


3. Activate the virtual environment.

```bash
.\venv\Scripts\activate
```


4. Install `pytest` in the virtual environment.

```bash
pip install pytest
```


#### macOS/Linux Setup

1. Make sure you have installed Python 3.7 or higher. Check your version by running:

```bash
python3 --version
```


2. Create a virtual environment in your project folder.


```bash
python3 -m venv venv
```


3. Activate the virtual environment.

```bash
source venv/bin/activate
```


4. Install `pytest` in the virtual environment.

```bash
pip install pytest
```

### Useful Commands

- **Deactivate the virtual environment**:

```bash
deactivate
```


### Step 3: Write and Run Tests

1. Write your test files, typically named `test_<function_name>.py`.
2. Run the tests with `pytest`:

```bash
pytest
```