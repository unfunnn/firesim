# firesim
DOOM PSX fire simulation using pygame
## How it works
It is heavily based on this paper: https://fabiensanglard.net/doom_fire_psx/, and it follows essentially the same principals:
- A row of infinitely "heated" pixels is created at the bottom
- The heat then "diffuses" upwards at a random rate. In my implimentation that around the intensity value given
- You then render via any media (in my case pygame)
