# BUILDING 'HOME SWEET HOME' USING DJANGO

> https://github.com/ingafter60/home-sweet-home

## 1. Environment Setup

	> 1.2 Creating our Env and Installing Django 
	> 1.3 Creating the Github Repository 

## 2. Introduction to Django

	> 2.0 Creating a Django Project 
	> 2.6 Creating the App: users

## 3. User App

	> 3.3 Finishing User Model 
	> 3.4 Falling in Love with Admin Panel 
	> 3.5 UserAdmin + CustomAdmin 
	> 3.6 Modified README.me

## 4. Core App & Rooms App

	> 4.1 Create Core App
	> 4.2 Create Rooms App
	> 4.3 Register Core App and Rooms App to settings and modified settings file
	> 4.4 Create Abstrac model 'TimeStampedModel'
	> 4.5 Install django-countries and register it to settings
	> 4.6 Modify core model to use auto_now and auto_now_add
	> 4.7 Add fields to Room model & run migration
	> 4.8 Add ManyToMany Rel between room and room type
	> 4.9 Add to Room model: on_delete behavior, and fields for: Amenity, Faciliy, HouseRule by using AbstracItem
	> 4.10 Add verbose_name and verbose_name_plural
	> 4.11 Make amenities, facilities, and house_rules fields blank true
	> 4.12 Create Photo class and add relationship with room
	> 4.15 Use string for class  name
	> 4.16 Register Photo to admin and add 'notes' to each of registered class

## 5. Reviews

	> 5.1 Create a new app 'reviews' and register it to settings
	> 5.2 Create Review model, run migration and Register Review model to admin 
		mysql> desc reviews_review;                                             
		+---------------+-------------+------+-----+---------+----------------+ 
		| Field         | Type        | Null | Key | Default | Extra          | 
		+---------------+-------------+------+-----+---------+----------------+ 
		| id            | int(11)     | NO   | PRI | NULL    | auto_increment | 
		| created       | datetime(6) | NO   |     | NULL    |                | 
		| updated       | datetime(6) | NO   |     | NULL    |                | 
		| review        | longtext    | NO   |     | NULL    |                | 
		| accuracy      | int(11)     | NO   |     | NULL    |                | 
		| communication | int(11)     | NO   |     | NULL    |                | 
		| cleanliness   | int(11)     | NO   |     | NULL    |                | 
		| location      | int(11)     | NO   |     | NULL    |                | 
		| check_in      | int(11)     | NO   |     | NULL    |                | 
		| value         | int(11)     | NO   |     | NULL    |                | 
		| room_id       | int(11)     | NO   | MUL | NULL    |                | 
		| user_id       | int(11)     | NO   | MUL | NULL    |                | 
		+---------------+-------------+------+-----+---------+----------------+ 
		12 rows in set (0.03 sec)                                               

	> 5.3 Add string method to Review model to show the review in admin panel


## 6. Reservations

	> 6.1 Create a reservations app and register it to settings
	> 6.2 Create a Reservation model, setting the time (datetimg, timezone, TIME_ZONE = 'UTC') and run migration
	  Note: Reservation basically constitute of: 
	  	- the room
	  	- the guest
	  	- check in
	  	- check out
	  	- status (like: pending, confirm, cancel)
	  	mysql> desc reservations_reservation;                                 
		+-----------+-------------+------+-----+---------+----------------+   
		| Field     | Type        | Null | Key | Default | Extra          |   
		+-----------+-------------+------+-----+---------+----------------+   
		| id        | int(11)     | NO   | PRI | NULL    | auto_increment |   
		| created   | datetime(6) | NO   |     | NULL    |                |   
		| updated   | datetime(6) | NO   |     | NULL    |                |   
		| status    | varchar(12) | NO   |     | NULL    |                |   
		| check_in  | date        | NO   |     | NULL    |                |   
		| check_out | date        | NO   |     | NULL    |                |   
		| guest_id  | int(11)     | NO   | MUL | NULL    |                |   
		| room_id   | int(11)     | NO   | MUL | NULL    |                |   
		+-----------+-------------+------+-----+---------+----------------+   
		8 rows in set (0.00 sec)    
	> 6.3 Add string method to Reservation model to show the reservation in admin panel, and register the model to admin	                                          

## 7. Lists

	> 7.1 Create lists app and register it to settings
	> 7.2 Create List model, run migration and register it to admin
	mysql> desc lists_list;
	+---------+-------------+------+-----+---------+----------------+
	| Field   | Type        | Null | Key | Default | Extra          |
	+---------+-------------+------+-----+---------+----------------+
	| id      | int(11)     | NO   | PRI | NULL    | auto_increment |
	| created | datetime(6) | NO   |     | NULL    |                |
	| updated | datetime(6) | NO   |     | NULL    |                |
	| name    | varchar(80) | NO   |     | NULL    |                |
	| user_id | int(11)     | NO   | UNI | NULL    |                |
	+---------+-------------+------+-----+---------+----------------+
	5 rows in set (0.00 sec)

## 8. Conversations

	> 8.1 Create conversations app and register it to settings
	> 8.2 Creare Reservation model with ManyToMay rel with User, run migration and register it to admin
	> 8.3 Creare Message model with OneToMay rel with User and with Conversation, run migration and register it to admin
	> 8.4 Fixing error: turn the method of the class Conversation to string
	mysql> desc conversations_conversation;
	+---------+-------------+------+-----+---------+----------------+
	| Field   | Type        | Null | Key | Default | Extra          |
	+---------+-------------+------+-----+---------+----------------+
	| id      | int(11)     | NO   | PRI | NULL    | auto_increment |
	| created | datetime(6) | NO   |     | NULL    |                |
	| updated | datetime(6) | NO   |     | NULL    |                |
	+---------+-------------+------+-----+---------+----------------+
	3 rows in set (0.00 sec)

	mysql> desc conversations_message;
	+-----------------+-------------+------+-----+---------+----------------+
	| Field           | Type        | Null | Key | Default | Extra          |
	+-----------------+-------------+------+-----+---------+----------------+
	| id              | int(11)     | NO   | PRI | NULL    | auto_increment |
	| created         | datetime(6) | NO   |     | NULL    |                |
	| updated         | datetime(6) | NO   |     | NULL    |                |
	| message         | longtext    | NO   |     | NULL    |                |
	| conversation_id | int(11)     | NO   | MUL | NULL    |                |
	| user_id         | int(11)     | NO   | MUL | NULL    |                |
	+-----------------+-------------+------+-----+---------+----------------+
	6 rows in set (0.00 sec)
	> 8.5 Modified README file