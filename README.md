A small game project with pygame :)

-----------------------------------------------

Controlls:

WASD - Movement
ARROWS - Shooting
Shift - Running

As the Level Increases, enemies will spawn quicker.
Survive as long as you can while and shoot for that hih score!

-----------------------------------------------

Changelog


v1.0

- And we are live!
- The player can walk and shoot
- Enemies spawn at the screen edges
- Shooting an enemy kills it and rewards you 1 Score
- There is no way for the player to die
- As time passes, the 'Level' increases, wich makes enemies spawn faster.


v1.1

- Enemies now spawn outside the screen and walk towards it.
- Enemies now shoot the player (seems to no kill him tho, go figure).
- At 'Level MAX(4)' enemies are able to walk towards the middle of the screen instead of being limited to the edges.


v1.2
- A tiny bit of cleanup in code logic
- When the player is shot the game closes


v1.3
- 'Level' was renamed to 'Threat'
- Implemented code to Save High Score
- Score, High Score and Threat Level are displayed on screen
- At "MAX THREAT" the game does a better job at showing it has reached bullet hell
- The game can be played using the browser now (anarkhi.github.io/Shootout-Night/)


v1.4
- Fix a bug where the wait time between shots would reset no matter if you shoot or not, it should feel way better now
- Added Sounds for when the player shoots, and when the time between shots hits 0 (Reload Sound)