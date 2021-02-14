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

### Landing Page - Search

* Search returns results from below fields from a database:
    - name
    - type
    - weight
    - weight unit
    - country
    - purity
    - mint
    - year
    - description

    Everything works as expected

    * For not logged in user search returns coin image and coin description as a link to register page.
    * For registered user search returns coin image and coin description. Description opens coin details.
    * For not recognized search, flash message displays: `No results, Please try again!`

* Coin counter works as expected

* For not registered user, Join our community today section works and displays all content.
Register link under a title works. Buttons on last 3 records from database work and redirect to register page.


### Catalog Page

Page displays 10 records from a database. Pagination links work as expected.
When logged in as an administrator `Edit` and `Delete` buttons are visible and work as expected.

![](md_data/test/catalog_administrator.png)

### Log In Page

Form validation, `Log in` button and Register link work as expected.

### Register Page

Form validation, `Register` button and Log in link work as expected.

### New Coin Page

Form validation, `Add Coin` and `Reset` buttons work as expected.
Corresponding tooltips are displayed for: weight, purity and year.
Type, weight unit and country drop down list display as expected.

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

### Error pages

All unrecognized pages are always redirect to error page.

![](md_data/test/errorpage.png)


[Back to Table of contents](#table-of-contents)
___
## Compatibility testing

Site was tested across multiple virtual mobile devices and browsers.
I checked all supported devices in both Mozilla web developer tolls and Chrome developer tools.

All tests Passed for devices from 320px on Chrome developer tools and 340px on Mozilla web developer tolls.

I tested on hardware devices such as: Lenovo ideapad with Ubuntu and Windows OS's as a virtual machines,
Lenovo smartphone with Android 7, LG smartphone with Android 8, Google pixel 3 with Android 11. No issues found.

[Back to Table of contents](#table-of-contents)
___
## User stories testing


[Back to Table of contents](#table-of-contents)
___
## Issues found during site development

During site development I found a lot of bugs. I always tried to fix them immediately.
Here are few trivial and more complex examples.

### Register form error

During the register form test I found an error.
The form allowed me to create an email without a domain name. As a test example I used: aa@aa

![](md_data/test/emailtest.png)


I had to change the pattern from

`pattern="^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}${5,35}$"`

to

`pattern="^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}$"`

![](md_data/test/emailcorrectpatternerror.png)

![](md_data/test/emailcorrectpatterndb.png)

After that fix, register form accepts expected pattern. The only problem was with a typo on email label and placeholder.
The slack user found the bug on peer-code-review channel.

![](md_data/test/email_slack.png)

### Html errors

I used [Nu Html Checker](https://validator.w3.org/nu/) to check HTML bugs.
It was hard to use because I have Jinja2 template language inside html file.

Bugs found and fixed:

`<div>` in Navigation

![](md_data/test/div_in_navbar.png)

![](md_data/test/div_in_navbar_fix.png)

Even if everything is OK an error still appears.

![](md_data/test/p_fix.png)

![](md_data/test/p.png)

### Search errors

Searching wasn't working properly and was confusing.

![](md_data/test/search.png)

Fix in Python:

![](md_data/test/index_update.png)

And in app.py file for search route:

![](md_data/test/app_py.png)

The `x` is only visible in chrome browser for an input field with `type="search"`

I tried to fix it but it is hidden behind MDB CSS or JS file.

#### I leave it as unfixed bug.

### Other unfixed bugs:

#### Second letter in a surname is not capitalize.

![](md_data/test/bug2.png)

#### Coins edited by administrator are saved as administrator collection in a database.

This should return back to database as a user collection.


[Back to Table of contents](#table-of-contents)
___
## Performance testing

I run Lighthouse tool to check performance of the website.
Performance results always vary and this is because of 3rd party images in mongodb database.

<details><summary>Performance</summary>

![](md_data/test/performance.png)
</details>

<details><summary>Performance - images</summary>

![](md_data/test/performance_images.png)
</details>


[Back to Table of contents](#table-of-contents)
___
## Code Validation

### Nu Html Checker to test HTML

![](md_data/test/nu_html.png)

### W3C CSS Validator to validate CSS

![](md_data/test/w3c_css.png)

### Jshint to test JavaScript

![](md_data/test/code.js.png)

![](md_data/test/email.js.png)

### PEP8 online

#### Result: Pass

[Back to Table of contents](#table-of-contents)

#### Back to [README.md](https://github.com/marcin-kli/MP3)