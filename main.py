import time
import view, model, controller

while True:
    time.sleep(1/100)
    controller.process_events()
    model.step()
    view.draw()