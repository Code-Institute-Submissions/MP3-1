# Coins Catalog

## Data Centric Development Milestone Project.

![Mockup](md_data/mockup/mockup.png)

Coins Catalog is a website where community can share their collections to other members and to the public. All users can search through dataset provided by a community members. Registered users can create, edit or delete their own dataset.

This project is for educational purposes only.

## [View live website](https://coinscatalog.herokuapp.com/)
___
# Table of contents

- [UX](#ux)
    - [Strategy](#strategy)
    - [Scope](#scope)
        - [User stories](#user-stories)
    - [Structure of the website](#structure-of-the-website)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Features](#features)
- [Technologies used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

___
# UX

## Strategy

The purpose of this project is to build a website that presents a catalog of bullion coins. Content is accessible for free for everyone and can be extended by registered members.

## Scope

A MVP (minimum viable product) includes:
- coins catalog
- landing page with a search option
- opportunity to create, edit and delete data by the user
- registration and login pages
- contact page

### User stories

As a new user:
- I would like to search coins catalog.
- I would like to be able to access all catalog data.
- I would like to register easily and login immediately after registration.

As a returning user:
- I would like to login and view details on my account.
- I would like to add a new coin to the database.
- I would like to edit my coin data in a database.
- I would like to delete my coin from a database.
- I would like to see a confirmation message on every action I take on the website.

As a site administrator:
- I would like to have a control of all data on the website database.
- I would like to have a control of all coin types.
- I would like to allow users to send a message to website administrator.

## Structure of the website

Website contains:
- fixed navigation bar or burger icon on mobile devices with essential links to navigate on the website
- a footer with contact option available all the time
- main content site which changes on every action taken by a user.

## Skeleton

### Wireframes

- Landing Page

    <details><summary>Desktop (click to view)</summary>

    ![](md_data/wireframes/desktop_landing_page.png)
    </details>
    <details><summary>Mobile (click to view)</summary>
    
    ![](md_data/wireframes/mobile_landing_page.png)
    </details>
- All Coins Page

    <details><summary>Desktop (click to view)</summary>

    ![](md_data/wireframes/desktop_all_coins_page.png)
    </details>
    <details><summary>Mobile (click to view)</summary>
    
    ![](md_data/wireframes/mobile_all_coins_page.png)
    </details>
- Add Coin Page

    <details><summary>Desktop (click to view)</summary>

    ![](md_data/wireframes/desktop_add_coin_page.png)
    </details>
    <details><summary>Mobile (click to view)</summary>
    
    ![](md_data/wireframes/mobile_add_coin_page.png)
    </details>
- Register Page

    <details><summary>Desktop (click to view)</summary>

    ![](md_data/wireframes/desktop_register.png)
    </details>
    <details><summary>Mobile (click to view)</summary>
    
    ![](md_data/wireframes/mobile_register.png)
    </details>
- Login Page

    <details><summary>Desktop (click to view)</summary>

    ![](md_data/wireframes/desktop_login.png)
    </details>

    <details><summary>Mobile (click to view)</summary>
    
    ![](md_data/wireframes/mobile_login.png)
    </details>

### Divergence final website look from wireframes

- Landing Page
    
    On landing page I decided to add 2 sections below search option:
        
    - A counter to display number of users registered on the website.
    - Join our community section for users that are not logged in.

- All Coins Page

    I decided to display images on the left hand side and description on the right hand side.
    This approach does not distract a user.

- Add Coin Page

    - Extra field for a year.
    - For a weight there is a drop down list for a weight unit.
    - For a country there is a drop down list available with fixed set of countries.
    - There is a Reset button instead of Cancel button.

- Register Page

    - There is a wide Register button instead of Sign up and Cancel buttons.
 
 - Login Page

    - Same as on the register page there is a wide Log in button instead of Sign in button.

### Database schema

Database contains 3 tables (collections):
- Coin
- Coin type
- User

The fields for each table can be found in the image below:

<details><summary>Database (click to view)</summary>

![](md_data/database/database_tables.png)
</details>

## Surface

### Colors

Colours used in a project:
Purpose | Colour value
------------ | -------------
background | #b0bec5 
content background | #2e2e2e
flash messages background | #4285f4
main font | #ffc107
navigation and footer font | #ffffff
link | #696969
hoover | #ffc107
login, register, email buttons | #ffa000
add coin, show/hide coins  buttons | #616161
edit button | #59698d
delete button | #78909c

### Fonts

* As a main font I used sans-serif.

### Images

I used images from:

*  [unsplash.com](https://www.unsplash.com) and it is credited in [credits](#credits) section.

*  [tavex.pl](https://www.tavex.pl) and it is credited in [credits](#credits) section.

[Back to Table of contents](#table-of-contents)
___
# Features

This project consist base.html page as a skeleton. It is divided into 4 parts:
- Header which contains navigation bar
- Section where flash messages are displayed
- Main section for all files other then base.html
- Footer with contact button

## Navigation bar

Navigation bar is located on the top of the website. It is responsive and changes to coins icon on mobile devices.
Brand logo is located in the top left corner. It is a link and it always redirect user to the home page.
Page links are in the top right corner.

Users who are on the website for the first time and are not logged in can see following options: 
- Home
- Catalog
- Log in
- Register

![](md_data/features/navbar.png)

For logged in users:
- Home
- Catalog
- New Coin
- Profile
- Log Out

![](md_data/features/navbar_user.png)

For administrator who is logged in there are the same options as for a logged in user.
Additionally, there is an Admin options button available. It contains two links:
- Coin Types
- Add new Type

![](md_data/features/navbar_admin.png)

## Footer

Footer has a copyright information and contact us button.
After clicking the button user is redirected to contact us site.

![](md_data/features/footer.png)

## Sites

### Home

Site contains 3 sections:
- Search bar where user can search a coin by their name or description
- Counter with total number of users and total number of records in database
- Join our community which is displayed for unregistered users only

<details><summary>Home (click to view)</summary>

![](md_data/features/home.png)
</details>

### Catalog

Site displays all coins from database. I used pagination and it is visible at the bottom of the page. 

<details><summary>Catalog (click to view)</summary>

![](md_data/features/catalog.png)
</details>

### Log In

Here user can login to the account. After that site redirects user to the profile page.
Below the login button there is a link to register page.

<details><summary>Log In (click to view)</summary>

![](md_data/features/log_in.png)
</details>

### Register

Register is the place where user can create an account.
Login link is available below the Register button.

<details><summary>Register (click to view)</summary>

![](md_data/features/register.png)
</details>

### New Coin

On this site user can add a new coin. All of the fields have to be filled out.
Add coin button validates the form and redirects the user to the profile page.
Reset button resets all data in the form.

<details><summary>Add new coin (click to view)</summary>

![](md_data/features/add_new_coin.png)
</details>

### Profile

User can see account details on the profile page.
User's coin collection can be displayed under show coins button.
Also Edit and Delete options are available here.

<details><summary>Profile (click to view)</summary>

![](md_data/features/profile.png)
</details>

### Log Out

Log Out button ends the session and redirects user to the home page.

<details><summary>Log Out (click to view)</summary>

![](md_data/features/log_out.png)
</details>

### Coin Types

This is an administrator option only. Administrator can view, edit or delete coin type here.

<details><summary>Coin Types (click to view)</summary>

![](md_data/features/coin_types.png)
</details>

### Add new Type

This is an administrator option only. Administrator can add new coin type here.

<details><summary>Add new Type (click to view)</summary>

![](md_data/features/add_new_coin_type.png)
</details>

### Catalog - administrator option

This is an administrator option only. Administrator can edit or delete user's coins.

<details><summary>Catalog (click to view)</summary>

![](md_data/features/catalog_admin_option.png)
</details>

### Contact Us

Contact us page is always accessible from a footer. Name and email fields are filled out for logged in users.

<details><summary>Contact Us (click to view)</summary>

![](md_data/features/contact_us.png)
</details>

### Error page

Custom error 404 and error 500 page.

<details><summary>Error page (click to view)</summary>

![](md_data/features/error_page.png)
</details>

### Possible future implementations:

- Add administrator dashboard
- Add option to edit or delete user account
- Add pagination for search option
- Add sort option in a catalog

[Back to Table of contents](#table-of-contents)
___
# Technologies used

### HTML5
* As a structure language.

### CSS
* As a style language.

### Javascript
* As a front-end programming language.

### Python 3.8.7
* As a back-end programming language.

### Bootstrap 
* Bootstrap@4.5.3 as a CSS framework.

### MDBootstrap CSS 
* MDBootstrap@4.19.1 as a CSS framework.

### jQuery 
* jQuery@3.5.1 as a JavaScript library.

### Email.js
* As a Javascript library

### Flask
* As a web framework for the Python.

### Jinja
* As a web template engine for the Python.

### MongoDB:
* As a NoSQL database.

### PyMongo
* As a communicate between Python and MongoDB.

### Font Awesome
* Font Awesome@5.15.2 as an icon library.

### GitHub
* As a software hosting platform to keep project in a remote location.

### Git
* As a version-control system tracking.

### Gitpod
* As a development hosting platform.

### Heroku
* As a cloud-based hosting platform.

### Wireframe.cc
* As a wireframing tool.

### GNU Image Manipulation Program [GIMP]
* As an image editor.

[Back to Table of contents](#table-of-contents)
___
# Testing

### Testing section is located in [TEST.md](https://github.com/marcin-kli/MP3/blob/Milestone-Projects/test.md) file.
___
# Deployment

This project was deployed to Heroku. I used Gitpod as a development environment where I commited all changes to git version control system.
I used push command in Gitpod to save changes into GitHub.
Then connected my GitHub account to Heroku and set up `Automatic deployment` in Heroku under `Deploy` section in my coinscatalog app.

![](md_data/deployment/deployment_method.png)
![](md_data/deployment/deployment_method_2.png)

To run this project follow below steps:

MongoDb:
* Setup MongoDB account [help here](https://docs.mongodb.com/guides/cloud/account/)
* Setup atlas [help here](https://docs.atlas.mongodb.com/getting-started/)
* Create a cluster [help here](https://docs.atlas.mongodb.com/cluster-configuration/)
* In a cluster create new Database `coins_catalog` and add 3 collections:
    coins, coin_types, users.
 
 ![](md_data/deployment/create_database.png)

Github:

* Create an account and Log in to GitHub, then go to [MP3](https://github.com/marcin-kli/MP3) and click on repository to download
* Select `Code` and click `Download the ZIP file`
* After download you can extract the file and use it in your local environment or upload to your GitHub account
* Alternatively you can [Clone](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
or [Fork](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo)
this repository ([MP3](https://github.com/marcin-kli/MP3)) into your github account
* Run a repository directly from your GitHub repository through Gitpod button.

Gitpod:

* Create env.py file
* Add env.py file to gitignore
* Add details to env.py file:

        import os
        
        os.environ.setdefault("IP", "0.0.0.0")
        os.environ.setdefault("PORT", "5000")
        os.environ.setdefault("SECRET_KEY", "YOURSECRETKEY")
        os.environ.setdefault("MONGO_URI", "mongodb+srv://root:YOURPASSWORD@YOUR-CLUSTER-NAME.mongodb.net/YOUR-DATABASE-NAME?retryWrites=true&w=majority")
        os.environ.setdefault("MONGO_DBNAME", "YOUR-DATABASE-NAME")

* In terminal window create a requirements.txt file by typing pip3 freeze --local > requirements.txt
* In terminal window create a Procfile by typing python app.py > Procfile
* In terminal window add files, commit and push changes to Github

Deploy a project to Heroku: 

* Create an account and Log in to Heroku
* From dashboard click `new` > `create new app`
* Add a unique name in `App name` field
* When connected go to `settings` > `Config Vars` and add key and value pairs.
  Variables shoud be the same as in the env.py file
* From `Deploy` go to `Automatic deployment` and connect `Connect to  GitHub` section, then select github username and repository name
* Heroku will receive all settings from your Github repository. Please wait for a message `your app was successfully deployed`
* Click `Open App` from top right corner to view the app in a new window.

[Back to Table of contents](#table-of-contents)
___
# Credits

* To complete this project I used Code Institute student template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template)

* Task Manager project from the Data Centric module.

* Ideas and knowledge library:

    * [w3schools.com](https://www.w3schools.com)
    * [Jinja - Template Designer Documentation](https://jinja.palletsprojects.com/en/2.10.x/templates/)
    * [Material Design Blocks](https://mdbootstrap.com/docs/b4/jquery/design-blocks/)

* How to connect MongoDB with Flask using Pymongo And Crud Operation with mongoDB [manual](https://medium.com/@sagarvermaitdeveloper/how-to-connect-mongodb-with-flask-using-pymongo-612f2bfbc95)

### Code:

* [modal](https://mdbootstrap.com/docs/b4/jquery/modals/additional/)

* [pagination](https://gist.github.com/mozillazg/69fb40067ae6d80386e10e105e6803c9)

* [search bar](https://mdbootstrap.com/snippets/jquery/marta-szymanska/1404595#html-tab-view)

* [counter](https://mdbootstrap.com/snippets/jquery/marta-szymanska/1359506#html-tab-view)

### Images:

* Unsplash: [unsplash-simon-zRxLgc-o56I.jpg](https://unsplash.com/photos/zRxLgc-o56I)

* All coins images and background image for a search bar: [www.tavex.pl](https://www.tavex.pl)     for educational use only.

### Content

* Coins features was taken from a [Celtic gold](https://www.celticgold.eu/) website.

[Back to Table of contents](#table-of-contents)
___