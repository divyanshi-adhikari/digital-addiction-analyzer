from model import predict_addiction

print("===== MindTrack AI =====")
print("Analyze your digital habits\n")

# Input
screen_time = float(input("Screen time (hours): "))
social_media = float(input("Social media hours: "))
sleep = float(input("Sleep hours: "))
study = float(input("Study hours: "))

# Prediction
result = predict_addiction([screen_time, social_media, sleep, study])

print("\nAddiction Level:", result)