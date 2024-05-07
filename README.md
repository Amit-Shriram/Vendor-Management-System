# Vendor-Management-System

This is a Vendor Management System developed using Django and Django REST Framework.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.x
Django

Installing
1.Clone the repository
2.Create a virtual environment and activate it
3.Install the required dependencies
4.Apply migrations
5.Running the Development Server
Start the Django development server: python manage.py runserver

The project will be accessible at http://127.0.0.1:8000/.

API Endpoints:- 
Vendor List: /api/vendors/ (GET, POST)
Vendor Detail: /api/vendors/<vendor_id>/ (GET, PUT, DELETE)
Purchase Order List: /api/purchase_orders/ (GET, POST)
Purchase Order Detail: /api/purchase_orders/<po_id>/ (GET, PUT, DELETE)

Built With:- 
Django - The web framework in python.
Django REST Framework - A powerful and flexible toolkit for building Web APIs in Django.

Author:-
Amit Shriram
