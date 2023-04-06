import getpass

# Define a function for the introduction of the game
def introduction():
    print("Welcome to 'It Starts With Us', a choice-based text RPG game.")
    print("In this game, you will be making choices that will determine the outcome of the story.")
    print("You will need to register or log in to play the game.")
    print("Let's get started!\n")

# Define a function for the login and registration page
def login_registration():
    # Prompt the user to choose between login and registration
    print("1. Login")
    print("2. Register")
    choice = input("Enter your choice (1 or 2): ")
    
    # Define a dictionary for the user accounts
    users = {}
    
    # If the user chooses to register
    if choice == "2":
        print("Please enter your details to register.")
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        users[username] = password
        print("Registration successful!")
    
    # If the user chooses to log in
    elif choice == "1":
        print("Please enter your credentials to log in.")
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        while True:
            if username in users and users[username] == password:
                print("Login successful!")
                break
            else:
                print("Incorrect username or password.")
                username = input("Enter your username: ")
                password = getpass.getpass("Enter your password: ")
    
    # If the user enters an invalid choice
    else:
        print("Invalid choice.")
        login_registration()

# Define a function for the first chapter of the story
def chapter1():
    print("Chapter 1: The Beginning")
    print("You are Sarah, a college student. It's Friday night and you're at a party.")
    print("You've had a few drinks and you're feeling a bit tipsy.")
    print("You notice a guy trying to hit on you.")
    print("What do you do?")
    print("1. Flirt back.")
    print("2. Politely decline.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("The guy takes advantage of your drunken state.")
        print("You wake up the next morning feeling ashamed and violated.")
        print("Game over.")
    elif choice == "2":
        print("The guy respects your decision and moves on.")
        print("You continue to enjoy the party and have a good time.")
        print("Congratulations, you have completed chapter 1!")
        chapter2()
    else:
        print("Invalid choice.")
        chapter1()

# Define a function for the second chapter of the story
def chapter2():
    print("Chapter 2: The Consequences")
    print("You wake up the next morning feeling refreshed.")
    print("You check your phone and see that you have missed calls and messages from your friends.")
    print("Apparently, a girl went missing from the same party you were at last night.")
    print("What do you do?")
    print("1. Go to the police.")
    print("2. Ignore it and carry on with your day.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("You go to the police and provide them with any information")
        print("The police are able to track down the girl's whereabouts and rescue her.")
        print("You feel relieved and proud of yourself for doing the right thing.")
        print("Congratulations, you have completed chapter 2!")
        chapter3()
    elif choice == "2":
        print("The girl's body is found a few days later.")
        print("You feel guilty and wonder if things would have been different if you had taken action.")
        print("Game over.")
    else:
        print("Invalid choice.")
        chapter2()

# Define a function for the third chapter of the story
def chapter3():
    print("Chapter 3: The Journey")
    print("You are now more aware of the consequences of your actions and the impact they can have on others.")
    print("You decide to make a change and take action whenever you see something wrong happening.")
    print("Congratulations, you have completed the game!")
    print("Thank you for playing 'It Starts With Us'.")
    print("Goodbye!")
# Define a function for the fourth chapter of the story
def chapter4():
    print("Chapter 4: The Awakening")
    print("As you become more involved in standing up against injustice, you begin to realize that there are many people out there who share your values.")
    print("You connect with like-minded individuals and start to work together to create positive change in your community.")
    print("What do you do?")
    print("1. Continue to work with your group to make a bigger impact.")
    print("2. Take a break from activism to focus on your personal life.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("Together, you make a significant impact and inspire others to join your cause.")
        print("Congratulations, you have completed chapter 4!")
        chapter5()
    elif choice == "2":
        print("You take a break from activism and focus on your personal life.")
        print("Although you miss the work you were doing, you feel refreshed and ready to get back to it soon.")
        print("Congratulations, you have completed chapter 4!")
        chapter5()
    else:
        print("Invalid choice.")
        chapter4()

# Define a function for the fifth chapter of the story
def chapter5():
    print("Chapter 5: The Opposition")
    print("Your movement gains traction and starts to attract attention from those who oppose your message.")
    print("You face challenges and opposition, but you remain steadfast in your beliefs.")
    print("What do you do?")
    print("1. Keep fighting for your cause, even in the face of adversity.")
    print("2. Give up and walk away from the movement.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("Through perseverance and determination, you overcome obstacles and continue to make progress.")
        print("Congratulations, you have completed chapter 5!")
        chapter6()
    elif choice == "2":
        print("You feel defeated and discouraged, but you know that your work has made a difference.")
        print("Although you are no longer actively involved in the movement, you continue to support it in your own way.")
        print("Congratulations, you have completed chapter 5!")
        chapter6()
    else:
        print("Invalid choice.")
        chapter5()

# Define a function for the sixth chapter of the story
def chapter6():
    print("Chapter 6: The Future")
    print("Your movement has now become a powerful force for change.")
    print("You have inspired a generation of young people to take action and make a difference in the world.")
    print("What do you do?")
    print("1. Continue to work with the movement and make an even bigger impact.")
    print("2. Step back and let others take the lead.")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        print("As you look towards the future, you realize that there is still much work to be done, but you are filled with hope and optimism.")
        print("Congratulations, you have completed the game!")
        print("Thank you for playing 'It Starts With Us'.")
        print("Goodbye!")
    elif choice == "2":
        print("You step back and let others take the lead.")
        print("Although you are no longer actively involved in the movement, you know that your work has made a difference and that others will continue to carry the torch.")
        print("Congratulations, you have completed the game!")
       

# Call the functions to run the game
introduction()
login_registration()
chapter1()

