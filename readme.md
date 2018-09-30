# Python Wrapper for Github Gist
![](https://img.shields.io/pypi/pyversions/Django.svg)
![](https://img.shields.io/badge/pypi-v1-green.svg)
![](https://img.shields.io/github/license/mashape/apistatus.svg)
---

This Script is a wrapper for pushing gist to github using terminal. Apart from uploading, this script also gives option to view, delete and delete all (in case you get in love with the script and ends up uploading everything).


## Installation
---
`pip install go-gist`

## Usage
---
You need to get an API Token from Github.  [Tutorial Here.](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/#creating-a-token) 
 _Note: In the scopes section, select only gist._


This API token will be saved along with your username (currently it's in plain text, but working on encrypting it), to allow faster access to the script.

You can type `go-gist -h` to get a list of all the commands.

## List of Commands
---


`go-gist -u /path/to/file` 

   Uploads FILE to the GITHUB


`go-gist -l` 

   Shows the LIST of all the GIST 


`go-gist -d name-of-gist`

   DELETES the gist of the GIVEN NAME 


`go-gist -da`

   DELETES all the GISTS
