import turtle as t
# w = forwards
# s = Backwards
# a = Counter-Clockwise
# d = clockwise
# c = clear drawing

tim = t.Turtle()
tim.speed("fastest")
screen = t.Screen()

def m_forward():
    tim.forward(10)
def m_backward():
    tim.backward(10)
def m_counter_clock():
    tim.left(10)
def m_clockwise():
    tim.right(10)
def clear_screen():
    tim.clear()
    tim.penup
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(m_forward, "w")
screen.onkeypress(m_counter_clock, "a")
screen.onkeypress(m_clockwise, "d")
screen.onkeypress(m_backward, "s")
screen.onkeypress(clear_screen, "c")
t.mainloop()

