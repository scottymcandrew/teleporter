# Teleporter - Transport for the Modern Ages

This project is for my CodeInstitute Full Stack Dev course. Specifically this is the final module milestone project in "Full Stack Frameworks with Django".

The purpose of this application is to track bug and features for my Teleporter service.

Bugs can be reported for free but feature request votes incur a cost; this is how the service is funded.


## UX

**Wireframes are in the wireframes directory**

The site had to be intuitive yet functional due to the number of capabilities. Features and bugs are two separate functions and so were divided. I decided to use FontAwesome icons on a static top navbar. There are tooltips for each icon. On smaller screens the nav bar collapses. Indeed I have used Bootstrap responsive utilities to re-size all content.

**One exception to the point above - chart.js** - I ran out of time for project submission and on small screens the graphs do not currently look good. Despite the fact I have included the responsive option on chart.js config. Perhaps a bug?

The colour scheme I wanted fresh but fun (given the light-hearted subject). Therefore I chose the "Minty" theme from Bootswatch: https://bootswatch.com/minty/

The landing page for the site uses a Parallax scrolling structure with three main sections representing the about section, user-area for features/bugs, and a link to register (although logon/registration is prompted when anonymously accessing member-only areas).

The About section follows the same structure as the landing site.

These pages are accessible without an account, as is the blog section. I also decided to make the service stats section public to be transparent on the current status/state of the service.

The bugs section includes a list of bugs which are not archived. Archived is a status which is set only by site admins on the admin page. I decided not to hide resolved bugs automatically to allow final verification and comments.

Bug detail section expands info about each bug. If it is a site admin or bug ower who is logged in they will be presented with a control panel to edit/update/delete the bug. Voting is also implemeted here - enforcing 1 vote per logged-in user. The icon updates depending on whether that user has voted or not. This is updated with AJAX.

Comments are permitted here by authenticated users.

The feature list/detail sections are largely the same except for these differences:
- Features are in a Jumbotron since they are of course more important than bugs!
- There are no votes, but rather contributions in the form of purchases.
- There is a different icon signifiying whether the feature is roadmap (set by the site owners) or user-requested.

Profile pictures are implemented and will show up on the navbar and bugs/features/comments (except for blog comments since don't require a logon).

### User Stories

- As the site owner/admin, I need to be able to add/manage/remove users/bugs/features/comments. I also need to be able to publish blogs through the admin panel.
- As a potential customer, I need to be able to find out what the service is all about and view some current statistics and read the current news (blog).
- As a potential customer, I need to be able to register for the site to use the service and be able to contribute.
- As a customer, I need to be able to edit my profile.
- As a customer, I need the ability to report bugs and contribute/comment on other bugs. I need to check on bug status.
- As a customer, I want to be able to ask for features and comment on others.
- As a customer, I want to be able to purchase contributions to features.

## Features
 
### General Features
- Public information resources - landing page, about page
- Public blog with ability for anyone to raise comments.
- Service statistics - public page using chart.js to provide some current stats. Also list implemented roadmap features.
- User registration and authentication using Django Framework. Users can update their profile with basic info including profile picture.
- Users can update passwords and even reset using email.

### Bugs
The bugs section requires the user to be registered and logged in. If attempting to browse here anonymously a redirect will occur.

- Bug list which returns all bugs which are not archived (only possible by site admins as per comment previously under UX section).
- Bug list displays severity (bug icon changes colour depending on the value), author, creation date-time, comment and vote count.
- Bug list page has a button to raise a new bug.
- Bug list page has a search function which matches bug title and description.
- Bug list is paginated.
- Bug detail has much of the information above, in addition:
    - Vote button. Tracked per authenticated user to prevent multiple votes. If user has already voted it will be a downvote.
    - If authenticated user is a site admin, they will see a control panel allowing updating of the bug.
    - Bug owners see the panel also except are unable to update severity or status. Only site admins should be able to do this once a bug is registered.
    - Bug comments listed at the bottom. All Authenticated users can comment. Comments are paginated.

### Features / E-Commerce
The features section requires the user to be registered and logged in. If attempting to browse here anonymously a redirect will occur.

Rather than repeat myself, this follows the same general structure as the bugs section. The differences I will detail below.

- Features are either roadmap or user-contributed.
- Features are purchasable, implemented via Stripe payment gateway.
- Features have a base cost and a user can purchase any number of contributions, depending on how keen they are!
- Rather than votes - stats displayed are number of contributions and funds raised.

## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [Python](https://www.python.org)
  - This logic of this application is coded in Python.
- [Django 2.2 (LTS)](https://www.djangoproject.com)
  - Django is used as the overall framework of this application.
- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction)
  - This project uses **Bootstrap** to provide the website's structure.
- [Bootswatch Minty Theme](https://bootswatch.com/minty)
  - Colour theme for Bootstrap.
- [FontAwesome](https://fontawesome.com/start)
  - This project uses **FontAwesome** for the various button icons.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation and for AJAX.
- [Heroku](https://heroku.com)
    - This application is hosted on Heroku.
- [PostgreSQL on Heroku](https://www.heroku.com/postgres)
  - PostgreSQL is the backend database hosted on Heroku.
- [Amazon AWS S3](https://aws.amazon.com/s3/)
  - S3 for static files storage.


## Testing

Tests have been implemented in tests.py for most apps and coverage reports generated. Not 100% coverage but most for models. Some views not covered but actually these manipulate the models, which do have coverage.

To run tests, use command "coverage run manage.py test". This may have too much output, including third party libraries. You can selectively run per app via e.g. "coverage run --source=bugs manage.py test"

In addition from my own GUI tests:

1. Navigation / General functionality:
    1. Main page redirects correctly to index. Parallax working on all screens (verified with dev tools) on index and about us page.
    2. Verified index/about/blog and stats are accessible anonymously. Comments on blog are working.
    3. Bugs/Features only accessible when authenticated.
    
2. User Management:
    1. Able to successfully register.
    2. Able to subsequently log in.
    3. Able to upload profile picture.
    4. Able to update profile info including password.
    6. Able to reset password - email received.
    
3. Data operations:
    1. Able to raise a new bug.
    2. Able to update bug/feature as site admin / owner.
    3. Able to comment on bug/feature.
    4. Able to search for title/body of bug/feature.
    5. Stats are correct for bugs/features - votes/purchases/funds/comments.
    6. Timestamps correct.
    7. Chart.JS stats are correct.
    
4. E-Commerce
    1. Able to add features to cart.
    2. Able to update cart.
    3. Able to reach checkout.
    4. Able to purchase from checkout using test card number "4242424242424242" and a valid expiry date.

- Responsive Design:
    1. The above tests were carried out with varying screen sizes (using Chrome Dev Tools).
    2. On small screens the navbar collapses and the burger icon is displayed and works.
    3. Components reduce in size correctly.
    4. As described earlier, chart.js components need improvement on small screens.

## Deployment

Start by cloning this repo!

### Hosting

This is hosted on Heroku but any hosting platform should work providing requirements.txt is honoured. That is *key* because it contains all python packages used.

It is possible to run locally, for example PyCharm Professional. There are static files and database considerations as detailed below.

### Django
- Runs on Django version 2.2

### Environment Varibles
The following environment varible keys need to be set:
- DATABASE_URL - IF this is being hosted then this needs to be set. If it is not set, then you can revert to sqlite and it should work.
- STRIPE_PUB_KEY - Stripe API public key from your account.
- STRIPE_SECRET_KEY - Stripe API secret key from your account.
- AWS_ACCESS_KEY_ID - Key ID for your AWS account which has access to your S3 bucket for static files.
- AWS_SECRET_ACCESS_KEY - Secret ID for your AWS account which has access to your S3 bucket for static files.
- SECRET_KEY - Django Secret key as defined in settings.py

### Static Files
As mentioned earlier - hosted on AWS S3. This can be done without S3 but not recommended in production. For example using Python package "whitenoise".

If using S3, the bucket needs to have public read permissions and CORS config allowing GET and HEAD. Using this requires packages "django-storages" and "boto3". Starting with local static files you need to run "python3 manage.py collectstatic" to push to S3. Be aware current config in this repo is set to S3.

### Deployment

Once these considerations are addressed you can run locally as described before (using sqlite), or deploy to somewhere like Heroku. Heroku uses requirements.txt to install dependencies.

## Credits

### Content / Acknowledgements
- I learned many of the coding concepts via the excellent book Django 2 by Example (https://learning.oreilly.com/library/view/django-2-by/9781788472487/). A number of code snippets in this project drew from the examples there.
- Other code snippets/concepts taken from CodeInstitute materials.
- Bootstrap CSS and Bootswatch Minty Theme.
- W3Schools for help with Parallax.
- Django official documentation.
- Content for the bugs, features etc is original content.

### Media
- The media used in this site was obtained from https://unsplash.com/ and Google Images.