**Flask Application Design**

**HTML Files**

* **index.html:**
    - Landing page for data input and visualization.
    - Contains forms for entering player and coach data.
    - Displays charts and tables summarizing coaching style and injury load data.

* **player-data.html:**
    - Form for entering player profiles, including name, team, and injury history.

* **coach-data.html:**
    - Form for entering coach profiles, including name, coaching style, and team history.

* **coaching-actions.html:**
    - Form for recording coaching actions, such as training drills or lineup changes.

* **game-results.html:**
    - Table displaying game results, including win/loss records and injury occurrences.

**Routes**

* **home:**
    - Default route that displays the landing page (index.html).

* **add_player:**
    - POST route that handles player data submission and adds the data to a database.

* **add_coach:**
    - POST route that handles coach data submission and adds the data to a database.

* **add_coaching_action:**
    - POST route that handles coaching action submissions and stores them in a database.

* **add_game_result:**
    - POST route that handles game result submissions and updates the database accordingly.

* **show_data:**
    - GET route that retrieves data from the database and displays it on the landing page.

* **charts:**
    - GET route that generates charts and tables based on the data in the database.