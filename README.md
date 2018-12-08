# Documentation of the code
This is a school project for a webdev cource at Tampere University of Technology. We did this project in a group of three and the work was distributed equally.

## Project group information
* Persons:
  * Mimmi Matalamäki
  * Oskari Lager
  * Ville Saukko

## Pages and navigation
- Login, logout and register pages which are user can sing in, out or register to the service
- After the login the user gets redirected to the the home page. In the home page is displayed various information about the discussions, events and requests that the user might have. 
- User has also a profile page, where can been seen all the information about him. From that page the user can go and to edit-info site, where the data of the user can be changed. In the change data page there is also a link to the page where user can change the password.
- From the home page the user can also navigate to his friends profile pages.
- If the user is not a friend with others person, the user can add friends from the home page, if he know the name of the person user wants to be friends with
- From the home page user can also navigate to discussions which the user is invited to or which the user has created himself
- From the home page user can also create and view the events. User can only see the events he is taking a part in, or the ones, he has created by him self.

## Technological considerations
- The date of birth is formated to djagos datetime, so it must be applied to MM/DD/YYYY
- Discussion timestamp depends on every machines own system time. For example if one user has her system time two hours later than others, other messages will go under her messages because messages goes in chronological order by timestamps.

### Django apps in your Django project
* Accounts
  * App for login, logout, registeration, email stuff and profile pages
* Homepage
  * Homepage for the user.
* Discussions
  * App for discussions

### Django models and their attributes
* UserProfile:
  * User name, Charfield unique
  * First name, Charfield
  * Last name, Charfield
  * Email, Emailfield unique
  * Phone number, Integerfield
  * Location, Charfield
  * Workplace, Charfield
  * Birth date, Datetime field
  * Bio, Textfield

* Friendship:
  * Sender, Charfield, Foreignkey(User)
  * Receiver, Charfield Foreignkey(User)
  * SendTime, DateTimeField
  * Status, TextField

* Discussion:
  * DiscussionNumber, PositiveIntegerfield
  * CreaterUser, CharField Foreignkey(User)

* DiscussionMessage:
  * Discussion, IntegerField Foreignkey(Discussions)
  * Time, DatetimeField
  * Sender, Charfield Foreignkey(User)
  * MessageData, CharField

* DiscussionMember:
  * Discussion, IntegerField Foreignkey(Discussion)
  * Member, CharField Foreignkey(User)


### URIs

- Homepage: /home/
- Home ajax action: /home/ajax/acceptFriend
- Home ajax action: /home/ajax/declineFriend
- Home ajax action: /home/ajax/cancelFriend
- Home ajax action: /home/ajax/rmFriend
- Login page: /account/login/
- Logout page: /account/logout/
- Register pager: /account/register/
- Users profile page: /account/profile/
- Edit users data: account/profile/edit/
- See other profiles: account/profile/'username'/
- User can change password via email: reset-password/
- Change users password: /accout/change-password/
- Discussion page: /discussion/'discussion id'/
- Discussion data ajaxpage: /discussion/ajax/discussionData/'discussion id'/
- Discussion members ajaxpage: /discussion/ajax/discussionMembers/'discussion id'/
- Discussion delete message ajaxpage: /discussion/ajax/discussionDataMessageRemove/'discussion id'/

### Django views and templates

* Homepage:
  * Views:
    * Homepageview is called when arriving to the homepage. The POST method is called when adding a friend in the homepage. The view is responible for getting and showing the friends, friendrequests and discussions, and also, adding them 


  * Templates:
    * homepage.html consists the template for the homepage. It has a list for the discussions where the user has joined, a list for friends, with the option to delete friendships, and a list for friendrequests where you can cancel sent ones and accept or decline received ones. In addition, in the homepage you can add new friends and join discussions. 

* Accounts:
  * Views:
    * All of the views under check that if the user is logged in, in order to provide the appropriate content.
    * Register is called when the register url is signed. The register view returns form for registering
    * View_profile return the user hes own profile page using own_profile.html template
    * Edit_profile return a page where user can edit hes profile and change the password. It uses the edit_profile.html.
    * Change_password renders the change password change_password.html where user can change hes own password
    * Show_profile renders other users profiles to the logged in profile. It displays different information for users that are logged in, friend with the selected user and so on using these templates: friends_profile.html, user_profile.html, user_does_not_exist.html
    
  * Templates:
    * change_password: Consists of django form made for changing password
    * edit_profile: Consists of django form made for changing userinformation
    * friends_profile: Consists of information of user that is friend with the requesting user. Information in the page is name, bio, workplace, location, birthdate and so on.
    * home: currently no in user anymore. Still there if we want to separate the homepage app from the accounts app
    * own_profile: The same as friends_profile, but there is also a button where user can change hes own profile information
    * reg_form: template that renders the Django registration form
    * user_does_not_exist: Template that tell the user that searched user does not exist
    * user_profile: Template that show limited number for logged in user of user that is not the requesters friend.

