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
