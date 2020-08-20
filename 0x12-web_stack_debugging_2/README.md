# 0x12. Web stack debugging #2
## Description
 This project is part of Foundations - System engineering & DevOps ― Web stack debugging:
## Project tasks :wrench:
### [0. Run software as another user ](./0-iamsomeoneelse) 
* 
### [1. Run Nginx as Nginx ](./0x12-web_stack_debugging_2) 
* The root user is a superuser that can do anything on a Unix machine, the top administrator. Security wise, you must do everything that you can to prevent an attacker from logging in as root. With this in mind, it’s a good practice not to run your web servers as root (which is the default for most configurations) and instead run the process as the less privileged nginx user instead. This way, if a hacker does find a security issue that allows them to break-in to your server, the impact is limited by the permissions of the nginx user.
---
Created by [DT Van](https://github.com/dtvangogh)