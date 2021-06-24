import onnx
model=onnx.load("/home/jnano/Downloads/jetson-inference/python/training/classification/myModel/resnet18.onnx")
onnx.checker.check_model(model)