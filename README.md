#FireFlyCrypto

A unique bot for earning cryptocurrency for communicating on Telegram

![FireFly Crypto](https://i.ibb.co/jJhpkSm/fflbanner.jpg)

## Description

FireFly Crypto is a unique Telegram bot designed to create an innovative and exciting communication environment on Telegram. Thanks to its advanced features and capabilities, FireFly Crypto provides users with a wide range of tools to earn cryptocurrency for active participation in dialogues.

## Technologies used

- Python is the programming language in which the bot is written.
- Aiogram is an asynchronous framework for developing bots.
- Django is a web framework used to create the administrative panel and other web interfaces.
- Docker - to containerize the application and simplify its deployment.
- MongoDB - for storing data about users, messages and tasks.
- PostgreSQL - for storing Sentry logs and errors.
- Redis - for storing cache, temporary data, queues.
- Sentry is a monitoring and error tracking platform used to detect and resolve problems in an application.

## Application modules

### admin_panel

A directory with administrative panels for managing bots. Includes an admin interface where you can manage bot settings, view statistics, create and delete tasks, etc.

### bot_counter

Submodule with the source code of the counter bot. Includes files for launching the bot, localization settings, database connection and other components necessary for the bot to function.

### bot_main

Submodule with the main bot. Includes the main bot classes, command handlers, database logic and other auxiliary functions.

### data

Directory with configuration and localization files. Includes configuration files for bots, message localization settings, and other data used by the application.

### models

A directory containing data models used in the project. Includes database classes, which are data models for storing information about users, messages, tasks, etc.

### utils

Utilities and auxiliary functions. Includes functions for logging, exception handling, sending notifications and other auxiliary components.

## Instructions for running with Docker Compose

1. Make sure you have Docker and Docker Compose installed.
2. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/Arnon-hs/FireFly.git
3. Go to the directory with the project
    ```bash
     cd FireFly
4. Create a .env file and specify the necessary environment variables
5. Run containers with Docker Compose
    ```bash
    docker-compose up --build -d

## Recommendations for developers

1. Periodically update the project dependencies, monitor the updates of the libraries and tools used.
2. Document your code so that other developers can easily understand its structure and logic.
3. Test your code before deploying it to a production server to avoid possible problems with the bot’s operation.
4. Maintain current project documentation, including installation, usage, and update instructions.

## License

All code and files in this repository are protected by copyright. Use, copying, distribution and modification without permission of the copyright owner is prohibited.

## Contacts

To contact the developer or obtain additional information about the application, you can contact the following contacts:

- Email: arnon.hs.btc@gmail.com
- Telegram: @whiterose_sc