# [FOODIUM](#) - Milestone Project Four

## Table of Contents

- [**About**](#About)
  - [Why This Project?](#Why-This-Project)
- [**UX**](#UX)
  - [Business Goals](#Business-Goals)
  - [User Stories](#User-Stories)
  - [Style Rationale](#Style-Rationale)
  - [Wireframes](#Wireframes)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
  - [Hosting](#Hosting)
- [**Testing**](#Testing)
  - [**Cart Details Testing**](#Cart-Details-Testing)
  - [**Browsers**](#Browsers)
  - [**Devices**](#Devices)
  - [**Testing User Stories**](#Testing-User-Stories)
  - [**Manual Testing**](#Manual-Testing)
  - [**Code Validation**](#Code-Validators)
- [**Deployment**](#Deployment)
  - [Live App Link](#Live-App-Link)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
  - [Media And Static Folders](#Media-And-Static-Folders)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Media](#Media)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

This web application is a fictional restaurant based in Copenhagen the capital of Denmark. The site allows users to perform many actions such as order a meal, contact the restaurant, make a reservation, and create an account. The site allows the restaurant owner or authorized personal to perform certain actions such as add, edit and delete meals from the website's menu.

### Why This Project?

I created this web application for the Full Stack with Django Project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create a web application for a restaurant, which allows users to order meals and pay with their credit card.

The front-end display and functionality uses HTML, CSS and JavaScript. The back-end functionality uses Python, Django, SQLite3 and PostgreSQL.

## UX

### Business Goals

The business goals of Foodium is to:
- Provide quality meals to all its customers
- Engage with customers via social media channels
- Build brand awareness through social media
- Have more than 1000 monthly active users on the website
- Generate sales through a simple to use checkout platform


### User Stories

As a user, I want to be able to:

- Browse meals on the website
- Make a reservation at the  restaurant
- Search for meals
- Add items to a cart
- Get feedback when I interact with forms
- View details about a meal I like on the restaurant's website
- Create an account
- View ratings on a meal to aid in my decision making
- Contact the restaurant
- Read a FAQ
- Order a meal  with a credit card
- See an overview of an order I just placed
- Find information about past orders I have made

### Style Rationale

I decided to keep the design simple for Foodium. Foodium is minimalistic in design with a focus on a good user experience to help users find items they are looking for, and have a seamless checkout experience. I wanted the site to be bright and have a magical feel to it. I kept the color scheme to a minimum.

### Wireframes
The wireframes used in this project were built using Balsamiq Wireframes [Balsamiq](https://balsamiq.com/). These were the first versions but in the development process, there were many changes.

During the development process some changes were made.

* [Home Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/home%20page%20preview.pdf)
* [Login Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/login%20page%20preview.pdf)
* [Register Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/register%20page%20preview.pdf)
* [Menu Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/menu%20page%20preview.pdf)
* [Single Meal Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/single%20meal%20page%20preview.pdf)
* [Shopping Cart Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/shopping%20cart%20preview.pdf)
* [Checkout Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/checkout%20page%20preview.pdf)
* [Reservation Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/reservation%20page%20preview.pdf)
* [Contact Page](https://github.com/Takaforyannick30/foodium_milestone_project_four/blob/master/static/wireframes/contact%20page%20preview.pdf)

## Features

### Functionality

The app uses Python logic to allow users to sign-in, or sign-up for a free account. The app offers CRUD operations to allow users to create, read, update, and delete blog posts. In addition, users can view all menu, add to their cart and make a purchase after filling their delivery information which is expected to be in Copenhagen. I will like to state that every time I mention meal, I mean beverages as well.

### Existing Features

#### Navbar/Sidenav

- The navbar contains the brand logo which is on the left and it always redirects users back to the home page. 
- The navbar also contains a search form which powers the search functionality of the website.
- The navbar and sidenav links vary depending on whether the user is logged in or not. If the user isn't logged in, the Home, Menu, Reservation, User icon containing Register and Login, and shopping cart  links are shown on the navigation bar. When the user is logged in, the User icon will show My Profile and Logout.And in addition, if the user is super user it will show Meal Management.
- A user who is currently logged out can access the registration page or log in page through the user icon. 
- A logged in user can access their profile or log out through the user icon.
- The checkout icon displays a pricing summary of the user's current order in their cart.

#### Registration Form

- A user who is not logged in can create a new account using the register page. 
- The registration requires an email address, email confirmation, a username (which must be unique), a password and password confirmation fields.
- The form was created using Django Crispy Forms.

#### Log in form

- A user who is registered can log in using their username and password.
- The form was created using Django Crispy Forms.

#### Menu

- Meals and beverages on the website are displayed as thumbnail images with title and price displayed underneath each thumbnail.
- When users click on a meal card, they are taken to the details page of the selected meal.
- If a super user is logged in, they have easy access to edit or delete a meal.

#### Delete modal 
- When the super user is logged in, they have the option to delete a product from the product listings.
- A modal displays as an extra layer of defensive design when the super user clicks delete, to make sure that they want to delete this meal from the website.
- I created the modal with Bootstrap modal popup.

#### Meal details

- Each meal detail page contains price, people per serving, preparation time, and description. Due to the fact that beverages don't have this information, I added an 'if' statement on the product detail page to prevent the field to show if it does not contain information about the field.
- Users can add a meal to their cart by clicking the "Add to cart" button or continue shopping by clicking the "Keep shopping" button.

#### Toast notification

- When a user selects a meal, they are notified of their selection through a success toast message.
- They are then given the option to continue shopping or view their cart.


#### Billing details

- The users profile page can only be accessed by a logged in user. 
- The account page contains the user's billing information that they can edit and update. At the moment the feature is not complete because the billing information is supposed to automatically populate a new order form but it's not.
- An order summary is visibile if user's have made a purchase in the past. This will contain:
   - Order number
   - Date an item was purchased
   - Item(s) purchased
   - Order total
   - Delivery
   - Grand total

#### Toast notification

- When a user updates their billing information they are notified of this change through a success toast message.

- The shopping cart page features a summary of all the meals the user has added to their shopping cart.
- Each item includes an image, name,  unit price and total price.
- The user has the ability to adjust the quantity in their cart. A user can also remove an item from their cart. When the quantity is updated. the subtotal will reflect the change.
- Cart total, delivery total and grand total of the user's cart are reflected in the order summary.
- A call to action button to proceed to checkout takes the user to the payment section.

#### Toast notification

- When a user adds a meal to their cart, a toast notification displays with the meal information.
- A user is notified of delivery cost which is 39kr.
- A call to action to visit the checkout is displayed below the item information.

#### Checkout form

- The checkout page features a form that needs to be filled out by the user.
- All users needs to fill out their billing information.
- Details required are name, address, email address, street address, town/city, postal code.

#### Stripe

- Users can complete the checkout process by entering their card details.
- Payment is handled through the secure Stripe API.
- Once a user clicks to buy, and if successful payment is made, the user is taken to the checkout success page.

#### Checkout success

- The order confirmation page gives the customer all their order information.
- An order number is generated on checkout.
- The user is invited to continue ordering after checkout.

#### About page

- The About page features a brief description about Foodium.

#### Reservation page

- The Reservation page contains a form for the user to fill in other to make a reservation to send to the Restaurant's admin.
- Name, number, email, number of persons, date and time are all required fields.
- An email is sent to the store admin's email address notifiying them of a new contact enquiry in the admin dashboard.
- The reservation can be checked by logging in to the admin area.
- A reservation success page informs  the user their reservation will be reviewed within 24hours. 
- At the moment there is no functionality to check availabity of table when a user is making a reservation that is why they do not get a confirm reservation message.

#### Toast notification

- When a reservation form form has been successfully submitted, the user is notified via toast message.

#### Contact page

- The contact page contains a form for the user to fill in to send to the Restaurant's admin.
- Name, subject, email address and message are all required fields.
- An email is sent to the store admin's email address notifiying them of a new contact enquiry in the admin dashboard.
- The message can be checked by logging in to the admin area.

#### Toast notification

- When a contact form has been successfully submitted, the user is notified via toast message.

#### FAQ page

- The FAQ pages contains four frequently asked questions.
- The first question has an answer which clearly states that Foodium is a fictional restaurant. 
- At the bottom of the form users are asked to 'contact us' if their question in mind was not answered.


## Features Left To Implement

#### Additional login methods
- For a future update, I would like to include the ability for users to login via a social media platform such as Facebook or google. 

#### Additional checkout methods
- For a future update, I would like to include the ability for users to checkout via PayPal as it is a popular checkout method.

#### Two Step verification
- With cybercrime on the rise and the recent trend of many bank applications introducing two-step verification, this would be a nice extra layer of security for users when logging in.

#### Custom 404 and 500 pages
- Create and implement custom pages for HTML status codes of 404 (Page Not Found) and 500 (Internal Server Error). Given the time constraints, this was not possible to implement. I tried to implement a 404 but ended up deleting the template and related code because it was not fully functional. 

## Technologies Used

- [**Balsamiq**](https://balsamiq.com/)
    - I've used **Balsamiq** to create wireframes of my website/app before building it.
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles to the elements and content of my app. The base.html file is linked directly to the base.css stylesheet.
- [**Bootstrap**](https://getbootstrap.com/)
   -Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS-and Javascript-based design templates for tools, typography, forms, buttons, navigations, and other interfaces.  Bootstrap classes were used to build the navigation bar and to make the website responsive.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**Django**](https://www.djangoproject.com/)
    - The project uses **Django** as the Python web framework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Python and Django in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**Stripe API**](https://stripe.com/gb)
    - The project uses **Stripe** to make secure payments for logging and upvoting Feature Requests. The project uses Stripe's test payment functionality.
- [**SQLite**](https://www.sqlite.org/index.html)
    - The project uses **SQLite** as the relational database to hold the backend information for the varions models used, when running locally.
- [**PostgreSQL**](https://www.postgresql.org/)
    - The project uses Heroku's **PostgreSQL** relational database to hold the backend information for the various models used, when deployed remotely.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The navigation bar and headings/titles on the site uses *_Roboto Slab_* font and the rest of the site uses the *_Roboto_* font.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
- [**Gitpod**](https://www.gitpod.io/)
   -Gitpod is an online integrated development environment for GitHub. It creates a complete and disposable development environment for any GitHub repository directly in a browser. This project was developed in Gitpod.
- [**Dev Tools**](https://developers.google.com/web/tools/chrome-devtools)
   - Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. DevTools can help you edit pages on-the-fly     and diagnose problems quickly, which ultimately helps you build better websites, faster. Google Chrome's Dev Tools was used in the building     process of this project.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in Gitpod, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting

- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

## Testing

### Cart Details Testing
To test the website's checkout functionality, use the following payment credentials:

- **Card number:** 4242 4242 4242 4242
- **Expiry date:** Any date in the future
- **CV2 number:** Any 3 digits
- **ZIP:** Any 5 digits

### Browsers
This web application was tested in the following browsers to ensure the web application is compatible and responsive.
 * Chrome
 * Mozilla
 * Safari
 * Opera 
 * Internet Explorer

### Devices
 This web application was tested in the following devices to ensure the web application is compatible and responsive.
 * IPhone 8 Plus
 * Huawei P30 Pro 
 * Huawei Mediapad T5
 * MacBook Pro

### Testing User Stories

- **As a user, I want to be able to browse meals on the website**
1. Click on "Menu" dropdown on the navbar.
2. Select food category you want to browse.

- **As a user, I want to be able to make a reservation at the restaurant**
1. Click on "Reservation" link on the navbar.
2. Fill in the form with Name, Phone Number, Email, Number of Persons, Date and Time.
3. Click on the "Send" button.

- **As a user, I want to be able to search for meals**
1. Type a word related to the meal you are looking for.
2. Click on the "Search" button.

- **As a user, I want to be able to add items to a cart**
1. Click on the meal you would like to add to your cart.
2. Click on "Add To Cart" button.

- **As a user, I want to be able to get feedback when I interact with forms**
1. Fill in a form with correct information.
2. Click on the "Send" button.

- **As a user, I want to be able to view details about a meal I like on the restaurant's website**
1. Click on the meal you would like to get more information about.

- **As a user, I want to be able to create an account**
1. Click on the user icon in the navbar.
2. Click on "Register"
3. Fill in the Register Form with Email Address, Email Address Confirmation, Username, Password and Password(again).
4. Click on the "Sign Up" button.

- **As a user, I want to be able to view ratings on a meal to aid in my decision making**
1. Click on the meal you are interested in.

- **As a user, I want to be able to contact the restaurant**
1. Click on "Contact Us" link in the footer.
2. Fill in the form with Name, Subject, Email Address and Message.
3. Click on the "Send" button.

- **As a user, I want to be able to read a FAQ**
1. Click on "FAQ" in the footer.
2. Click on the question you would like to see the answer.
3. Click on "Contact Us" below the FAQ if you have different question.

- **As a user, I want to be able to order a meal with a credit card**
1. Go to your cart.
2. Click on "Secure Checkout".
3. Fill in your personal information.
4. Click "Complete Order"

- **As a user, I want to be able to see an overview of an order I just placed**
1. Click on the user icon in the navbar.
2. Click on "My Profile"

- **As a user, I want to be able to find information about past orders I have made**
1. Click on the user icon in the navbar.
2. Click on "My Profile"

## Manual Testing

**NavBar** 
* I tested that the navbar brand(FOODIUM) redirects user to the home page.
* I tested that the navbar collapses to a hamburger menu in smaller screen devices.
* I tested that when the Home icon is clicked, users are taken to the home page.
* I tested that "Meals" dropdown menu in the navbar shows all food categories (Starters, Burgers, Main Course, Beverages, All Meals).
* I tested that when a food category is clicked, it shows all meals related to that category.
* I tested that when the reservation icon is clicked, users are taken to the reservation form.
* I tested that when the user icon is clicked, a dropdown appears with "Register" and "Login" option.
* I tested that when a user is logged in, the user icon dropdown changes with "Meal Management", "My Profile" and "Logout" Option.
* I tested that when the cart icon is clicked, users are taken to the shopping cart page.

**Search**
* I tested that the search bar shows the user meals related to the word they typed.

**Login/Logout**
* I logged in from several fake user accounts using the username(or email) and password and tested the "Login" button.
* I tested the log out funtion from all accounts by clicking on the "Logout" button.

**Register**
* I tested the registration form by creating several fake user accounts with an Email Address, Emails Address Confirmation, Username, Password, Password(again) and tested the "Sign Up" button.

**Menu/Meal Page**
* I tested that the "View Menu" button in the home page, takes user to the menu page.
* I tested that when a user clicks on a specific meal , it takes them to the meal detail page where they can see Meals Name, Price, Servings, Preparation Time, Ratings and Description.
* I tested that on the meal details page, when a user clicks on the "+" button, the quantity increases.
* I tested that on the meal details page, when a user clicks on the "-" button, the quantity reduces.
* I tested that the "Add To Cart" button is clicked, it adds the meal into the users cart.
* I tested that the "Keep Shopping" button redirects user to the Meals page.
* I tested that when a meal is being added to the cart, a toast appears displaying products added, delivery fee and I tested "Go To Secure Checkout" button.

**Reservation**
* I tested the reservation form by filling it in with Name, Phone Number, Email, Number of Persons, Date, Time and clicking on the "Send" button.

**My Profile**
* I tested that in the "My Profile " page the user can see and edit their personal information (Phone Number, Address) and tested the "Update Information" button.
* I tested that in "My Profile" page Order History table is being displayed. Users can see Order Number, Date, Items and Order Total.
* I tested that when a user clicks on the Order Number, it shows further information about the specific order they placed (Name, Delivery Address, Phone Number, Delivery Fee and Grand Total).
* I tested that the "Back To Profile" button redirects user to "My Profile" page.

**Cart**
* I tested on the cart page, that if the "+" icon is clicked, the product quantity is increasing.
* I tested on the cart page, that if the "-" icon is clicked, the product quantity is decreasing.
* I tested on the cart page, that if "Update" is clicked after the user changes the quantity, the subtotal updates.
* I tested on the cart page, that if "Remove" is clicked, the meal is being removed from the cart.
* I tested that the "Keep Shopping" button redirects user to the Meals page.
* I tested that the "Secure Checkout" button brings up a form where the user has to fill in with personal details and credit card details.
* I tested that if the Secure Checkout form is correctly filled and the "Complete Order" button is clicked, it takes user to the Checkout Success page where user can view the order details and confirmation.
* I tested that if "Adjust Bag" is clicked, the user will be taken back to their cart.

**Contact**
* I tested that the "Contact Us" link in footer takes user to the Contact form.
* I tested the Contact form by filling it in with Name, Subject, Email Address, Message and tested the "Send" button.

**FAQ**
* I tested that the "FAQ" link in footer takes user to the FAQ page.
* I tested the FAQ by clicking on a question to see if the answer will pop up.
* I tested the "Contact Us" link to see if it will take user to the Contact page.


**Social Icons**
* I tested that all social icons open up a new tab with the social media account linked to them.

**About Us**
* I tested that the "About Us" link in footer takes user to the About page.

### Code Validators 
The web application's HTML and CSS code has been tested in [W3C Validator](https://validator.w3.org/). The JavaScript code has been tested in [JS Hint](https://jshint.com/). Python syntax has been tested in [Pep8 Online Tool](http://pep8online.com/) and responsiveness in this [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly).

## Deployment

This project was developed using Gitpod. I used GitHub for my version control and Heroku to host the live version of the project. Heroku hosts complex web applications and services. To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Went to the **Resources** tab in Heroku and searched for **Heroku Postgres** in the 'Add-Ons' section.
3. Selected the free **Hobby** level.
4. Updated the `env.py` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.
5. Ran the `python3 manage.py makemigrations`, `python3 manage.py migrate`, `python3 manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.
5. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.
6. Copied and pasted all of the `env.py` default variables in Heroku's Config Vars section.
7. Went to the **Deploy** tab in Heroku, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.
8. Went to the **Developers** section in Stripe and clicked on **API Keys**.
9. Copied and pasted the **Publishable Key** and **Secret Key** and set them as the `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` environment variables in the `env.py` file within my local workspace.
10. Updated the `settings.py` with the new Stripe environment variables.
8. Went to the **S3** section of AWS and created a new S3 bucket.
9. Within the relevant bucket's permissions, changed the **CORS Configuration** to the following:

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
    ```

10. Still in the **S3** section, changed the **Bucket Policy** to the following:

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<my-bucket-name>/*"
            }
        ]
    }
    ```

11. Replaced the `<my-bucket-name>` in the `Resource` line with my S3 bucket's name instead.
12. Went to the **IAM** section of AWS, created a 'New Group' and attached my S3 bucket details to it.
13. Still in the **IAM** section, created a 'New Policy' and a 'New User' and attached these to the newly created group.
14. Updated the `settings.py` file in my local workspace with the relevant S3 bucket details:

    ```
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "<s3-bucket-name>"
    AWS_S3_REGION_NAME = "<region-name>"
    AWS_ACCESS_KEY_ID = <access-key-id>
    AWS_SECRET_ACCESS_KEY = <secret-access-key>
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    ```

15. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.
16. Updated the `settings.py` file with the relevant configuration for static and media file storage.
17. Ran the `python3 manage.py collectstatic` command to push the static files to my S3 bucket.
18. Created a requirements.txt file using the following command in the terminal window:

    ```pip3 freeze --local > requirements.txt```

19. Created a Procfile using the following command in the terminal window:

    ```echo web: gunicorn UnicornAttractor.wsgi:application > Procfile```

20. Ran the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[Foodium](https://foodium-restaurant.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[Foodium GitHub Repository](https://github.com/Takaforyannick30/foodium_milestone_project_four)

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository](https://github.com/Takaforyannick30/foodium_milestone_project_four)
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Complete one of the two below steps in your local workspace to set your own credentials for the environment variables:
    - Enter and save your own credentials in the `.baschrc` file; or
    - Create a `.env.py` file with your own credentials and import this into the `settings.py` file
9. Install the `requirements.txt` file by running the below command in your CLI Terminal:

    ```sudo pip3 install -r requirements.txt```

10. Run one of the following commands in your Terminal to launch the Django project:

    ```python3 manage.py runserver```

11. Click the `http://` link that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.
12. Run the following commands to migrate the database models and create a super user:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

Once the migrations are completed and the super user has been created successfully, the site should be running locally. To deploy the site remotely, follow the instructions in the [Deployment](#Deployment) section.

### Media And Static Folders

My static and media folders are hosted in my s3 bucket for the live version of this site.

## Credits

### Content

* Most of this project's us functionality and code was taken from [Code Institute's](https://codeinstitute.net/) Boutique Ado Project. I had to customize it for my app and added additional features.

* The Modal Structure HTML and JavaScript code was taken from [Bootstrap Modals](https://getbootstrap.com/).

* Checkout code taken from [Stripe](https://stripe.com/en-dk).


### Media
None of the images belong to me.

* I Created the Logo Icon on my website using [Free logo design](https://www.freelogodesign.org/)

* The favicon on my website was created using [favicon.cc](https://www.favicon.cc/)

* Meal images were taken from [Red Bamboo](https://red-bamboo.square.site/?fbclid=IwAR0JbLypnlU62XXLT-XYuNmGN8FVHmFw8RDdpO8MDyvadX2NQvFsUn8XbMc) restaurant.

* Home page image was taken from [Pexels](https://www.pexels.com/search/restaurant/?fbclid=IwAR2Ams9t0fi60vOMxRXpuPGCeCf-R4mGXkSrd4xVP-cuqzb3WVJO5AkwX5M).

## Acknowledgements

* A special thanks to my mentor, Sandeep Aggarwal, for his feedback on my project's scope, design and functionality.
* Code Institute's Tutor assistance has helped my a lot in solving and understanding the cause of the errors and issues I was facing.
* I took inspiration for this project from [Hello World Apparel](https://github.com/orlamadden/hello-world-apparel).

## Disclaimer

This project is for educational purposes only.
