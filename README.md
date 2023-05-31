# Django_shop_app
ShopApp using Python and Django
# Shop Locator App

The Shop Locator App is a Django-based web application that allows users to store and query location details of different types of shops based on latitude and longitude coordinates. It provides functionalities to create, update, delete, and find shops within a specified radius from a given location.

## Features

- Store location details of different types of shops
- Perform queries to find shops within a specified radius from a given location
- Create, update, and delete shop entries

## Technologies Used

- Python
- Django
- HTML
- CSS
- Django Template Language (DTL)
- Bootstrap

## Installation

1. Install Python (version X.X.X) from the official Python website: https://www.python.org/downloads/
2. Install Django by running the following command:
pip install django
## Setup

1. Clone the repository to your local machine.
2. Navigate to the project directory.

## Database Setup

1. Run the following commands to create and apply database migrations:
python manage.py makemigrations
python manage.py migrate
## Running the App

1. Start the development server by running the following command:
python manage.py runserver
2. Access the app in your web browser at http://localhost:8000/

## Configuration

1. In the `settings.py` file, add the name of the app (`shop_locator`) to the `INSTALLED_APPS` list.

## Usage

1. Create a new shop entry:
- Visit the homepage and click on the "Create Shop" button.
- Fill in the required details, including the shop's name, address, contact information, and description.
- Click "Save" to create the shop entry.

2. Update a shop entry:
- On the homepage, find the shop you want to update and click on the "Edit" button.
- Modify the shop details as needed and click "Save" to update the entry.

3. Delete a shop entry:
- On the homepage, find the shop you want to delete and click on the "Delete" button.
- Confirm the deletion when prompted.

4. Query shops within a specified radius:
- Click on the "Query Shops" button on the homepage.
- Enter the latitude, longitude, and distance in kilometers.
- Click "Submit" to see the list of shops within the specified radius.

## Known Issues

- No known issues at the moment.

## Future Development

- Add user authentication and authorization for managing shop entries.
- Improve the user interface and design.
- Implement additional search and filtering options.

## Contributing

- Contributions are welcome! If you'd like to contribute to the project, please follow these guidelines:
- Fork the repository and create a new branch.
- Make your changes and submit a pull request.
- Ensure that your code follows the project's coding conventions and passes all tests.


Deployment Process
To deploy the Shop Locator App to a live server using Railway.app, follow the steps below:

Make sure you have generated the requirements.txt file by running the following command:
$ pip freeze > requirements.txt
Create a Procfile file in the root directory of your project and add the following line:
web: gunicorn 'name-of-application.wsgi'
Create a Procfile file in the root directory of your project and add the following line:
web: gunicorn 'name-of-application.wsgi'
Replace 'name-of-application' with the actual name of your Django application.

Create a runtime.txt file in the root directory of your project and add the following line:
python-3.10.2
Replace 3.10.2 with the version of Python you are using for your project.

Open the settings.py file in your project and locate the ALLOWED_HOSTS variable. Update it to the following:
ALLOWED_HOSTS = ['*']
This allows any host to access your application. Make sure to configure the ALLOWED_HOSTS list with appropriate domain names or IP addresses for production deployment.

Add the following line to the settings.py file to configure the STATIC_ROOT directory:
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
This sets the directory where Django will collect static files.
Run the following command to collect the static files:
$ python manage.py collectstatic
This will gather all the static files into the STATIC_ROOT directory.

Commit and push all the changes to your GitHub repository.

Sign up or log in to Railway.app at https://railway.app/.

Click on the '+New' button to create a new project.

Select 'GitHub Repo' as the deployment method.

Choose the repository where you pushed the code.

After selecting the repository, go to the project settings tab.

Under the domain section, click on 'Generate Domain' to obtain a domain for your deployed application.

Optionally, you can update the domain name to a custom one if desired.

Your Shop Locator App is now live and accessible at the provided domain.

Please make sure to replace 'name-of-application' with the actual name of your Django application and adjust other placeholders with relevant values as per your project setup.
