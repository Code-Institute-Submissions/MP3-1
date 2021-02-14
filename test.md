# Table of contents
- [Functionality testing](#functionality-testing)
- [Compatibility testing](#compatibility-testing)
- [User stories testing](#user-stories-testing)
- [Issues found during site development](#issues-found-during-site-development)
- [Performance testing](#performance-testing)
- [Code Validation](#code-validation)

## Functionality testing

I used Mozilla web developer tools and Chrome developer tools throughout the project for testing and solving problems with responsiveness and style issues.

### Landing Page

Starting from the top of the page, I check:

* Navigation - first time user:
    - brand title - after clicking on the link page reloads.
    - Home - after clicking on the link page reloads.
    - Catalog - after clicking on the link page redirects to coins catalog.
    - Log in - after clicking on the link page redirects to log in page.
    - Register - after clicking on the link page redirects to register page.

* Navigation - logged in as a user:
    - New Coin - after clicking on the link page redirects to new coin page.
    - Profile - after clicking on the link page redirects to profile page.
    - Log out - after clicking on the link page redirects to home page.

* Navigation - logged in as an administrator:
    - Admin options button - after clicking drop down menu displays as expected
    - Coin Types - after clicking on the link page redirects to coin types page
    - Add new Type - after clicking on the link page redirects to add new type page

* Footer - Contact me button works and opens contact us page

### Catalog Page

Page displays 10 records from a database. Pagination links work as expected.
When logged in as an administrator Edit and Delete buttons are visible work as expected.

![](md_data/test/catalog_administrator.png)

### Log In Page

Form validation, `Log in` button and Register link work as expected.

### Register Page

Form validation, `Register` button and Log in link work as expected.

### New Coin Page

Form validation, `Add Coin` and `Reset` buttons work as expected.
Corresponding tooltips are displayed for: weight, purity and year.
Type, weight unit and country drop down list displays as expected.

![](md_data/test/new_coin_validation.png)

### Profile Page

`Add new coin`, `Show Coins` and `Hide Coins` buttons work as expected.
`Click here to view more details` opens coin details. `Edit` and `Delete` buttons work as expected.

![](md_data/test/profile.png)

#### Edit Coin Page

Page loads and displays all data correctly.
Form validation, tooltips, drop down list and `Update`, `Cancel` buttons work as expected.

![](md_data/test/edit_coin.png)

### Admin options - Add new Type Page

`Add Type` and `Reset` buttons work as expected. 

### Admin options - Coin Types Page

`Edit` and `Delete` buttons work as expected.

#### Edit Coin Types Page

Page loads correctly. `Edit Type` and `Cancel` buttons work as expected.

### Contact Us Page

Page loads and displays user data correctly when logged in as a user or administrator. As a regular
Form validation and `Send a message` button work as expected. OK button redirects user to home page.

![](md_data/test/contact_us_page.png)

![](md_data/test/email.png)


[Back to Table of contents](#table-of-contents)
___
## Compatibility testing


[Back to Table of contents](#table-of-contents)
___
## User stories testing


[Back to Table of contents](#table-of-contents)
___
## Issues found during site development


[Back to Table of contents](#table-of-contents)
___
## Performance testing


[Back to Table of contents](#table-of-contents)
___
## Code Validation