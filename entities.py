from math import radians, cos, sin, atan2, sqrt

MAX_SPEED = 100
SPEED_INCREMENT = 0.2
DECELERATION = -0.02
ROTATION_INCREMENT = 0.05

# determine the points of the new polygon

def rotate_polygon(angle, polygon):
    angle_rad = radians(angle)
    cos_a = cos(angle_rad)
    sin_a = sin(angle_rad)

    new_polygon = []

    for x, y in polygon:
        x2 = x * cos_a - y * sin_a
        y2 = x * sin_a + y * cos_a
        new_polygon.append((x2, y2))

    return new_polygon

# compute a speed vector norm

def compute_speed_vector_norm(speed_vector):
    x, y = speed_vector
    return sqrt(x ** 2 + y ** 2) 

# compute a new speed vector

def determine_speed_vector(angle, speed_value):
    return (speed_value * cos(angle), speed_value * sin(angle))

# compute the angle of a speed vector

def determine_vector_angle(speed_vector):
    x, y = speed_vector
    return atan2(x, y)

# change the norm of the speed vector
#       with value < 0
#         or value > 0

def change_norm_speed_vector(speed_vector, value):
    angle = determine_vector_angle(speed_vector)
    speed_value = compute_speed_vector_norm(speed_vector)
    return determine_speed_vector (angle, speed_value + value)



class Entity():
    def __init__(self, x, y, speed_vector, angle, *polygon):
        self.x = x
        self.y = y
        self.speed_vector = speed_vector
        self.angle = angle
        self.angle_speed = 0
        self.polygon = list(polygon)

    def __str__(self):
        return f'''({self.x}, {self.y})
{self.angle}°, speed={self.speed}, angle_speed={self.angle_speed}
polygon = {self.polygon}\n'''

    def rotate_right(self):
        
        # update angle_speed OR angle 

        if self.angle_speed < 0:
            self.angle_speed += ROTATION_INCREMENT
            if self.angle_speed > 0:
                self.angle_speed = 0
        else:
            self.angle += ROTATION_INCREMENT
            if self.angle > 360:
                self.angle = self.angle - 360 
        
        # update the polygon
        
        new_polygon = rotate_polygon(self.angle, self.polygon) 
        self.polygon.clear()
        self.polygon = new_polygon 

    def rotate_left(self):
         
        # update angle_speed OR angle 

        if self.angle_speed > 0:
            self.angle_speed -= ROTATION_INCREMENT
            if self.angle_speed < 0:
                self.angle_speed = 0 
        else:
            self.angle -= ROTATION_INCREMENT
            if self.angle < 0:
                self.angle = 360 + self.angle 

        # update the polygon
        
        new_polygon = rotate_polygon(self.angle, self.polygon) 
        self.polygon.clear()
        self.polygon = new_polygon 

    def accelerate(self):
        additional_vector = determine_speed_vector(self.angle, SPEED_INCREMENT)
        new_speed_vector = tuple(map(sum, zip(self.speed_vector, additional_vector)))

        if compute_speed_vector_norm(new_speed_vector) <= MAX_SPEED:
            self.speed_vector = new_speed_vector 

    def decelerate(self):
        angle = determine_vector_angle(self.speed_vector)
        speed_value = compute_speed_vector_norm(self.speed_vector)
        speed_value -= SPEED_INCREMENT
        if speed_value > 0:
            self.speed_vector = determine_speed_vector(angle, speed_value)
        else:
            self.speed_vector = (0, 0)

    def update(self, height, width):
        self.angle += self.angle_speed
        self.x += self.speed_vector[0]
        self.y += self.speed_vector[1]

        if self.x > width:
            self.x = self.x - width
        elif self.x < 0:
            self.x = width - self.x

        if self.y > height:
            self.y = self.y - height
        elif self.y < 0:
            self.y = height - self.y
            
        self.speed_vector = change_norm_speed_vector(self.speed_vector, DECELERATION)

    def polygon_to_draw(self):
        return [(self.x + point[0], self.y + point[1]) for point in self.polygon]


if __name__ == '__main__':
    
    my_entity = Entity(50, 100, (0, 0), 0, (-10, 0), (10, 0), (0, 20))
    print('Entity created.\n')
    print(my_entity)

    print('Rotate entity to the left.\n')
    my_entity.rotate_left()
    print(my_entity)

    print('Rotate entity 2x to the right.\n')
    my_entity.rotate_right()
    my_entity.rotate_right()
    print(my_entity)
