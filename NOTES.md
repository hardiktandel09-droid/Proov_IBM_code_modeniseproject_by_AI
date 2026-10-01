# What I checked, and what the agent got wrong
The maintenance service used integer division for the ratio, so every partial value was floored to zero.

## Why it was dangerous 
It silently removed the whole 80 to 99.9 percent warning window. That's about 3000km of early warning per car across 6000 cars, so vehicle could have reached breakdown with no alert and no chance to service them first. 

## What I checked before I accepted its work
I checked that Agent has performed accurately according to the prompt as I mention in it - replaced whole division to true division, modernised print sentenced and add test and check all test results.


