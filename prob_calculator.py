import copy
import random
class Hat:
    def __init__(self, **hats):
        self.contents = list()
        for key, val in hats.items():
            for i in range(val):
                self.contents.append(key)
        #print('original hat', self.contents)
    def draw(self, num):
        if len(self.contents) <= num:
            return self.contents
        else:
            drawn_balls = list()
            for j in range(num):
                drawn = random.sample(self.contents, 1) #can also use choices(), randrange(), randint() giving the same result
                drawn_balls += drawn
                for item in drawn:
                    if item in self.contents:
                        self.contents.remove(item)
                #print('drawn', drawn)
            #print('collect drawn balls', drawn_balls)
            #print('Left in the hat', self.contents)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    event = 0
    for experiment in range(num_experiments):
        expected = list()
        for c, n_ball in expected_balls.items():
            for color in range(n_ball):
                expected.append(c)
        new_hat = copy.deepcopy(hat)
        sample_list = new_hat.draw(num_balls_drawn)
        ### if sample have the least number of expected balls, count as 1 event
        ### here we draw xx balls (number) more than the expected balls
        ### means that the matched color of sample can be >= the amount of expected balls
        for color in sample_list:
            if color in expected:
                expected.remove(color)
        if len(expected) == 0:
            event += 1
            #print('event + 1')
        #print('Left in expected list', expected)
        probability = event / num_experiments
    return probability

#hat = Hat(black=6, red=4, green=3)
#hat.draw(14)
#experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=3, num_experiments=2000)
#hat = Hat(red=5,blue=2)
#hat.draw(2)
#hat = Hat(blue=3,red=2,green=6)
#experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
#expected = 0.272
