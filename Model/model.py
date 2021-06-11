
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
    email  as primary key
    password
"""

# restaurant
"""
    name as primary key
    region
    address
    serving regions   "a text of regions with , between them"
    work hours        "text with this format   open_hour:close_hour"
    delivery time
    delivery fee
    'manager' foreign key to manager email
"""


# food
"""
    id as primary key 
    name  unique
"""

# relation between food and restaurant
"""
    restaurant_id foreign key to restaurant name }
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
    user_phone foreign key to user phone number
    restaurant_name   foreign key to name
    food_id  foreign key to id
    count
    status
    date
"""
