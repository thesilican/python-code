from enum import Enum
# ---------- Indices ----------
LIFEPOINTS = 0
HAPPINESS = 1
HUNGER = 2
HEALTH = 3
WEIGHT = 4
DISCIPLINE = 5
POOP = 6

# ---------- Variable limits ----------
LIFEPOINTS_MAX = 100
HAPPINESS_MAX = 100
HUNGER_MAX = 100
HEALTH_MAX = 100
WEIGHT_MAX = 100
DISCIPLINE_MAX = 100
POOP_MAX = 20
VARIABLES_MAX = [LIFEPOINTS_MAX, HAPPINESS_MAX,
                 HUNGER_MAX, HEALTH_MAX, WEIGHT_MAX,
                 DISCIPLINE_MAX, POOP_MAX]

# ---------- Initial Variables ----------
LIFEPOINTS_INIT = 100
HAPPINESS_INIT = 80
HUNGER_INIT = 0
HEALTH_INIT = 80
WEIGHT_INIT = 30
DISCIPLINE_INIT = 50
POOP_INIT = 0
VARIABLES_INIT = [LIFEPOINTS_INIT, HAPPINESS_INIT,
                  HUNGER_INIT, HEALTH_INIT, WEIGHT_INIT, DISCIPLINE_INIT, POOP_INIT]

# ---------- Pet types ----------


class PetTypes(Enum):
    CAT = 0

#---------- Random Config ----------
