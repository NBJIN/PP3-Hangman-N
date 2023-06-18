"""
score.py holds code for displaying the hangman
"""


def show_hangman(lives):
    """
    Function to display hangman
    """
    stages = [
        # Stage 1 : head, arm1, arm2, stomach, leg1, leg2
        """
        ---------
        |  / |
        | /  O
        |  \\ //
        |    |
        |  // \\
        |
        """,
        # Stage 2 : head, arm1, arm2, stomach, leg1
        """
        ---------
        | /  |
        |/   O
        |  \\ //
        |    |
        |  //
        |
        """,
        # Stage 3 : head, arm1, arm2, stomach
        """
        ---------
        | /  |
        |/   O
        |  \\ //
        |    |
        """,
        # Stage 4 : head, arm1, arm2
        """
        ---------
        | /  |
        |/   O
        |  \\ //
        """,
        # Stage 5 : head, arm1
        """
        ---------
        | /  |
        |/   O
        |  \\
        """,
        # Stage 6 : head
        """
        ---------
        | /  |
        |/   O
        """,
        # Stage 7
        """
        ---------
        | /  |
        """
    ]
    return stages[lives]


WELCOME = """

 \\ \\         /     |
  \\ \\  \\   /  _ \\  |   __|   _ \\   __ `__ \\    _ \\
   \\ \\  \\ /   __/  |  (     (   |  |   |   |   __/
    \\_/\\_/  \\___| _| \\___| \\___/  _|  _|  _| \\___|



  |               |   |
  __|   _ \\       |   |   _` |  __ \\    _` |  __ `__ \\    _` |  __ \\
  |    (   |      ___ |  (   |  |   |  (   |  |   |   |  (   |  |   |
 \\__| \\___/      _|  _| \\__,_| _|  _| \\__, | _|  _|  _| \\__,_| _|  _|
                                      |___/

\n

--------
|  / |
| /  O
|  \\\\ //
|    |
|  // \\\\
|
"""


WIN = """
__   __           __        ___
\\ \\ / ___  _   _  \\ \\      / (_) __ _
 \\ V / _ \\| | | |  \\ \\ /\\ / /| |/ _` |
  | | (_) | |_| |   \\ V  V / | | | | |
  |_|\\___/|_.__/     \\_/\\_/  |_|_| |_|

"""

LOOSE = """


 \\ \\   /
  \\   /  _ \\   |   |
     |  (   |  |   |
    _| \\___/  \\__,_|

  |\n
  |       _ \\    _ \\    __|   _ \\
  |      (   |  (   | \\__ \\   __/
 _____| \\___/  \\___/  ____/ \\___|

"""

menu = [
    "Choose 1 To Start Playing The Hangman Game"
    "Choose 2 To Choose The Desired Level"

]
