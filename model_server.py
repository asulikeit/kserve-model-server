from kserve import Model, ModelServer
import numpy as np

class DummyModel(Model):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = name
        self.ready = True

    def predict(self, payload: dict, headers=None):
        inputs = payload["instances"]
        return {"predictions": [[x[0] + 1] for x in inputs]}

if __name__ == "__main__":
    model = DummyModel("dummy-model")
    ModelServer().start([model])
