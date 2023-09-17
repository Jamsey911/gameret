# eCommerce: gameret

![Am I Responsive](docs/amiresponsive.PNG)

**Developer: James Lynch**

💻 [Visit live website](https://gameret-e526d0bda5ef.herokuapp.com/)  
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

## Business Plan  
### Executive Summary:

Gameret is a web-based platform that video game lovers can view and purchase old and new products in the video game industry. It offers a convenient ecommerce shop with a easy-to-use platform for purchasing products as well as a contact page for inquiries and support.

Our target market is video game lovers of all ages. We aim to differentiate ourselves from competitors by offering a more easy to use and intuitive platform, as well varied scale of products.

Overall, Gsmeret aims to become the go-to destination for gamers looking to purchase video game products, as well as a trusted and reliable platform to use.

### Market Analysis:

The gaming industry is a multi-billion euro industry, with a large and dedicated consumer base. While traditional methods of purchasing video game related items (such as travelling to shop to see what is offered in-person) are still popular, there is a growing trend towards online ecommerce platforms. This shift towards online ecommerce presents a significant opportunity for Gameret to establish itself as a leading player in the market.

In terms of competition, Gameret will face other online ecommerce platforms as well as traditional methods of purchasing. However, we believe that our user-friendly platform and wide range of products in our ecommerce shop will differentiate us from competitors and make us a preferred choice for gamers.

In terms of target market, our primary focus will be video game lovers of all ages. We will also target collectors and online groups as potential customers for our software, as these organizations are constantly seeking rare and collectable pieces.

### Marketing and Sales Strategy:

Gameret will utilize a combination of online and offline marketing tactics to reach our target market. These tactics will include:

Online advertising through Google AdWords and social media platforms such as Facebook and Instagram
Content marketing through our blog and email newsletter
Partnerships and sponsorships with video-game related brands
Public relations efforts to generate press coverage and raise awareness of Gameret

### Operations and Management:

Gameret will be operated and managed by a small team of experienced professionals. The team will consist of a CEO, CTO, and marketing and sales staff.

In terms of operations, we will utilize a cloud-based platform to host the website and software, as well as a payment gateway for processing transactions. We will also utilize third-party fulfillment centers to handle the storage, packing, and shipping of products purchased through our ecommerce shop.

#### Financial Plan:

Gameret will generate revenue through the sale of products in our ecommerce shop. In terms of expenses, the main cost will be marketing and advertising efforts to drive traffic to the website and attract customers. We will also incur expenses related to the development.

In terms of financing, Gameret will initially be funded through a combination of personal investment and a small seed round of funding. As the business grows, we will explore additional funding options such as venture capital or a larger round of financing.

In terms of projections, we anticipate strong growth in both revenue streams over the first few years of operation. In the first year, we expect to generate €100,000 in revenue coming from product sales. In the second year, we expect to see revenue increase to €200,000 coming from product sales. By the third year, we anticipate revenue to reach €300,000 coming from software sales.

In terms of profitability, we expect to break even within the first year of operation and achieve profitability in the second year.

### Conclusion:

Gameret is a unique and innovative platform that aims to connect gamers with new and rare items, while also offering a convenient and user-friendly platform for purchasing video game related products. With strong growth potential and a clear revenue model, we believe that Gameret has the potential to become a leading player in the golf industry.
##### Back to [top](#table-of-contents)<hr>

## Marketing  

### Social Media  
The web app "Gameret" has a presence on both Facebook. The Facebook page serves as a platform to promote upcoming events, post updates on the latest features, and share user-generated content. This social media account allow users to stay informed and connected with the "Gameret" community.

[Facebook Mockup](docs/facebook/facebook_wireframe.png)  
[Facebook Suspended Account](docs/facebook/facebook_suspend.PNG)

### Mailing List  

Gameret uses Mailchimp to manage its mailing list. By joining the mailing list, users will receive updates on new features, upcoming events, and exclusive promotions. The process to join the mailing list is simple, users just need to provide their email address on the website, and they will start receiving email updates. Mailchimp allows the "gameret" team to segment the mailing list, personalize emails and track the success of email campaigns. By joining the mailing list, users will stay informed and be the first to know about new developments in the "gameret" web app.  

<details><summary>See Image</summary>

![Mailchimp](docs/mailchimp.PNG)  

</details> 

## User Goals

- To easily and conveniently purchase games, consoles and console accessories 
- To browse and purchase a wide range of gaming products through the eCommerce shop
- To access the latest news and tips on gaming through various social media links
- To contact the Gameret team with any inquiries or support needs through the contact page

## Site Owner Goals

- Generate revenue through the sale of products in the ecommerce shop
- Build a strong and loyal customer base by providing an easy-to-use platform and high-quality products
- Establish Gameret as a trusted and respected brand in the gaming industry
- Achieve profitability and sustain long-term growth
<hr>


## User Experience

### Target Audience
- Gaming enthusiasts who are interested in gaming related products.
- Gaming Collecters who look to find rare or valuable piceses.
- Individuals who are looking for information and resources related to speicic gaming products.
- Any individual who is interested in purchasing gaming related products through the app's ecommerce shop.

### User Requirements and Expectations

- Good customer service
- A user-friendly interface
- Fully responsive
- Accessible
- A welcoming design
- Contact information
- Accessibility
- Competitive prices
- Social media


##### Back to [top](#table-of-contents)<hr>

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
| 14 | Shopper / Site User | view a list of consoles | select a console I want to purchase |
| 15 | Shopper / Site User | view a list of games | select a game I want to purchase |
| 16 | Shopper / Site User | view a list of accessories | select an accessory I want to purchase |
| Sorting and Searching ||||
| 17 | Shopper / Site User | view individual consoles | see more detailed information about it |
| 18 | Shopper / Site User | view individual games | see more detailed information about it |
| 19 | Shopper / Site User | view individual accessories | see more detailed information about it |
| 20 | Shopper / Site User | search for a product by name or description | find a certain product                                    |
| 21 | Shopper / Site User | see my search results | only see what I am searching for |
| 22 | Shopper / Site User | sort by price low to high and high to low | view products according to my budget |
| 23 | Shopper / Site User | Sort products in alphabetical order | search products by letter |
| Purchasing and Checkout ||||
| 24 | Shopper / Site User | use a card as the payment method | complete my purchase                                      |
| 25 | Shopper / Site User | select the quantity of a product | select a quantity that suites my needs |
| 26 | Shopper / Site User | view items in my basket | be aware of what I am buying and it's cost |
| 27 | Shopper / Site User | adjust item quantity in my basket | increase or reduce item count according to my needs |
| 28 | Shopper / Site User | receive order confirmation | be notified of a successful order |
| 29 | Shopper / Site User | receive email confirmation | have a record of my purchase |
| Admin and Store Management | | | |
| 30 | Store Owner / Admin | add a product | add new products to the shop |
| 31 | Store Owner / Admin | edit a product | edit existing products in the shop |
| 32 | Store Owner / Admin | delete a product | delete existing products from the shop |
| 33 | Store Owner / Admin | view messages sent in by public | gather feedback and converse its with its community|
