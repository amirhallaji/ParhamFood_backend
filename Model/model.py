
# User
"""
    id as primary key
    name
    password
    phone number
    region
    address
    credit
"""


# manager
"""
    id as primary key
    name
    email 
    password
"""

# restaurant
"""
    id as primary key
    name 
    region
    address
    serving regions   "a text of regions with , between them"
    work hours        "text with this format   open_hour:close_hour"
    delivery time
    delivery fee
    'manager' foreign key to manager id
"""


# food
"""
    id as primary key 
    name  unique
"""

# relation between food and restaurant
"""
    restaurant_id foreign key to restaurant id  }
    food_id foreign key to food, food id         } => both as primary key
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
    user_id foreign key to user id
    restaurant_id   foreign key to id
    food_id  foreign key to id
    count
    status
    date
"""
