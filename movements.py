import cv2
from classes import Supermarket, Customer

def move_to(customer, supermarket, target_y, target_x):
    # up
    if target_y < customer.y and target_x is customer.x:

        while not customer.y == target_y:
            customer.vy = -10
            customer.vx = 0
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break
    # down
    elif target_y > customer.y and target_x is customer.x:

        while customer.y < target_y:
            customer.vy = 10
            customer.vx= 0
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break
    # left
    elif target_x < customer.x and target_y is customer.y:

        while customer.x > target_x:
            customer.vx = -10
            customer.vy = 0
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break
    # right
    else:

        while customer.x < target_x:
            customer.vx = 10
            customer.vy = 0
            supermarket.draw()
            supermarket.render()
            customer.move()
            if cv2.waitKey(0) == ord('q'):
                break

# Functions naming: Start_Destination

def entrance_fruit(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 250, customer.x) # e to fu

def entrance_spices(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # e to fu
    move_to(customer, supermarket, customer.y, 550) # fu to su
    move_to(customer, supermarket, 250, customer.x) #  su to s

def entrance_dairy(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # e to fu
    move_to(customer, supermarket, customer.y, 315) # su to du
    move_to(customer, supermarket, 250, customer.x) # du to d

def entrance_drinks(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # e to fu
    move_to(customer, supermarket, customer.y, 85) # fu to ru
    move_to(customer, supermarket, 250, customer.x) # ru to r

def fruit_spices(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # f to fu
    move_to(customer, supermarket, customer.y, 550) # fu to su
    move_to(customer, supermarket, 250, customer.x) #  su to s

def fruit_dairy(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # f to fu
    move_to(customer, supermarket, customer.y, 315) # su to du
    move_to(customer, supermarket, 250, customer.x) # du to d

def fruit_drinks(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # f to fu
    move_to(customer, supermarket, customer.y, 85) # du to ru
    move_to(customer, supermarket, 250, customer.x) # ru to r

def spices_fruit(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x)# s to su
    move_to(customer, supermarket, customer.y, 770)# su to fu
    move_to(customer, supermarket, 250, customer.x)# fu to f

def spices_dairy(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x)# s to su
    move_to(customer, supermarket, customer.y, 315)# su to du
    move_to(customer, supermarket, 250, customer.x)# du to d

def spices_drinks(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x)# s to su
    move_to(customer, supermarket, customer.y, 85) # du to ru
    move_to(customer, supermarket, 250, customer.x) # ru to r

def dairy_fruit(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # d to du
    move_to(customer, supermarket, customer.y, 770)# su to fu
    move_to(customer, supermarket, 250, customer.x)# fu to f

def dairy_spices(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # d to du
    move_to(customer, supermarket, customer.x, 550) # du to su
    move_to(customer, supermarket, 250, customer.x) #  su to s

def dairy_drinks(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # d to du
    move_to(customer, supermarket, customer.y, 85) # du to ru
    move_to(customer, supermarket, 250, customer.x) # ru to

def drinks_fruit(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # r to ru
    move_to(customer, supermarket, customer.y, 770)# ru to fu
    move_to(customer, supermarket, 250, customer.x)# fu to

def drinks_spices(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # r to ru
    move_to(customer, supermarket, customer.y, 550) # ru to su
    move_to(customer, supermarket, 250, customer.x) # su to s

def drinks_dairy(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    move_to(customer, supermarket, 60, customer.x) # r to ru
    move_to(customer, supermarket, customer.y, 315) # ru to du
    move_to(customer, supermarket, 250, customer.x) # du to d

def to_checkout(start_coord,vv):
    customer = Customer(start_coord, vv)
    supermarket = Supermarket([customer])
    if customer.x == 770: # fruit
        move_to(customer, supermarket, 450, customer.x)
        move_to(customer, supermarket, customer.y, 500)
        move_to(customer, supermarket, 600, customer.x)
    elif customer.x == 550: # spices
        move_to(customer, supermarket, 450, customer.x)
        move_to(customer, supermarket, customer.y, 355)
        move_to(customer, supermarket, 600, customer.x)
    elif customer.x == 315: #dairy
        move_to(customer, supermarket, 450, customer.x)
        move_to(customer, supermarket, customer.y, 218)
        move_to(customer, supermarket, 600, customer.x)
    else: # drinks
        move_to(customer, supermarket, 600, customer.x)
