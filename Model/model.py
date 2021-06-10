
# User
"""
    name
    password
    phone number as primary key
    region
    address
    credit
"""


# manager
"""
    name
    email as primary key
    password
"""

# restaurant
"""
    'manager' foreign key to manager email address
    name as primary key
    region
    address
    serving regions
    work hours
    delivery time
    delivery fee
"""


# food
"""
    name as primary key
"""

# relation between food and restaurant
"""
    restaurant_name foreign key to restaurant name  }
    food_name foreign key to food food name         } => both as primary key
    count
    copen_type = Default : None
    price
    disabled = Default : False
"""


# comment
"""
    'order id' as foreign key to order_id and primary key
    score
    content
    manager_reply
"""


# order
"""
    'order id' as primary key
    user foreign key to user phone number
    restaurant_name   foreign key to restaurant name
    food_name  foreign key to food name
    count
    status
    date
"""


# order (for order history)
"""
    'user id'
    
"""