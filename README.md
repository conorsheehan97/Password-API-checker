# Password-API-checker
## Overview
This project utilizes the Pwned Passwords API to check if a password has been involved in any data breaches. The API provided by Have I Been Pwned aggregates hashed passwords from known data breaches, allowing users to check the security of their passwords without transmitting the password itself.

## How It Works
### Password Checking Process:
 - Input the password to be checked.
 - Encode and hash the password into a SHA1 object.
 - Convert the hashed password to an uppercase hexadecimal string.
 - Split the hexadecimal string into the initial 5 characters (prefix) and the remaining characters (suffix).
 - Send a GET request to the Pwned Passwords API with the prefix to retrieve a response containing suffixes and their occurrence counts.
 - Compare the received suffixes with the password's suffix to determine if the password has been breached.

### Functions:
- encode_password: UTF-8 encodes and hashes the password into a SHA1 object.
 - check_pwned_api: Sends a GET request to the Pwned Passwords API with the hashed prefix and retrieves responses.
 - check_password: Integrates encode_password and check_pwned_api to verify if the password has been compromised.

### Libraries Used
 - OS: For handling operating system functionalities.
 - Requests: For making HTTP requests to the Pwned Passwords API.
 - Hashlib: For encoding and hashing password strings using SHA1.

## Conclusion
This project provides a simple yet effective way to check if passwords have been involved in data breaches using the Pwned Passwords API. By utilizing hashing and secure API interactions, it ensures privacy and security while validating password integrity.

Contributions and feedback are welcome to improve the functionality and expand the capabilities of this password security checker.
