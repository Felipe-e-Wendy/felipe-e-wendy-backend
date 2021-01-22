# felipe-e-wendy.github.io -- backend
The Backend of Felipe and Wendy's wedding website

## Requiriments

- Python 3.8.6

- [Poetry](https://python-poetry.org/) 1.x 

- [MongoDB Atlas](https://www.mongodb.com/cloud/) Database configurated

- [Mercado Pago](https://www.mercadopago.com.br/) Credentials configurated

## How to install 

1. Clone the repository

2. Install the dependecies: 
    ```bash
    $ cd felipe-e-wendy-backend
    $ poetry install
    ```

3. Registre the front-end domain on [Google reCAPTCHA v2](https://www.google.com/recaptcha/) and get the pairs of keys.

4. Set the enviroment variable "SECRET_RECAPTCHAV2" with the server-side secret key.

5. Set the MongoDB Atlas Secrets

    5.1. Set the enviroment variable "MONGODB_USER" as [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) DB User.

    5.2. Set the enviroment variable "MONGODB_PASSWORD" as [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) DB Password.

    5.3. Set the enviroment variable "MONGODB_NAME" as [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) DB name.

6. Set the enviroment variable "MEPAGO_ACCESS_TOKEN" as [Mercado Pago](https://www.mercadopago.com.br/) Access Token.

## How to run
```bash
$ poetry run uvicorn app:app --reload
```

## How to acess the API documentation
http://127.0.0.1:8000/docs