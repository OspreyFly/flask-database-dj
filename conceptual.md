### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  An open-source relational database management system.

- What is the difference between SQL and PostgreSQL?
  SQL is a language used for interacting with the relational databases in general, while PostgreSQL is one of many databases that support SQL.

- In `psql`, how do you connect to a database?
  'psql -h <hostname> -U <username> -d <database>' You can use 'localhost' or '127.0.0.1' if it is hosted on the same machine.

- What is the difference between `HAVING` and `WHERE`?
  The 'WHERE' clause is used for filtering individual rows before any grouping or aggregation. 
  The 'Having' clause is used for filtering the results of aggregate functions after grouping has been performed.

- What is the difference between an `INNER` and `OUTER` join?
  An 'INNER JOIN' returns only the matching rows between two tables, while an 'OUTER JOIN' returns all rows from one table and the matching rows from the joined table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  'LEFT OUTER JOIN' includes all rows from the *left table*, and 'RIGHT OUTER JOIN' includes all rows from the *right table*.

- What is an ORM? What do they do?
  (Object-Relational Mapping) is a programming technique that allows developers to interact with a relational database using an object-oriented programming language. Essentially, it provides a higher-level, object-oriented abstraction over the relational database.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  AJAX is a client-side technology used for asynchronous communication within a web page, while server-side libraries like 'requests' are used on the server side to interact with external resources or APIs. They are each suited for different parts of the web development stack.


- What is CSRF? What is the purpose of the CSRF token?
  (Cross-Site Request Forgery) is a type of security vulnerability that occurs when an attacker tricks a user's browser into making an unwanted and unauthorized request to a web application on which the user is authenticated. It takes advantage of the fact that the browser automatically includes authentication cookies with request to the same domain.

  The use of CSRF tokens helps ensure that they can't forge requests on behalf of a user, even if they can trick the user into clicking a link or loading a script. It adds an additional layer of security by requiring information that only the server and the legit user should possess.

- What is the purpose of `form.hidden_tag()`?
  It renders hidden fields within an HTML form containing a CSRF token as a security measure to prevent CSRF attacks.
