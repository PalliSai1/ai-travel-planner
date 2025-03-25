import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
temperature=ctrl.Antecedent(np.arange(0,108,1),'temperature')
fanspeed=ctrl.Consequent(np.arange(0,100,1),'fanspeed')
temperature['cold']=fuzz.gaussmf(temperature.universe,15,10)
temperature['warm']=fuzz.gaussmf(temperature.universe,50,10)
temperature['hot']=fuzz.gaussmf(temperature.universe,90,10)
fanspeed['slow']=fuzz.gaussmf(fanspeed.universe,20,10)
fanspeed['medium']=fuzz.gaussmf(fanspeed.universe,50,10)
fanspeed['fast']=fuzz.gaussmf(fanspeed.universe,90,10)
rule1=ctrl.Rule(temperature['cold'],fanspeed['slow'])
rule2=ctrl.Rule(temperature['warm'],fanspeed['medium'])
rule3=ctrl.Rule(temperature['hot'],fanspeed['fast'])
fanspeed_ctrl=ctrl.ControlSystem([rule1,rule2,rule3])
fanspeeding=ctrl.ControlSystemSimulation(fanspeed_ctrl)
temperature_input = 9
fanspeeding.input['temperature'] = temperature_input
fanspeeding.compute()
print(f"Fan speed for {temperature_input}°C is: {fanspeeding.output['fanspeed']:.2f}%")


