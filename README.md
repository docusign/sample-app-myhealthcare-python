# Python and React: MyHealthcare Sample Application

### Github repo: MyHealthcareApp

## Introduction
MyHealthcare sample application written in Python 3.7 Django DRF (server) and React (client). You can find a live instance running at [https://myhealthcare.sampleapps.docusign.com/](https://myhealthcare.sampleapps.docusign.com/).

MyHealthcare demonstrates the following:

1. Authentication with DocuSign via [JSON Web Token (JWT) Grant](https://developers.docusign.com/esign-rest-api/guides/authentication/oauth2-jsonwebtoken)
2. **Request Medical Records:**
   This will enable the user to request medical records through the website. The user will be sent an email to electronically sign a medical release form. Users will verify identity using IDV and sign the document.
   * Remote signing
   * Templates
   * IDV (recipient authentication)
3. **COVID-19 Consent Form.**
   This will enable users to give consent for a COVID-19 vaccine through the website. The user should be taken to a form where they input their name, phone number, and email address. After submitting the form they should receive an envelope via SMS delivery to sign a consent form that is pre-filled with form data.
   * SMS Delivery
   * Templates
   * Data Entry Tabs
   * Anchor positioning
4. **Purchase a new insurance policy.**
   This will enable users to apply for an assistance program through the website. Users will use embedded signing to fill out an application for an assistance program. As required by the example application, users will be able to upload identification and proof of income documents as an optional attachment.
   * Embedded Signing
   * Templates
   * Signer Attachment tab

## Installation

### Prerequisites
* A DocuSign Developer account (email and password) on [demo.docusign.net](https://demo.docusign.net). If you don't already have a developer account, create a [free account](https://go.docusign.com/sandbox/productshot/?elqCampaignId=16535).
* A DocuSign integration key (a client ID) that is configured to use **JSON Web Token (JWT) Grant**.
   You will need the **integration key** itself and its **RSA key pair**. To use this application, you must add your application's **Redirect URI** to your integration key. This [**video**](https://www.youtube.com/watch?v=GgDqa7-L0yo) demonstrates how to create an integration key (client ID) for a user application like this example.
* [Python 3.7+](https://www.python.org/downloads/)
* The Python [venv](https://docs.python.org/3/library/venv.html#module-venv) module
* [Node.js](https://nodejs.org/) v10+

### Required environment variables

For the application to work correctly, you must have 2 .env files and a private key file:
- 1st env file is located in the root folder of the application.
- 2nd env file is in the frontend folder.
Change the name .env_example to .env and add the correct variable values to these files

The example_private.key file is located in the backend folder. Replace the contents of the file with your private key and rename the file to private.key

* **DS_CLIENT_ID** - The integration key is the same as the client ID
* **DS_CLIENT_SECRET** - Integration Secret Key
* **DS_IMPERSONATED_USER_GUID** - API account ID
* **DS_TARGET_ACCOUNT_ID** - Target account ID. Use FALSE to indicate the user's default
* **REACT_APP_DS_RETURN_URL** - URL where the back end of the application is located (If you run it locally, use `http://localhost:3000`)
* **REACT_APP_API_BASE_URL** - URL where the front end of the application is located; will be used by Docusign to redirect back after signing ceremony (If you run it locally, use `http://localhost:5001/api`)
* **DS_AUTH_SERVER** - The DocuSign authentication server (for testing purposes, use `https://account-d.docusign.com`)
* **DS_DEMO_SERVER** - Link to the DocuSign demo server (for testing purposes, use `https://demo.docusign.net`)
* **DJANGO_SECRET** - Your Django secret key
* **BACKEND_ALLOWED_HOSTS** - URL of your server

### Installation steps

**Manual**

1. Download or clone this repository to your workstation in a new folder named **sample-app-myhealthcare-python**.
2. Navigate to that folder: **`cd sample-app-myhealthcare-python`**
3. Navigate to backend folder: **`cd backend`**
4. Upgrade pip: **`pip3 install --upgrade pip`**
5. Install python packages: **`pip3 install -r requirements.txt`**
6. Navigate to frontend folder: **`cd frontend`**
7. Install React dependencies using the [npm](https://www.npmjs.com/) package manager:  **npm install**
8. Update the **.env** file with the integration key and other settings.
    > **Note:** Protect your integration key and client secret. You should make sure that the **.env** file will not be stored in your source code repository.

**Using installation scripts**

1. Download or clone this repository to your workstation in a new folder named **sample-app-myhealthcare-python**.
2. Navigate to that folder:**`cd sample-app-myhealthcare-python`**
3. Make the installation script executable: **`chmod +x scripts/install.sh`**
4. Run the installation script: **`./scripts/install.sh`**
5. Update the **.env** file with the integration key and other settings.
    > **Note:** Protect your integration key and client secret. You should make sure that the **.env** file will not be stored in your source code repository.

### Additional installation scripts
All installation scripts are located in the **scripts** folder.
1. Make the installation script executable: **`chmod +x scripts/stop.sh`**
2. To stop the application, run **`./scripts/stop.sh`**
3. Make the installation script executable: **`chmod +x scripts/clean.sh`**
4. To remove the virtual environment and modules, run **`./scripts/clean.sh`**

## Running MyHealthcare

### Manual

1. Navigate to the application folder: **`cd sample-app-myhealthcare-python`**
2. Navigate to the backend folder: **`cd backend`**
3. Run the application: **`python3 manage.py runserver localhost:5001`**
4. Navigate to frontend folder: **`cd ../frontend`**
5. Run npm: **`npm start`**
6. Open a browser to **http://localhost:3000**

### Using scripts:
1. Navigate to the application folder: **`cd sample-app-myhealthcare-python`**
2. Make the script executable: **`chmod +x scripts/run.sh`**
3. run **`./scripts/run.sh`**

### Using Docker:
1. **`cd sample-app-myhealthcare-python`**
2. **`cd backend`**
3. **`docker build -t backend:latest .`**
4. **`cd ..`**
5. **`docker run --env-file=.env -d -p 5001:5001 backend:latest`**
6. **`cd frontend`**
7. **`docker build -t frontend:latest .`**
8. **`docker run --env-file=.env -d -p 3000:3000 frontend:latest`**
9. **`cd ..`**
10. Open a browser to **http://localhost:3000**

#### To stop running processes in docker:
1. docker stop <backend_container_id>
2. docker stop <frontend_container_id>

## License information
This repository uses the MIT License. See the [LICENSE](./LICENSE) file for more information.
