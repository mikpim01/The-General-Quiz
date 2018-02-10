Security
========

File: generalQuiz/security.py

Account
-------

.. code-block:: python
    :caption: Validate Registration
    :name: validatereg

    validateReg(fname, lname, password, confpassword, age, year)

The Validate Registration function ensures that all of the details that have been
entered are possible and safe to use. It checks whether:

- Your First Name is over three characters long
- Your First Name has any numbers in it
- Your Last Name has any numbers in it
- You Username which will be generated already exists
- Your Password is too short (under 6 chars) or too long (over 100 chars)
- Your Password and your Confirming Passwords match
- Age is an integer

If it finds that any of the above are true, it will append that error to an array
and return that when its finished.

----------

.. code-block:: python
    :caption: Register
    :name: register

    register(username, password, fname, lname, age, year)

The Register function is called after the validate register function. It calls the
Hash function for the password then adds the user to the Database via the Add Class
in the db file.

----------

.. code-block:: python
    :caption: login
    :name: login

    login(username, password)

The login function takes the username and unhashed password from a user input, then
graps the hashed password from the DB using the username, calls the pskCheck function
and then will return the userData if the password is correct or False if the Password
is incorrect.

----------

Hash
----

.. code-block:: python
    :caption: Password
    :name: psk

    psk(password)

The psk function grabs the salt from the config file then Hashes the password using
sha512 and the salt. Then it returns the Hashed password.

----------

.. code-block:: python
    :caption: Check Password
    :name: pskcheck

    pskCheck(hashedPassword, password)

The pskCheck hashes the password in the same way as the psk function, then it
compares it to the hashedPassword; if it's a match, it returns True otherwise it
returns False.
