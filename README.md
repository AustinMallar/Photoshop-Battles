# Photoshop Battles WebApp

A Django web application where users can submit photos to be photoshopped by other users. Photoshops will be voted on to determine the winner.

The publicly available URL for this project is http://add34812.ngrok.io/

## Authors

* **Austin Mallar**
* **Cameron Fisher**
* **Priya Kaira**

# Features

### Account Creation

User can create an account using a username and password. Accounts consist of a user profile image and a biography. It will also track all posts and replies.

### Starting Battles

User's may start a battle by using the button on the navigation menu at the top of the site. Battles require a title and a starting image. At any point a user may delete their post.

### Posting Replies

User's may reply to a battle and add an additional image which other users can like. At any point a user may delete their reply.

### Liking Replies

User's may like a reply to a post. These likes will be tracked for leaderboard purposes. At any point a user unlike a reply.

### Leaderboard

The leader keeps track of the most liked replies and accounts with the highest number of likes.

### Austin-2-factor Authentication Login

Two factor authentication using phone number working.

### OpenStack Structure

The stack name is "Austin" on cisopenstack.ufv.ca. The OpenStack HEAT templates can be found in the production-settings directory in the repository.

The instance stack for this project consists of the following:

### Austin-NGINX-Deploy

The deploy server running NGINX and UWSGI to serve the application. NGROK is used to create a tunnel to a public URL where the project can be accessed.

### Austin-Jenkins

Spins up a Docker container running Jenkins on port 8080.

### Cameron-Ngrok

* ./ngrok authtoken 2DXgSYkoB8Vk7ZmYJfmrs_7SWpCNhZVDzN9hdxqPcUJ

* ./ngrok http 8000


## Example Data

* https://old.reddit.com/r/photoshopbattles/comments/bhab4d/psbattle_cat_through_a_window/
* https://old.reddit.com/r/photoshopbattles/comments/bh3z6u/psbattle_tiger_in_the_snow/
* https://old.reddit.com/r/photoshopbattles/comments/bhahbr/psbattle_this_knight_riding_the_subway/
* https://old.reddit.com/r/photoshopbattles/comments/bh1skh/psbattle_this_woman_spraying_her_yard_for_pests/

