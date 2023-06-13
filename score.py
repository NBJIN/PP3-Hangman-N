def show_hangman(lives):
    """
    Function to display hangman
    """
    stages = [  # Stage 1 : head, arm1, arm2, stomach, leg1, leg2
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
