from .predictor import predict

input_text = "What is the capital of France?"
print("Input text:", input_text)
prediction = predict(input_text)
print("Prediction:", prediction)