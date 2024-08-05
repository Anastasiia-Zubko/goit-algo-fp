import turtle

# Function to draw the Pythagoras tree
def draw_pythagoras_tree(t, branch_length, depth):
    if depth == 0:
        return

    # Draw the trunk
    t.forward(branch_length)

    # Save the current position and heading
    pos = t.position()
    heading = t.heading()

    # Draw the left branch
    t.left(45)
    draw_pythagoras_tree(t, branch_length * 0.6, depth - 1)

    # Return to the trunk position
    t.setposition(pos)
    t.setheading(heading)

    # Draw the right branch
    t.right(45)
    draw_pythagoras_tree(t, branch_length * 0.6, depth - 1)

    # Return to the trunk position
    t.setposition(pos)
    t.setheading(heading)

def main():
    # Set up the screen and the turtle
    screen = turtle.Screen()
    screen.title("Pythagoras Tree Fractal")
    t = turtle.Turtle()
    t.speed(0)  
    t.left(90)  

    # Get the recursion depth from the user
    depth = int(screen.textinput("Pythagoras Tree", "Enter the recursion depth:"))

    # Draw the Pythagoras tree
    t.penup()
    t.goto(0, -200)
    t.pendown()
    draw_pythagoras_tree(t, 100, depth)

    # Hide the turtle and display the window
    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
