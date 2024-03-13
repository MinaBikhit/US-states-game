import turtle
import pandas

screen = turtle.Screen()                              # screen object from turtle lib
screen.title("U.S. States Game")                      # choosing a title for the screen
image = "blank_states_img.gif"                        # an image variable to store the path to the image
screen.addshape(image)                                # adding the image to the shapes in the screen
turtle.shape(image)                                   # using the shape method to turn the image in into the background

data = pandas.read_csv("50_states.csv")               # using pandas lib to load the csv file that contains the names and coordinates of the states
states = data.state.to_list()                         # a state list created from the state column in the dataframe

answers = []                                          # an empty answer list to contain the answers
remaining_states = []                                 # a list to contain the remaining states


while len(answers) < 50:                              # a while loop to keep the game going until all states are named
    # create a prompt to as the user for input (name of a state)
    answer_state = turtle.textinput(title=f"{len(answers)}/50 States Correct", prompt="Name a state: ").title()

    # setting an exit value to exit the game and then adds the remaining states to the remaining states list
    if answer_state.lower() == "exit":
        for state in states:
            if state not in answers:
                remaining_states.append(state)
        break


    # checking if the user input is a state name and then using turtle methods to display the state name on the map
    if answer_state in states:
        ans = data[data.state == answer_state]
        ans_turtle = turtle.Turtle()                # create an answer turtle object to display te name
        ans_turtle.hideturtle()                     # hide turtle symbol
        ans_turtle.penup()                          # penup to avoid turtle drawing lines
        ans_turtle.goto(int(ans.x.item()), int(ans.y.item()))    # setting the turtle to go to the coordinates imported from the csv file
        ans_turtle.write(answer_state)     # using the write method to display the name in the coordinates set previously
        answers.append(answer_state)       # adding the answer to the answers list to be checked at the end of the game


remaining_state_data = pandas.DataFrame(remaining_states)       # a variable to store the pandas dataframe of the remaining states list
remaining_state_data.to_csv("states_to_learn.csv")           # exporting the remaining states to csv file for the user to check
