# Docker Limux Shell
Create linux shells in docker per users request. This might be ideal for classroom settings for teaching/testing stuff. 

## Why
Made this for reddit post: https://www.reddit.com/r/selfhosted/comments/1ekr2nm/looking_for_a_service_that_can_automatically/
This is no way perfect or finished, its just a POC that should be built up. I made this while laying in bed on my phone. 

## Setup
The ***shell_base*** is the linux shell that you want to offer to your users. 

The ***shell_hub*** is the flask app webpage that allows users to create a shell. 


- Clone this repo.
- Build a dockerfile for your ***shell_base*** that you want to use/offer to your users. Example using ubuntu: `shell_base/dockerfile`
  - Change to the ***shell_base*** directory and build the image: `docker build -t shell_base .`
- Build the ***shell_hub*** by changing to the ***shell_hub*** directory and build the image: `docker build -t shell_hub .`
- Run your ***shell_hub*** container: `docker run -d -p 5000:5000 -v /var/run/docker.sock:/var/run/docker.sock --name shell_hub shell_hub`
- Visit the ***shell_hub*** url: `http://localhost:5000`

You can now request a shell, it will then responde with the port that its running on. You can then ssh to that shell with username `ubuntu` and the password you entered on the website and the port that its running on. 
