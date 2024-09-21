import cv2
import pandas as pd

df = pd.read_csv('participants.csv')

# list_names = df.values.tolist()

list_names = [['Abirup Kumar Ghosh', '3rd', 'CSBS']]

area = (304, 560, 1113, 617)
area2 = (361, 656, 1065, 697)

for index, name in enumerate(list_names):
    template = cv2.imread('certtemplate.jpg')
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1.0  # Adjust the font scale as needed
    thickness = 2
    text_size = cv2.getTextSize(name[0], font, font_scale, thickness)[0]
    
    # Calculate position for the first element (name)
    x = area[0] + (area[2] - area[0] - text_size[0]) // 2
    y = area[1] + (area[3] - area[1] - text_size[1]) // 2 + 20  # Adjusted y coordinate
    cv2.putText(template, name[0], (x, y), font, font_scale, (0, 0, 0), thickness)
    
    # Combine year and department for the second text
    text2 = f"{name[2]} {name[1]} year"
    text_size = cv2.getTextSize(text2, font, font_scale, thickness)[0]
    x = area2[0] + (area2[2] - area2[0] - text_size[0]) // 2
    y = area2[1] + (area2[3] - area2[1] - text_size[1]) // 2 + 20  # Adjusted y coordinate
    cv2.putText(template, text2, (x, y), font, font_scale, (0, 0, 0), thickness)
    
    cv2.imwrite(f"generated/{name[0]}.jpg", template)
    print(f'processing certificate {index+1}/{len(list_names)}')
