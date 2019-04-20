# Photoshop Battles WebApp

A Django web application where users can submit photos to be photoshopped by other users. Photoshops will be voted on to determine the winner.

The publicly available URL for this project is http://add34812.ngrok.io/

## Authors

* **Austin Mallar**
* **Cameron Fisher**
* **Priya Kaira**

## OpenStack Structure

The stack name is "Austin" on cisopenstack.ufv.ca. The OpenStack HEAT templates can be found in the production-settings directory in the repository.

The instance stack for this project consists of the following:

### Austin-NGINX-Deploy

The deploy server running NGINX and UWSGI to serve the application. NGROK is used to create a tunnel to a public URL where the project can be accessed.

### Austin-Jenkins

Spins up a Docker container running Jenkins on port 8080.

## Ngrok commands used 
./ngrok authtoken 2DXgSYkoB8Vk7ZmYJfmrs_7SWpCNhZVDzN9hdxqPcUJ

./ngrok http 8000