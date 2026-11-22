label chapter_1_6:
with irisin

show CG1:
    alpha 0.25
with Dissolve(2)
shq "{cps=10}{shader=jitter}It’s scary{w=.5}, isn’t it[kw]"
show CG1:
    alpha 0.5
with Dissolve(2)
shq "{cps=15}{shader=jitter}I’m scared, too[kw]{w=1} I’m scared of everything[kw]"
show CG1:
    alpha 0.75
with Dissolve(2)
shq "{cps=30}{shader=jitter}Especially you!"
show CG1

scene black
with Dissolve(3)
with Pause(4)