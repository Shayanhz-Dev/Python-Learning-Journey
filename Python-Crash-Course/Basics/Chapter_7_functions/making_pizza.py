# Hi I'm shayan and today I want t practice about functuin
# importing module and call
# importing functions and call

import pizza_2

pizza_2.make_pizza(16, 'pepperoni')
pizza_2.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

from pizza import make_pizza

make_pizza(22, 'chicken')
make_pizza(15, 'mushrooms')

from pizza import make_pizza as p

p(22, 'potato')