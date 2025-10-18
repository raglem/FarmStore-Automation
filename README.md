# Farmstore Automation Project

## Setup Instructions

This quick program uses Playwright to order a few items on the Cal Poly Pomona Farm Store website.
With Django, I've exposed an API route to return the total price of these order items.
To set up the project, follow these steps. It is assumed python is already installed

1. **Clone repository**
    ```bash
    git clone
    ```

2. **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

After setting up the environment and installing the dependencies, you can run the project as needed.
You can ignore instructions to migrate. 

```bash
    python manage.py runserver
```

Open another terminal window and execute the following command. This calls the api route to run the automated order and return the total price. 

```bash
    curl http://127.0.0.1:8000/
```