# py-back-end

## Starting the server

### Installing a virtual environment

To avoid installing dependencies on the system, install a virtual environment

1. Create a virtual environment:
   ```sh
   john@doe:~$ python3 -m venv env # 'env' virtual environment name
   ```

2. Activate the virtual environment:
   ```sh
   john@doe:~$ source ./env/bin/activate
   ```

### Installing dependencies

1. Install __poetry__ if not installed:
   ```sh
   john@doe:~$ pip install poetry
   ```

2. Install dependencies:
   ```sh
   john@doe:~$ poetry install
   ```

### Starting the server

- In the __app__ directory, run the command:
```sh
john@doe:~$ uvicorn api:app --reload
```

- Or run the __start__ script:
```sh
john@doe:~$ ./start
```