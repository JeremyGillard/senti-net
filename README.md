# Senti-net

The sentinel of your personal network

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

## Table of content

**_[Description](#description)_**  
**_[Project Structure](#project-structure)_**  
**_[Technologies](#technologies)_**  
**_[Setup](#setup)_**

## Description

Big refactoring. I am not satisfied by the current structure of the project for many reasons:

- python psycopg2 lib is pretty good but a little too much low level and I would like to try an orm. In addition, I am actually concentrating my study time on javascript and this is why i would prefer to use a javascript orm. (I've heard a lot of good things about Knex.js)
- In Addition, my current relational database schema is very very bad.
- Even if my initial idea was to allow to retrieve those data from an rest api (the reason of strapi presence), I would also prefer to allow to a client to retrieve data in real time. I think about Socket.io.
  I will continue to do some research but I think that I will try a new architecture.

I will continue to use python for network packet sniffing with Scapy library.
This sniffer will publish his results in a redis database.
Then I will create 3 "differents" javascript programs. One subscriber to store those data in a postgresql database with help of Knex.js and serve them by a rest api. One subscriber to allow client app to retrieve those data in real time. And a last one in python or in javascript to allow to the server user to display those information in the console.

## Project Structure

## Technologies

## Setup

## Notes
