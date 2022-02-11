import time


def check_color(color):

    if color.startswith("R"):
        return 1
    elif color.startswith("Y"):
        return 2
    elif color.startswith("G"):
        return 3
    else:
        raise ValueError("There is a problem in traffic lights work. It has been stopped.")


class TrafficLight:

    _color = None
    traffic_lights = {
         'Red': 7,
         'Yellow': 2,
         'Green': 7
     }


    def running(self):
        color_count = 0
        while True:
            for el in TrafficLight.traffic_lights:
                try:
                    check_color(el)
                except ValueError:
                    print("There is a problem in traffic lights work. It has been stopped.")
                    break
                else:
                    print(el)
                    color_count += 1
                    time.sleep(TrafficLight.traffic_lights.get(el))



traffic = TrafficLight()
traffic.running()
