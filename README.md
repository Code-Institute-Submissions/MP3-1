# Coins Catalog

## Data Centric Development Milestone Project.

Coins Catalog is a website where community can share their collections to other members and to the public. All users can search through dataset provided by a community members. Registered users can create, edit or delete their own dataset.

This project is for educational purposes only.

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
- [Screenshots](#screenshots)

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

    <details><summary>Desktop</summary>

    ![](md_data/wireframes/DesktopLandingPage.png)
    </details>
    <details><summary>Mobile</summary>
    
    ![](md_data/wireframes/MobileLandingPage.png)
    </details>
- All Coins Page

    <details><summary>Desktop</summary>

    ![](md_data/wireframes/DesktopAllCoinsPage.png)
    </details>
    <details><summary>Mobile</summary>
    
    ![](md_data/wireframes/MobileAllCoinsPage.png)
    </details>
- Add Coin Page

    <details><summary>Desktop</summary>

    ![](md_data/wireframes/DesktopAddCoinPage.png)
    </details>
    <details><summary>Mobile</summary>
    
    ![](md_data/wireframes/MobileAddCoinPage.png)
    </details>
- Register Page

    <details><summary>Desktop</summary>

    ![](md_data/wireframes/DesktopRegister.png)
    </details>
    <details><summary>Mobile</summary>
    
    ![](md_data/wireframes/MobileRegister.png)
    </details>
- Login Page

    <details><summary>Desktop</summary>

    ![](md_data/wireframes/DesktopLogin.png)
    </details>

    <details><summary>Mobile</summary>
    
    ![](md_data/wireframes/MobileLogin.png)
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

<details><summary>Database</summary>

![](md_data/database/DataBaseTables.png)
</details>

## Surface

### Colors

Colours used in a project:
Purpose | Colour value
------------ | -------------
background | # b0bec5 
main font | # ffc107
navigation and footer font | # ffffff
link | # 696969
hoover | # ffc107
login, register, email button | # ffa000
profile button | # 616161
edit button | # 59698d
delete button | # 78909c

## Fonts

* As a main font I used sans-serif.

## Images

I used images from:

*  [unsplash.com](https://www.unsplash.com) and it is credited in [credits](#credits) section.

*  [tavex.pl](https://www.tavex.pl) and it is credited in [credits](#credits) section.

[Back to Table of contents](#table-of-contents)
___
# Features

___
# Technologies used

___
# Testing

___
# Deployment

___
# Credits

### Images:

* [unsplash-simon-zRxLgc-o56I.jpg](https://unsplash.com/photos/zRxLgc-o56I)

* All coins images are from [www.tavex.pl](https://www.tavex.pl) and are for educational use only.

___
# Screenshots
