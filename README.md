# compsoc_stats

README still under development.

To get your first cookie value:
- Go to [https://su.sheffield.ac.uk/](https://su.sheffield.ac.uk/) and login
- Open developer console
- Go to [https://su.sheffield.ac.uk/auth/dashboard](https://su.sheffield.ac.uk/auth/dashboard)
- Open up the HTTP request for the webpage and find the **cookie** header under *Request Headers*
- Copy the cookie, it should look something like this: `su_session=nidpa5odknif09on59q3eli03n0ru5i1`
- Paste it into the `cookie.json` file, as the value to the key `cookie`