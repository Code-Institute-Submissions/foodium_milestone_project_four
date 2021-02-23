# [FOODIUM](#) - Milestone Project Four

## Table of Contents

- [**About**](#About)
  - [Why This Project?](#Why-This-Project)
- [**UX**](#UX)
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
  - [Testing User Stories](#Testing-User-Stories)
  - [Responsive and Functional Testing](#Responsive-and-Functional-Testing)
  - [Additional Testing](#Additional-Testing)
  - [Code Validation](#Code-Validation)
  - [Interesting Bugs Or Problems](#Interesting-Bugs-Or-Problems)
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
- [*Dev Tools*](https://developers.google.com/web/tools/chrome-devtools)
   - Chrome DevTools is a set of web developer tools built directly into the Google Chrome browser. DevTools can help you edit pages on-the-fly     and diagnose problems quickly, which ultimately helps you build better websites, faster. Google Chrome's Dev Tools was used in the building     process of this project.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in Gitpod, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting

- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

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