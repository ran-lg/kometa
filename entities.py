from math import radians, cos, sin

MAX_SPEED = 100
SPEED_INCREMENT = 5
ROTATION_INCREMENT = 0.5

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


class Entity():
    def __init__(self, x, y, speed, angle, *polygon):
        self.x = x
        self.y = y
        self.speed = speed
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
        pass

    def decelarate(self):
        pass

    def update(self):
        self.angle += self.angle_speed
        
        # TBD

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

