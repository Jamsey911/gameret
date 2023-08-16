# eCommerce: gameret

![Am I Responsive](#)

**Developer: James Lynch**

💻 [Visit live website](#)  
(Ctrl + click to open in new tab)



## Table of Contents
  - [Executive Summary](#executive-summary)
     - [Market Analysis](#market-analysis)
     - [Marketing and Sales Strategy](#marketing-and-sales-strategy)
     - [Operations and Management](#operations-and-management)
     - [Financial Plan](#financial-plan)
     - [Conclusion](#conclusion)
  - [Marketing](#marketing)
     - [Social Media](#social-media)
     - [Mailing List](#mailing-list)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [AWS](#aws)
      - [Database](#database)
      - [Models](#models)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

<hr>
## User Stories


| User Story ID                  | As A/AN             | I CAN...                                                | SO THAT I CAN...                                          |
|--------------------------------|---------------------|---------------------------------------------------------|-----------------------------------------------------------|
| Registration and User Accounts ||||
| 1 | Shopper / Site User | register for an account | have an account and view my profile |
| 2 | Shopper / Site User | login and logout | have an account with my information stored for fast usage |
| 3 | Shopper / Site User | recover my password | set a new password if I forgot it                         |
| 4 | Shopper / Site User | receive an email confirmation after registration| be notified registration was successful                   |
| 5 | Shopper / Site User | have a profile | store my information for faster checkouts in the future |
| Viewing and navigation ||||
| 6 | Shopper / Site User | navigate across the site | can access all parts of the site                          |
| 7 | Shopper / Site User | use a navbar, footer, and social icons | navigate the site, access menus, and access socials       |
| 8 | Shopper / Site User | be notified of my actions | be aware the action was completed successfully or not     |
| 9 | Shopper / Site User | see my login status | know if I am logged in or not |
| 10 | Shopper / Site User | visit the shop| view all products available |
| 11 | Shopper / Site User | view my basket and total cost at any time | so I am aware of what I am buying and it's cost |
| 12 | Shopper / Site User | view a list of products | select a product to purchase                              |
| 13 | Shopper / Site User | view an individual product details | view a more detailed view of the product |
| 14 | Shopper / Site User | view a list of golf courses | select a golf course I want to play on |
| 15 | Shopper / Site User | view individual golf course details | see more detailed information about it |
| 16 | Shopper / Site User | view a list of tee times available for each golf course | select a date and time to play |
| Sorting and Searching ||||
| 17 | Shopper / Site User | search for a product by name or description | find a certain product                                    |
| 18 | Shopper / Site User | see my search results | only see what I am searching for |
| 19 | Shopper / Site User | sort by category | select products of a certain category |
| 20 | Shopper / Site User | sort by price low to high and high to low | view products according to my budget |
| 21 | Shopper / Site User | select only available dates/times | I can only purchase available tee slots |
| Purchasing and Checkout ||||
| 22 | Shopper / Site User | use a card as the payment method | complete my purchase                                      |
| 23 | Shopper / Site User | select the size and quantity of a product | select a size and quantity to my needs |
| 24 | Shopper / Site User | view items in my basket | be aware of what I am buying and it's cost |
| 25 | Shopper / Site User | adjust item quantity in my basket | increase or reduce item count according to my needs |
| 26 | Shopper / Site User | receive order confirmation | be notified of a successful order |
| 27 | Shopper / Site User | receive email confirmation | have a record of my purchase |
| Admin and Store Management | | | |
| 28 | Store Owner / Admin | add a product | add new products to the shop |
| 29 | Store Owner / Admin | edit a product | edit existing products in the shop |
| 30 | Store Owner / Admin | delete a product | delete existing products from the shop |
| 31 | Store Owner / Admin | add a golf club | add a golf club to the site |
| 32 | Store Owner / Admin | edit a golf club |edit an existing golf club on the site|
| 33 | Store Owner / Admin | delete a golf club | delete existing golf club from the site |
| 34 | Store Owner / Admin | add a tee time | add a tee time to a golf club |
| 35 | Store Owner / Admin | edit a tee time | edit an existing tea time on a golf club |
| 36 | Store Owner / Admin | delete a tee time | delete a tee time from a golf club |
| 37 | Shopper / Site User | book a tee time | book a tee time for a golf club |
| 38 | Shopper / Site User | edit a tee time booking | edit a tee time booking as I alter my schedule to play golf |
| 39 | Shopper / Site User | delete a tee time booking | delete a tee time booking if I need to cancel |
| 40 | Shopper / Site User | view my tee time bookings | view my tee time bookings |