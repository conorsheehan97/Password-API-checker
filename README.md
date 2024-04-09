# Password-API-checker
This project involves the use of the Pwned Passwords API to check, on the Client side if your password has been involved in any data breaches.

This project is a simple password checker really. The guys at Have I Been Pwned maintain a database which aggregates hashed passwords from known data breaches. This project makes use of the Pwned API which allows us to check if our own Password has been involved in any breach. This project uses 3 functions, in the below order:

- We first input the password we would like to check. This is then UTF-8 encoded, and hashed into a SHA1 object.
- This is then converted to an uppercase Hexadecimal string, and split into the intial 5 characters, and the subsequent tail of newly hashed password.
- We then use then 5 characters to send a GET request to the API. We have this response on our own machine, rather than sending the entire password.
- This response is then converted to a generator of tuples in the format (tail,count).
- We check this response for the tail of the password we initially split, returning the count if found.

Libraries used: OS, Requests, Hashlib
