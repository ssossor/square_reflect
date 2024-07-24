# Tiles code :

empty 00
block 01
ghostblock 02
key 03
lock 04
kill 05
start top ?1
start right ?2
start down ?3
start left ?4
end top !1
end right !2
end down !3
end left !4
angle top left A1
angle top right A2
angle bot right A3
angle bot left A4
ghost angle top left a1
ghost angle top right a2
ghost angle bot right a3
ghost angle bot left a4

# Direction

no direction 0
up 1
right 2
down 3
left 4

# State

state[0] pos
state[1] direction
state[2] keys

# Boardsize

boardsize[0] width
boardsize[1] height