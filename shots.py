import matplotlib
import pandas as pandas
import nbashots as nba

curry_id = nba.get_player_id("Curry, Stephen")[0]
print type(curry_id)