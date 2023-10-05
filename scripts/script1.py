
# Moving Leg

Simple script that ...
```
import pymunk
body = pymunk.Body(1,2, body_type=pymunk.Body.KINEMATIC)
def sine_wave(body, gravity, damping, dt):
    body.velocity = ... # a vector of the velocity x and y.

body.velocity_func = sine_wave
```
